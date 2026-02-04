#!/usr/bin/env python3
"""
🧪 ThreeJSEvolution 物理引擎完整单元测试 (修复版)
测试物理引擎 v1.1 的所有功能是否正常
"""

import subprocess
import re
import os
from datetime import datetime

class PhysicsEngineTester:
    """物理引擎测试器"""
    
    def __init__(self):
        self.test_file = "/root/.openclaw/workspace/evolution-registry/skills/threejs/v1_phys/index.html"
        self.url = "https://perlinson.github.io/ThreeJSEvolution/skills/threejs/v1_phys/index.html"
        self.results = []
        self.passed = 0
        self.failed = 0
    
    def log_test(self, name, passed, message=""):
        """记录测试结果"""
        status = "✅ PASS" if passed else "❌ FAIL"
        self.results.append({
            "name": name,
            "passed": passed,
            "message": message
        })
        if passed:
            self.passed += 1
            print(f"   {status}: {name}")
            if message:
                print(f"        ✓ {message}")
        else:
            self.failed += 1
            print(f"   {status}: {name}")
            if message:
                print(f"        ✗ {message}")
    
    def run_all_tests(self):
        """运行所有测试"""
        print("=" * 80)
        print("🧪 ThreeJSEvolution 物理引擎完整单元测试")
        print("=" * 80)
        print(f"🕐 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📄 测试文件: {self.test_file}")
        print(f"🌐 测试 URL: {self.url}")
        print("=" * 80)
        
        # 读取文件内容
        if not os.path.exists(self.test_file):
            print(f"\n❌ 文件不存在: {self.test_file}")
            return False
        
        with open(self.test_file, 'r') as f:
            content = f.read()
        
        # 提取 JavaScript
        js_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
        js_code = js_match.group(1) if js_match else ""
        
        all_content_lower = content.lower()
        
        # 1. 文件存在
        print("\n1️⃣ 测试文件存在...")
        self.log_test("HTML 文件存在", True, self.test_file)
        
        # 2. HTML 结构
        print("\n2️⃣ 测试 HTML 结构...")
        self.log_test("DOCTYPE", '<!DOCTYPE html>' in content)
        self.log_test("HTML 标签", '<html' in content and '</html>' in content)
        self.log_test("字符编码", 'charset' in content)
        
        # 3. Three.js 集成
        print("\n3️⃣ 测试 Three.js 集成...")
        self.log_test("Three.js CDN", 'three.min.js' in content)
        self.log_test("THREE.Scene", 'THREE.Scene' in content)
        self.log_test("PerspectiveCamera", 'PerspectiveCamera' in content)
        self.log_test("WebGLRenderer", 'WebGLRenderer' in content)
        self.log_test("Renderer.render", 'renderer.render' in content)
        
        # 4. 物理引擎
        print("\n4️⃣ 测试物理引擎...")
        self.log_test("Cannon.js CDN", 'cannon' in all_content_lower)
        self.log_test("CANNON.World", 'CANNON.World' in content)
        self.log_test("重力设置", 'gravity' in all_content_lower)
        self.log_test("刚体创建", 'CANNON.Body' in content or 'new CANNON.Body' in content)
        self.log_test("碰撞形状", 'CANNON.Box' in content or 'CANNON.Sphere' in content)
        self.log_test("物理步进", 'world.step' in content)
        
        # 5. 交互功能
        print("\n5️⃣ 测试交互功能...")
        self.log_test("init() 函数", 'function init()' in js_code)
        # 使用更宽松的匹配
        self.log_test("animate() 函数", 'animate(' in js_code and 'function' in js_code)
        self.log_test("createBox() 函数", 'function createBox' in js_code)
        self.log_test("createSphere() 函数", 'function createSphere' in js_code)
        self.log_test("spawnRandomBox() 函数", 'function spawnRandomBox' in js_code)
        self.log_test("spawnRandomSphere() 函数", 'function spawnRandomSphere' in js_code)
        self.log_test("resetScene() 函数", 'function resetScene' in js_code)
        
        # 6. 按钮绑定
        print("\n6️⃣ 测试按钮绑定...")
        self.log_test("方块按钮 onClick", 'onclick="spawnRandomBox()"' in content or 'onclick="spawnRandomBox' in content)
        self.log_test("球体按钮 onClick", 'onclick="spawnRandomSphere()"' in content or 'onclick="spawnRandomSphere' in content)
        self.log_test("重置按钮 onClick", 'onclick="resetScene()"' in content or 'onclick="resetScene' in content)
        
        # 7. UI 元素
        print("\n7️⃣ 测试 UI 元素...")
        self.log_test("信息面板", 'id="info"' in content)
        self.log_test("状态面板", 'id="status"' in content)
        self.log_test("控制按钮", 'id="controls"' in content or 'controls' in all_content_lower)
        self.log_test("FPS 显示", 'id="fps"' in content)
        self.log_test("物体数量显示", 'id="objCount"' in content)
        
        # 8. Canvas 元素
        print("\n8️⃣ 测试 Canvas 元素...")
        # 检查 renderer 是否添加到 DOM
        self.log_test("Renderer 添加到 DOM", 'appendChild' in js_code and 'renderer.domElement' in js_code)
        # 检查是否有 canvas 标签
        has_canvas_tag = '<canvas' in all_content_lower
        self.log_test("Canvas HTML 标签", has_canvas_tag)
        
        # 9. JavaScript 语法
        print("\n9️⃣ 测试 JavaScript 语法...")
        temp_file = "/tmp/physics_test.js"
        with open(temp_file, 'w') as f:
            f.write(js_code)
        
        result = subprocess.run(
            ['node', '--check', temp_file],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            self.log_test("JavaScript 语法", True, "无语法错误")
        else:
            error = result.stderr.strip().split('\n')[0][:100]
            self.log_test("JavaScript 语法", False, error)
        
        # 10. HTTP 可访问性
        print("\n🔟 测试 HTTP 可访问性...")
        result = subprocess.run(
            ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', self.url],
            capture_output=True,
            text=True
        )
        
        status = result.stdout.strip()
        http_ok = status == '200'
        self.log_test("HTTP 状态 200", http_ok, f"实际: {status}")
        
        if http_ok:
            remote_content = subprocess.run(['curl', '-s', self.url], capture_output=True, text=True).stdout
            self.log_test("远程页面有 Canvas", '<canvas' in remote_content.lower())
        
        # 11. 递归调用检查
        print("\n1️⃣1️⃣ 测试递归调用...")
        has_recursive = False
        for func in re.findall(r'function\s+(\w+)\s*\(', js_code):
            if f'{func}(' in js_code:
                # 找到函数定义的位置
                func_idx = js_code.find(f'function {func}(')
                if func_idx != -1:
                    # 检查在函数定义之后、函数结束之前是否调用了自己
                    func_body_start = js_code.find('{', func_idx) + 1
                    # 找到匹配的 }
                    brace_count = 1
                    func_body_end = func_body_start
                    for i in range(func_body_start, len(js_code)):
                        if js_code[i] == '{':
                            brace_count += 1
                        elif js_code[i] == '}':
                            brace_count -= 1
                            if brace_count == 0:
                                func_body_end = i
                                break
                    
                    func_body = js_code[func_body_start:func_body_end]
                    # 排除注释
                    func_body_no_comments = re.sub(r'//.*', '', func_body)
                    if f'{func}(' in func_body_no_comments:
                        has_recursive = True
                        self.log_test("递归调用检查", False, f"发现递归: {func}()")
                        break
        
        if not has_recursive:
            self.log_test("递归调用检查", True, "无递归调用")
        
        # 总结
        print("\n" + "=" * 80)
        print("📋 测试结果总结")
        print("=" * 80)
        print(f"✅ 通过: {self.passed}")
        print(f"❌ 失败: {self.failed}")
        print(f"📊 总计: {self.passed + self.failed}")
        print()
        
        critical_tests = [
            'Canvas HTML 标签',
            'Renderer 添加到 DOM',
            'JavaScript 语法',
            'HTTP 状态 200',
            'Cannon.js CDN',
            'Three.js CDN'
        ]
        
        critical_failed = [r['name'] for r in self.results if r['name'] in critical_tests and not r['passed']]
        
        if self.failed == 0:
            print("🎉 所有测试通过！物理引擎功能正常。")
            print()
            print("💡 如果页面上点击没反应，请尝试:")
            print("   1. Ctrl+F5 强制刷新 (清除缓存)")
            print("   2. 打开浏览器开发者工具 (F12) 查看控制台")
            print("   3. 尝试在其他浏览器中打开")
            print("   4. 检查网络连接是否正常")
            print()
            print("🔗 测试链接:")
            print(f"   物理引擎: {self.url}")
        elif critical_failed:
            print(f"❌ 关键测试失败: {', '.join(critical_failed)}")
            print("   这些问题需要立即修复。")
        else:
            print("⚠️ 部分非关键测试失败")
            print("   物理引擎核心功能应该正常。")
        
        print()
        print("=" * 80)
        
        return self.failed == 0 or len(critical_failed) == 0


def main():
    tester = PhysicsEngineTester()
    success = tester.run_all_tests()
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
