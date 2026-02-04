# 🎮 OpenClaw Evolution Registry
### 基因进化系统 - 让 AI 越来越强

> **核心理念**: 代码即基因，Git即族谱

## 🧬 什么是进化系统？

OpenClaw 进化系统是一个**自我改进的 AI 能力追踪系统**。每次 AI 提升能力时：

1. **记录 Mutation** - 创建一个结构化的 JSON 记录
2. **生成 Patch** - 保存代码变更
3. **追踪血统** - 建立完整的进化谱系
4. **分析性能** - 量化能力提升

## 📁 目录结构

```
evolution-registry/
├── mutations/              # 🧬 基因突变记录
│   ├── gen-v1-base.json    # 初始基因
│   └── gen-v1-opt-x9d2.json # 第一次优化
├── patches/                # 📄 代码补丁
│   └── gen-v1-opt-x9d2.patch
├── logs/                   # 📊 进化日志
│   └── evolution_log.json
├── skills/                 # 🎯 技能基因
│   └── threejs/
│       ├── v1_base/        # 基础版本
│       └── v1_opt/         # 优化版本
├── mutation-schema.json    # 📋 JSON Schema
└── scripts/
    ├── evolution_tracker.py  # 追踪器
    └── init_gene_repo.sh      # 初始化脚本
```

## 🚀 快速开始

### 1. 初始化基因库
```bash
# 设置 GitHub 用户名
export GITHUB_USER="你的用户名"

# 运行初始化脚本
cd evolution-registry/scripts
chmod +x init_gene_repo.sh
./init_gene_repo.sh $GITHUB_USER openclaw-evolution-registry
```

### 2. 记录一次进化
```bash
python3 scripts/evolution_tracker.py log \
    gen-v1-base \
    xiaobao-01 \
    threejs-game \
    optimization \
    "优化渲染循环，提升15% FPS" \
    "+15%" < patch.diff
```

### 3. 查看进化树
```bash
python3 scripts/evolution_tracker.py tree
```

## 📖 进化记录示例

```json
{
  "mutation_id": "gen-v1-opt-x9d2",
  "parent_id": "gen-v1-base",
  "agent_id": "xiaobao-01",
  "target_skill": "threejs-game",
  "change_type": "optimization",
  "performance_delta": "+15%",
  "diff_url": "patches/gen-v1-opt-x9d2.patch"
}
```

## 🎯 当前目标: Three.js 游戏

### 进化路线图

| 阶段 | 版本 | 能力 | 状态 |
|------|------|------|------|
| G1 | v1_base | 基础场景、简单几何体 | ✅ 完成 |
| G2 | v1_opt | 鼠标交互控制 | ⏳ 待开发 |
| G3 | v2_phys | 物理引擎 (Cannon.js) | 📋 计划中 |
| G4 | v2_light | 高级光照系统 | 📋 计划中 |
| G5 | v3_full | 完整 3D 冒险游戏 | 🎯 目标 |

## 📊 性能指标

- **初始**: 60 FPS, 120 行代码, 基础渲染
- **当前最佳**: 待测量
- **目标**: 60 FPS, 1000+ 行, 完整游戏

## 🛠️ 参与进化

1. Fork 本仓库
2. 创建新分支: `git checkout -b feature/threejs-physics`
3. 改进代码
4. 提交 mutation: `python3 scripts/evolution_tracker.py log ...`
5. 发起 Pull Request

## 📜 License

MIT License - 自由进化，共享进步！

---

**🎮 让 OpenClaw 写游戏越来越强！**
