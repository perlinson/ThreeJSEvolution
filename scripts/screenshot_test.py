#!/usr/bin/env python3
"""
📸 ThreeJSEvolution 页面截图测试
生成详细的测试报告
"""

import subprocess
import json
from datetime import datetime

def run_curl_test():
    """使用 curl 测试页面"""
    print("🧪 页面功能测试")
    print("=" * 70)
    
    pages = [
        ("主页", "https://perlinson.github.io/ThreeJSEvolution/"),
        ("物理引擎 v1.1", "https://perlinson.github.io/ThreeJSEvolution/skills/threejs/v1_phys/index.html"),
        ("动画系统 v1.2", "https://perlinson.github.io/ThreeJSEvolution/skills/threejs/v1_anim/index.html"),
    ]
    
    results = {}
    
    for name, url in pages:
        print(f"\n🔍 测试: {name}")
        print(f"   URL: {url}")
        
        # 获取页面
        result = subprocess.run(
            ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', url],
            capture_output=True, text=True
        )
        status = result.stdout.strip()
        
        if status == '200':
            # 检查关键内容
            content = subprocess.run(
                ['curl', '-s', url],
                capture_output=True, text=True
            ).stdout
            
            checks = {
                'HTML结构': '<!DOCTYPE html>' in content,
                'Canvas元素': '<canvas' in content,
                'JavaScript': '<script>' in content,
                'Three.js引用': 'three.min.js' in content,
                '初始化函数': 'function init()' in content or 'function init()' in content,
                '动画循环': 'requestAnimationFrame' in content,
                '按钮元素': 'onclick=' in content or 'button' in content.lower(),
                '控制面板': 'id="info"' in content or 'id="controls"' in content,
            }
            
            print(f"   ✅ HTTP 状态: {status}")
            print(f"   📊 内容检查:")
            
            all_pass = True
            for check, passed in checks.items():
                symbol = "✅" if passed else "❌"
                print(f"      {symbol} {check}")
                if not passed:
                    all_pass = False
            
            results[name] = {
                'status': status,
                'url': url,
                'passed': all_pass,
                'checks': checks
            }
        else:
            print(f"   ❌ HTTP 状态: {status}")
            results[name] = {
                'status': status,
                'passed': False,
                'error': f'HTTP {status}'
            }
    
    # 总结
    print()
    print("=" * 70)
    print("📋 测试总结")
    print("=" * 70)
    
    passed_count = sum(1 for r in results.values() if r.get('passed', False))
    total_count = len(results)
    
    print(f"✅ 通过: {passed_count}/{total_count}")
    print(f"❌ 失败: {total_count - passed_count}/{total_count}")
    print()
    
    if passed_count == total_count:
        print("🎉 所有测试通过！")
        print()
        print("💡 如果页面点击没反应，可能的原因:")
        print("   1. 浏览器缓存 - 尝试 Ctrl+F5 强制刷新")
        print("   2. JavaScript 被阻止 - 检查浏览器设置")
        print("   3. CDN 加载问题 - 检查网络连接")
        print("   4. 浏览器兼容 - 尝试其他浏览器")
        print()
        print("🔗 直接访问:")
        for name, data in results.items():
            print(f"   - {name}: {data['url']}")
    else:
        print("❌ 有测试失败，请检查上方输出")
    
    print()
    print("=" * 70)
    
    return passed_count == total_count

if __name__ == "__main__":
    print("=" * 70)
    print("📸 ThreeJSEvolution 页面功能测试")
    print(f"🕐 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    print()
    
    success = run_curl_test()
    exit(0 if success else 1)
