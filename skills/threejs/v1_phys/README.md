# ThreeJSEvolution Engine v1_phys - 物理引擎演示

## 📊 进化状态

| 版本 | 名称 | 功能 | 状态 |
|------|------|------|------|
| ✅ v1_base | 基础场景 | Three.js 基础场景、相机、几何体 | 已完成 |
| ⏳ v1_opt | 鼠标交互 | Raycaster 鼠标拾取、悬停高亮 | 待审核 |
| 🎮 v1_phys | 物理引擎 | Cannon.js 重力、碰撞、刚体动力学 | **当前版本** |
| 📋 v1_anim | 动画系统 | 关键帧动画、骨骼动画 | 计划中 |
| 📋 v2_core | ECS系统 | 实体组件系统 | 计划中 |

## 🧪 当前版本功能

- ✅ 重力模拟 (-9.82 m/s²)
- ✅ 刚体碰撞检测 (Box, Sphere)
- ✅ 物理材质 (摩擦力、弹性)
- ✅ 鼠标点击施加力
- ✅ 动态物体生成
- ✅ 实时物理同步

## 🎮 在线演示

访问: [v1_phys 物理引擎演示](skills/threejs/v1_phys/index.html)

## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/perlinson/ThreeJSEvolution.git

# 进入目录
cd ThreeJSEvolution/skills/threejs/v1_phys

# 用浏览器打开 index.html
# 或使用本地服务器
npx serve .
```

## 📁 文件结构

```
v1_phys/
├── index.html          # 主页面 (物理引擎演示)
├── README.md           # 本文档
└── assets/             # 资源文件
    └── ...
```

## 🔧 技术栈

- **Three.js** r128 - 3D 渲染
- **Cannon.js** 0.6.2 - 物理引擎
- **WebGL** - 图形渲染

## 📈 性能指标

- FPS: 60
- 物体数量: 10+
- 物理精度: 1/60s 步长
- 渲染延迟: < 16ms

## 🎯 下一步

1. 实现动画系统 (v1_anim)
2. 实现实体组件系统 (v2_core)
3. 实现场景管理 (v2_scene)

## 📞 联系

- GitHub: https://github.com/perlinson/ThreeJSEvolution
- Issues: https://github.com/perlinson/ThreeJSEvolution/issues

---

**🦞 让 OpenClaw 写游戏越来越强！**
