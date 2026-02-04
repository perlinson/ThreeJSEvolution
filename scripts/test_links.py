#!/usr/bin/env python3
"""
🌐 ThreeJSEvolution Link Checker
检查所有演示链接是否可访问
"""

import urllib.request
import urllib.error
import json
from datetime import datetime

BASE_URL = "https://perlinson.github.io/ThreeJSEvolution"

# 所有需要检查的链接
LINKS = [
    ("主页", f"{BASE_URL}/"),
    ("基础演示", f"{BASE_URL}/skills/threejs/v1_base/index.html"),
    ("物理引擎 v1.1", f"{BASE_URL}/skills/threejs/v1_phys/index.html"),
    ("动画系统 v1.2", f"{BASE_URL}/skills/threejs/v1_anim/index.html"),
    ("架构文档", f"{BASE_URL}/skills/threejs/ENGINE_ARCHITECTURE.md"),
]

def check_link(name, url):
    """检查链接是否可访问"""
    print(f"🔍 检查: {name}")
    print(f"   URL: {url}")
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            status = response.status
            size = len(response.read())
            
            if status == 200:
                print(f"   ✅ 状态: 200 OK")
                print(f"   📦 大小: {size:,} bytes")
                return True
            else:
                print(f"   ❌ 状态: {status}")
                return False
                
    except urllib.error.HTTPError as e:
        print(f"   ❌ HTTP 错误: {e.code} - {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"   ❌ 连接错误: {e.reason}")
        return False
    except Exception as e:
        print(f"   ❌ 未知错误: {e}")
        return False

def main():
    print("=" * 70)
    print("🌐 ThreeJSEvolution 链接检查")
    print("=" * 70)
    print(f"🕐 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🎯 基准: {BASE_URL}")
    print("=" * 70)
    print()
    
    results = []
    
    for name, url in LINKS:
        success = check_link(name, url)
        results.append((name, success))
        print()
    
    # 统计
    print("=" * 70)
    print("📊 检查结果统计")
    print("=" * 70)
    
    total = len(results)
    passed = sum(1 for _, s in results if s)
    failed = total - passed
    
    print(f"✅ 通过: {passed}/{total}")
    print(f"❌ 失败: {failed}/{total}")
    print()
    
    if failed > 0:
        print("❌ 失败的链接:")
        for name, success in results:
            if not success:
                print(f"   - {name}")
    else:
        print("🎉 所有链接都正常工作！")
    
    print("=" * 70)
    
    # 返回退出码
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    exit(main())
