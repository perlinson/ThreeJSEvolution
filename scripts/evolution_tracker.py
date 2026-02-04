#!/usr/bin/env python3
"""
🎯 OpenClaw Evolution Tracker
基因进化追踪器 - 记录每一次能力提升

核心功能：
1. 记录 mutation log
2. 生成 diff patch
3. 追踪进化谱系
4. 分析性能变化
"""

import json
import hashlib
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import sys

class EvolutionTracker:
    """基因进化追踪器"""

    def __init__(self, registry_path: str = "./evolution-registry"):
        self.registry = Path(registry_path)
        self.mutations_dir = self.registry / "mutations"
        self.patches_dir = self.registry / "patches"
        self.logs_file = self.registry / "logs" / "evolution_log.json"

        # 确保目录存在
        self.mutations_dir.mkdir(parents=True, exist_ok=True)
        self.patches_dir.mkdir(parents=True, exist_ok=True)
        self.logs_file.parent.mkdir(parents=True, exist_ok=True)

    def generate_mutation_id(self, version: str, skill: str) -> str:
        """生成唯一的进化ID"""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        random_suffix = hashlib.md5(f"{version}{skill}{timestamp}".encode()).hexdigest()[:4]
        return f"gen-{version}-{random_suffix}"

    def log_mutation(self,
                      parent_id: str,
                      agent_id: str,
                      skill: str,
                      change_type: str,
                      description: str,
                      diff_content: str,
                      performance_delta: str = "+0%",
                      metrics: Optional[Dict] = None) -> str:
        """记录一次基因突变"""

        # 生成新 ID
        version = parent_id.split('-')[1]  # 从 parent 提取版本
        mutation_id = self.generate_mutation_id(version, skill)

        # 构建 mutation 数据
        mutation = {
            "mutation_id": mutation_id,
            "parent_id": parent_id,
            "agent_id": agent_id,
            "target_skill": skill,
            "change_type": change_type,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "performance_delta": performance_delta,
            "diff_url": f"patches/{mutation_id}.patch",
            "description": description,
            "changelog": [description],
            "metrics": metrics or {
                "code_lines": len(diff_content.split('\n')),
                "complexity": "★★☆☆☆",
                "test_coverage": "0%"
            },
            "approved": False
        }

        # 保存 mutation
        mutation_file = self.mutations_dir / f"{mutation_id}.json"
        with open(mutation_file, 'w', encoding='utf-8') as f:
            json.dump(mutation, f, indent=2, ensure_ascii=False)

        # 保存 patch
        patch_file = self.patches_dir / f"{mutation_id}.patch"
        with open(patch_file, 'w', encoding='utf-8') as f:
            f.write(diff_content)

        # 更新主日志
        self._append_to_log(mutation)

        print(f"🧬 Mutation 记录成功: {mutation_id}")
        print(f"📁 Patch: {patch_file}")
        print(f"📊 性能变化: {performance_delta}")

        return mutation_id

    def _append_to_log(self, mutation: Dict):
        """追加到主日志"""
        logs = []
        if self.logs_file.exists():
            with open(self.logs_file, 'r', encoding='utf-8') as f:
                logs = json.load(f)

        logs.append({
            "id": mutation["mutation_id"],
            "parent": mutation["parent_id"],
            "skill": mutation["target_skill"],
            "type": mutation["change_type"],
            "delta": mutation["performance_delta"],
            "timestamp": mutation["timestamp"]
        })

        with open(self.logs_file, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=2)

    def get_evolution_tree(self, mutation_id: str = None) -> Dict:
        """获取进化树"""
        mutations = {}
        for f in self.mutations_dir.glob("*.json"):
            with open(f, 'r') as mf:
                data = json.load(mf)
                mutations[data['mutation_id']] = data

        return mutations

    def compare_mutations(self, id1: str, id2: str) -> Dict:
        """对比两次突变"""
        tracker = EvolutionTracker()
        tree = tracker.get_evolution_tree()

        if id1 not in tree or id2 not in tree:
            raise ValueError(f"未知 mutation ID: {id1} 或 {id2}")

        m1, m2 = tree[id1], tree[id2]

        return {
            "from": id1,
            "to": id2,
            "generations_apart": int(m2['mutation_id'].split('-')[1]) - int(m1['mutation_id'].split('-')[1]),
            "performance_gain": m2['performance_delta'],
            "feature_jumps": len(m2['changelog']) - len(m1['changelog']),
            "lineage": self._get_lineage(m2, tree)
        }

    def _get_lineage(self, mutation: Dict, tree: Dict) -> List[str]:
        """获取血统链"""
        lineage = [mutation['mutation_id']]
        current = mutation
        while current['parent_id'] != 'null' and current['parent_id'] in tree:
            current = tree[current['parent_id']]
            lineage.append(current['mutation_id'])
        return list(reversed(lineage))


def main():
    """命令行入口"""
    tracker = EvolutionTracker()

    if len(sys.argv) < 2:
        print("Usage: python3 evolution_tracker.py <command> [args]")
        print("Commands:")
        print("  log <parent_id> <agent> <skill> <type> <desc> <delta>")
        print("  tree [mutation_id]")
        print("  compare <id1> <id2>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "log":
        if len(sys.argv) < 8:
            print("Usage: evolution_tracker.py log <parent_id> <agent> <skill> <type> <desc> <delta>")
            sys.exit(1)

        parent_id = sys.argv[2]
        agent_id = sys.argv[3]
        skill = sys.argv[4]
        change_type = sys.argv[5]
        description = sys.argv[6]
        performance_delta = sys.argv[7]

        # 读取标准输入的 diff
        diff_content = sys.stdin.read() if not sys.stdin.isatty() else ""

        tracker.log_mutation(
            parent_id=parent_id,
            agent_id=agent_id,
            skill=skill,
            change_type=change_type,
            description=description,
            performance_delta=performance_delta,
            diff_content=diff_content
        )

    elif command == "tree":
        mutation_id = sys.argv[2] if len(sys.argv) > 2 else None
        tree = tracker.get_evolution_tree()
        print(json.dumps(tree, indent=2, ensure_ascii=False))

    elif command == "compare":
        if len(sys.argv) < 4:
            print("Usage: evolution_tracker.py compare <id1> <id2>")
            sys.exit(1)

        result = tracker.compare_mutations(sys.argv[2], sys.argv[3])
        print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
