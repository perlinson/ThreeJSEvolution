# 🎮 ThreeJSEvolution
### AI游戏引擎 - 为AI Agent打造的3D游戏开发框架

> **核心理念**: 让AI Agent能快速构建有趣的游戏

## 🎯 v2.2 更新：AI敌人系统 (2026-02-10)

**新增功能**:
- **Enemy 类**: 智能敌人AI（近战、远程、BOSS）
- **状态机**: IDLE → PATROL → CHASE → ATTACK → FLEE → DEAD
- **敌人生成器**: EnemySpawner 支持批量生成敌人波次
- **血条系统**: 实时血量显示
- **受伤反馈**: 闪烁效果和伤害数值

**敌人类型**:
| 类型 | 颜色 | 特点 |
|------|------|------|
| 近战 | 橙色 | 主动接近玩家，近距离攻击 |
| 远程 | 红色 | 发射投射物，远程消耗 |
| BOSS | 紫色 | 高血量，高伤害，大范围检测 |

**AI行为**:
- 巡逻模式：按预设路径移动
- 追逐模式：检测到玩家后紧追不舍
- 攻击模式：接近后造成伤害
- 逃亡模式（可选）：血量低时逃跑

## 📁 项目结构

```
ThreeJSEvolution/
├── index.html           # 核心演示
├── physics-demo.html    # 物理引擎演示
├── combat-demo.html     # 战斗系统演示
├── enemy-demo.html      # AI敌人系统演示 ✨NEW
├── level-editor.html    # 关卡编辑器
├── platform-game.html   # 平台跳跃游戏
└── src/
    ├── GameEngine.js    # 核心引擎
    ├── PhysicsWorld.js  # 物理引擎
    ├── AnimationSystem.js # 动画系统
    ├── ParticleSystem.js # 粒子系统
    ├── Sound/           # 音效系统 (v2.1)
    └── AI/
        └── Enemy.js     # AI敌人系统 ✨NEW
```

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

## 🚀 快速开始

### 1. 运行AI敌人演示
```bash
cd ThreeJSEvolution
python3 -m http.server 8080
# 打开浏览器访问 http://localhost:8080/enemy-demo.html
```

### 2. 创建自定义敌人
```javascript
import { Enemy, EnemySpawner } from './src/AI/Enemy.js';

// 创建敌人
const enemy = new Enemy({
    type: 'melee',           // 近战/远程/boss
    health: 100,             // 生命值
    speed: 3,                // 移动速度
    damage: 10,              // 攻击力
    detectionRange: 15,     // 检测范围
    attackRange: 2          // 攻击范围
});

// 添加巡逻路径
enemy.addPatrolPoint(new THREE.Vector3(0, 1, 0));
enemy.addPatrolPoint(new THREE.Vector3(10, 1, 0));

// 设置追踪目标
enemy.setTarget(player);

// 敌人生成器
const spawner = new EnemySpawner(scene);

// 生成敌人波次
spawner.spawnWave({
    melee: 3,    // 近战敌人数量
    ranged: 2,   // 远程敌人数量
    boss: true   // 是否包含BOSS
});
```

### 3. 游戏循环中更新
```javascript
const gameState = {
    player: player,
    projectiles: projectiles
};

// 每帧更新敌人AI
spawner.enemies.forEach(enemy => {
    enemy.setTarget(gameState.player);
    enemy.update(deltaTime, gameState);
});
```

## 🎮 功能特性

### 核心引擎
- ✅ 3D场景渲染
- ✅ 物理碰撞系统
- ✅ 角色控制器
- ✅ 动画系统
- ✅ 粒子特效
- ✅ 音效系统

### AI系统
- ✅ 敌人AI状态机
- ✅ 巡逻/追逐/攻击行为
- ✅ 远程射击机制
- ✅ BOSS战支持
- ✅ 血条显示
- ✅ 受伤反馈

### 工具系统
- ✅ 关卡编辑器
- ✅ 存档系统
- ✅ 游戏模板生成器

## 📊 代码统计

| 模块 | 代码行数 | 状态 |
|------|----------|------|
| 核心引擎 | 1000+ | ✅ 稳定 |
| 物理系统 | 500+ | ✅ 稳定 |
| 动画系统 | 300+ | ✅ 稳定 |
| 粒子系统 | 400+ | ✅ 稳定 |
| 音效系统 | 200+ | ✅ 稳定 |
| AI敌人系统 | 500+ | ✨ 新增 |

## 🎯 计划功能

- [ ] AI敌人寻路 (A* Pathfinding)
- [ ] 群体AI行为 (Flocking)
- [ ] 玩家技能系统
- [ ] 关卡目标与任务
- [ ] 网络同步支持

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
