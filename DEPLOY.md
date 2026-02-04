# 🦞 OpenClaw Evolution Registry - Three.js 进化系统

> 🎯 **让 OpenClaw 写 Three.js 游戏越来越强！**

## 🚀 快速部署

### 方式 A: 一键部署（推荐）

```bash
cd evolution-registry
chmod +x deploy.sh
./deploy.sh
```

按照提示输入你的 GitHub 用户名即可。

### 方式 B: 手动部署

```bash
# 1. 创建 GitHub 仓库
gh repo create ThreeJSEvolution --public --description "OpenClaw Evolution Registry"

# 2. 推送代码
git remote add origin git@github.com:你的用户名/ThreeJSEvolution.git
git push -u origin main

# 3. 启用 GitHub Pages
# 访问: https://github.com/你的用户名/ThreeJSEvolution/settings/pages
# Source: Deploy from a branch → main / (root)
```

## 🌐 访问网站

部署完成后，网站将在这里可用：

```
https://你的用户名.github.io/ThreeJSEvolution/
```

**示例（部署后）：**
- 👤 GitHub 用户名: `perlinson`
- 🌐 网站地址: `https://perlinson.github.io/ThreeJSEvolution/`

## 📋 已完成

- ✅ Three.js 基础基因 (v1_base)
- ✅ 鼠标交互优化 (v1_opt)
- ✅ 进化追踪系统
- ✅ GitHub Actions 自动部署
- ✅ 现代化 Web UI
- ✅ 进化树可视化
- ✅ 在线演示页面

## 🧬 进化状态

```
🧬 gen-v1-base (✅ 已批准)
   └── Three.js 基础场景
   └── 120 行代码
   └── ⭐☆☆☆☆ 复杂度

⏳ gen-v1-opt-mouse-v1 (⏳ 待审核)
   └── 鼠标交互功能
   └── +25% UX 提升
   └── 📝 等待合并
```

## 🔄 持续更新

每次向 `main` 分支推送代码时：

1. 🚀 GitHub Actions 自动部署
2. 🌐 网站在 1-2 分钟内更新
3. 📊 进化日志自动记录

### 添加新 Mutation

```bash
# 1. 创建新分支
git checkout -b feature/新功能

# 2. 改进代码...
# 编辑 skills/threejs/*/index.html

# 3. 记录 Mutation
python3 scripts/evolution_tracker.py log \
    gen-v1-opt-mouse-v1 \
    xiaobao-01 \
    threejs-game \
    feature_addition \
    "添加新功能描述" \
    "+10% 性能提升" < patch.diff

# 4. 提交并推送
git add -A
git commit -m "🧬 Add: 新功能描述"
git push origin feature/新功能

# 5. 创建 Pull Request
gh pr create --title "🧬 Add: 新功能描述" --body "..."
```

## 📁 项目结构

```
ThreeJSEvolution/
├── 🏠 index.html                 # GitHub Pages 主页
├── 🧬 mutations/                  # 基因突变记录
│   ├── gen-v1-base.json
│   └── gen-v1-opt-mouse-v1.json
├── 📄 patches/                    # 代码补丁
│   └── gen-v1-opt-mouse-v1.patch
├── 🎮 skills/threejs/             # Three.js 演示
│   └── v1_base/index.html        # 基础场景
├── 🔧 scripts/
│   ├── evolution_tracker.py      # 进化追踪器
│   └── init_gene_repo.sh         # 初始化脚本
└── 🚀 .github/workflows/
    ├── deploy.yml               # 自动部署
    └── validate.yml             # 验证 Mutation
```

## 🎯 Three.js 进化路线

| 版本 | 功能 | 状态 |
|------|------|------|
| v1_base | 基础场景、几何体、光照 | ✅ |
| v1_opt | 鼠标交互、Raycaster | ⏳ |
| v2_phys | 物理引擎 (Cannon.js) | 📋 |
| v2_light | 高级光照、阴影 | 📋 |
| v3_full | 完整 3D 冒险游戏 | 🎯 |

## 🤝 参与贡献

1. ⭐ Star 本仓库
2. 🍴 Fork 项目
3. 🌿 创建分支: `git checkout -b feature/xxx`
4. 📝 提交改进
5. 📤 推送分支
6. 🔀 创建 Pull Request

## 📞 联系

- 🐛 Issues: https://github.com/你的用户名/ThreeJSEvolution/issues
- 💬 Discussions: https://github.com/你的用户名/ThreeJSEvolution/discussions

---

**🦞 让 OpenClaw 越来越强！🧬**
