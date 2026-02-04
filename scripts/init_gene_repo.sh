#!/bin/bash
"""
🚀 基因库初始化脚本
创建 GitHub 远程仓库并推送初始基因

Usage:
    ./init_gene_repo.sh <github_username> <repo_name>
"""

set -e

GITHUB_USER=${1:-"your-username"}
REPO_NAME=${2:-"openclaw-evolution-registry"}

echo "🦞 初始化 OpenClaw 进化基因库..."
echo "📦 GitHub 用户: $GITHUB_USER"
echo "📛 仓库名: $REPO_NAME"

# 1. 创建 GitHub 仓库（需要 gh CLI 或手动创建）
echo ""
echo "📝 请手动在 GitHub 创建仓库:"
echo "   https://github.com/new?name=$REPO_NAME"
echo ""
read -p "按 Enter 继续（创建后）..."

# 2. 初始化本地 Git
echo ""
echo "🔧 初始化 Git 仓库..."
cd "$(dirname "$0")/../.."

# 如果还没有 Git 仓库
if [ ! -d ".git" ]; then
    git init
    git add -A
    git commit -m "🧬 Initial OpenClaw Evolution Registry

- Three.js v1 基础基因
- Mutation Schema (JSON Schema)
- Evolution Tracker (Python)
- 进化追踪系统就绪

🎯 使命: 让 OpenClaw 写 Three.js 游戏越来越强！"
fi

# 3. 添加远程仓库
REMOTE_URL="git@github.com:$GITHUB_USER/$REPO_NAME.git"
echo ""
echo "🔗 添加远程仓库: $REMOTE_URL"

if ! git remote get-url origin &>/dev/null; then
    git remote add origin "$REMOTE_URL"
fi

# 4. 推送
echo ""
echo "🚀 推送到 GitHub..."
git push -u origin main

echo ""
echo "✅ 基因库初始化完成！"
echo ""
echo "📊 进化统计:"
python3 scripts/evolution_tracker.py tree

echo ""
echo "🔗 远程仓库:"
echo "   https://github.com/$GITHUB_USER/$REPO_NAME"
echo ""
echo "💡 下一步:"
echo "   1. 在 GitHub 上设置 branch protection rules"
echo "   2. 配置 GitHub Actions 自动测试 mutation"
echo "   3. 开始写 Three.js 游戏！"
