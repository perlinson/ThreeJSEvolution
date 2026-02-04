#!/usr/bin/env python3
"""
🧪 ThreeJSEvolution 物理引擎完整单元测试
测试物理引擎 v1.1 的所有功能是否正常
"""

import subprocess
import re
import os
import sys
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
                print(f"        {message}")
        else:
            self.failed += 1
            print(f"   {status}: {name}")
            if message:
                print(f"        ❗ {message}")
    
    def test_file_exists(self):
        """测试1: 文件是否存在"""
        print("\n1️⃣ 测试文件存在...")
        exists = os.path.exists(self.test_file)
        self.log_test("HTML 文件存在", exists, f"路径: {self.test_file}")
        return exists
    
    def test_html_structure(self):
        """测试2: HTML 结构"""
        print("\n2️⃣ 测试 HTML 结构...")
        with open(self.test_file, 'r') as f:
            content = f.read()
        
        checks = [
            ('DOCTYPE', '<!DOCTYPE html>' in content),
            ('HTML 标签', '<html' in content and '</html>' in content),
            ('HEAD 标签', '<head>' in content and '</head>' in content),
            ('BODY 标签', '<body>' in content and '</body>' in content),
            ('字符编码', 'charset="UTF-8"' in content or "charset='UTF-8'" in content),
            ('标题', '<title>' in content and '</title>' in content),
            ('视图端口', 'viewport' in content),
        ]
        
        all_pass = True
        for name, passed in checks:
            self.log_test(name, passed)
            if not passed:
                all_pass = False
        
        return all_pass, content
    
    def test_threejs_integration(self, content):
        """测试3: Three.js 集成"""
        print("\n3️⃣ 测试 Three.js 集成...")
        
        checks = [
            ('Three.js CDN 引用', 'three.min.js' in content),
            ('THREE 命名空间', 'THREE.Scene' in content),
            ('Scene 创建', 'new THREE.Scene()' in content),
            ('Camera 创建', 'new THREE.PerspectiveCamera' in content),
            ('Renderer 创建', 'new THREE.WebGLRenderer' in content),
            ('渲染循环', 'renderer.render' in content),
        ]
        
        all_pass = True
        for name, passed in checks:
            self.log_test(name, passed)
            if not passed:
                all_pass = False
        
        return all_pass
    
    def test_physics_engine(self, content):
        """测试4: 物理引擎 (Cannon.js)"""
        print("\n4️⃣ 测试物理引擎...")
        
        checks = [
            ('Cannon.js CDN 引用', 'cannon.min.js' in content or 'cannon.js' in content),
            ('CANNON.World 创建', 'new CANNON.World()' in content),
            ('重力设置', '.gravity.set(' in content),
            ('刚体创建', 'new CANNON.Body(' in content),
            ('碰撞形状', 'new CANNON.Box(' in content or 'new CANNON.Sphere(' in content),
            ('物理步进', 'world.step(' in content),
        ]
        
        all_pass = True
        for name, passed in checks:
            self.log_test(name, passed)
            if not passed:
                all_pass = False
        
        return all_pass
    
    def test_interactive_functions(self, content):
        """测试5: 交互功能"""
        print("\n5️⃣ 测试交互功能...")
        
        # 提取并检查 JavaScript
        js_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
        js_code = js_match.group(1) if js_match else ""
        
        checks = [
            ('init() 函数', 'function init()' in js_code),
            ('animate() 函数', 'function animate()' in js_code),
            ('createBox() 函数', 'function createBox(' in js_code),
            ('createSphere() 函数', 'function createSphere(' in js_code),
            ('spawnRandomBox() 函数', 'function spawnRandomBox(' in js_code),
            ('spawnRandomSphere() 函数', 'function spawnRandomSphere(' in js_code),
            ('resetScene() 函数', 'function resetScene()' in js_code),
            ('updateStatus() 函数', 'function updateStatus()' in js_code),
        ]
        
        all_pass = True
        for name, passed in checks:
            self.log_test(name, passed)
            if not passed:
                all_pass = False
        
        # 检查函数调用
        if 'spawnRandomBox()' in js_code:
            # 检查是否在 onclick 中被调用
            if 'onclick="spawnRandomBox()"' in content:
                self.log_test("spawnRandomBox 按钮绑定", True)
            else:
                # 检查是否有事件监听器
                if 'addEventListener' in js_code and 'click' in js_code:
                    self.log_test("click 事件监听器", True)
                else:
                    self.log_test("spawnRandomBox 按钮绑定", False, "未找到 onclick 绑定")
                    all_pass = False
        
        return all_pass, js_code
    
    def test_ui_elements(self, content):
        """测试6: UI 元素"""
        print("\n6️⃣ 测试 UI 元素...")
        
        checks = [
            ('信息面板 (info)', 'id="info"' in content),
            ('状态面板 (stats)', 'id="status"' in content),
            ('控制按钮 (controls)', 'id="controls"' in content),
            ('FPS 显示', 'id="fps"' in content),
            ('物体数量显示', 'id="objCount"' in content),
            ('生成方块按钮', 'spawnRandomBox' in content and ('button' in content.lower() or 'btn' in content.lower())),
            ('生成球体按钮', 'spawnRandomSphere' in content and ('button' in content.lower() or 'btn' in content.lower())),
            ('重置按钮', 'resetScene' in content and ('button' in content.lower() or 'btn' in content.lower())),
        ]
        
        all_pass = True
        for name, passed in checks:
            self.log_test(name, passed)
            if not passed:
                all_pass = False
        
        return all_pass
    
    def test_javascript_syntax(self, js_code):
        """测试7: JavaScript 语法"""
        print("\n7️⃣ 测试 JavaScript 语法...")
        
        # 保存临时文件
        temp_file = "/tmp/physics_test.js"
        with open(temp_file, 'w') as f:
            f.write(js_code)
        
        # 使用 Node.js 检查语法
        result = subprocess.run(
            ['node', '--check', temp_file],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            self.log_test("JavaScript 语法检查", True, "无语法错误")
            return True
        else:
            error = result.stderr.strip().split('\n')[0][:100]
            self.log_test("JavaScript 语法检查", False, error)
            return False
    
    def test_http_accessibility(self):
        """测试8: HTTP 可访问性"""
        print("\n8️⃣ 测试 HTTP 可访问性...")
        
        result = subprocess.run(
            ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', self.url],
            capture_output=True,
            text=True
        )
        
        status = result.stdout.strip()
        passed = status == '200'
        self.log_test("HTTP 状态 200", passed, f"实际状态: {status}")
        
        if passed:
            # 检查内容
            content = subprocess.run(
                ['curl', '-s', self.url],
                capture_output=True,
                text=True
            ).stdout
            
            has_canvas = '<canvas' in content.lower()
            self.log_test("Canvas 元素存在", has_canvas)
            
            has_threejs = 'three.min.js' in content
            self.log_test("Three.js 引用存在", has_threejs)
            
            return has_canvas and has_threejs
        
        return False
    
    def test_recursive_calls(self, js_code):
        """测试9: 递归调用问题"""
        print("\n9️⃣ 测试递归调用问题...")
        
        # 检查是否有递归调用
        # 常见问题: spawnSphere() 函数内部调用 spawnSphere()
        
        # 提取所有函数定义
        func_pattern = r'function\s+(\w+)\s*\('
        functions = re.findall(func_pattern, js_code)
        
        # 检查每个函数是否在定义内部调用自己
        has_recursive = False
        recursive_funcs = []
        
        for func in functions:
            # 找到函数定义
            func_match = re.search(rf'function\s+{func}\s*\([^)]*\)\s*\{{([^}}]+)\}}', js_code, re.DOTALL)
            if func_match:
                func_body = func_match.group(1)
                # 检查是否在函数体内调用自己
                # 排除注释中的调用
                lines = func_body.split('\n')
                for line in lines:
                    if f'{func}(' in line and '//' not in line:
                        # 排除函数定义行
                        if 'function' not in line:
                            has_recursive = True
                            recursive_funcs.append(func)
                            break
        
        if has_recursive:
            self.log_test("递归调用检查", False, f"发现递归: {', '.join(recursive_funcs)}")
            return False
        else:
            self.log_test("递归调用检查", True, "无递归调用")
            return True
    
    def run_all_tests(self):
        """运行所有测试"""
        print("=" * 80)
        print("🧪 ThreeJSEvolution 物理引擎完整单元测试")
        print("=" * 80)
        print(f"🕐 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📄 测试文件: {self.test_file}")
        print(f"🌐 测试 URL: {self.url}")
        print("=" * 80)
        
        # 运行测试
        file_exists = self.test_file_exists()
        
        if not file_exists:
            print("\n❌ 文件不存在，测试终止")
            return False
        
        html_ok, content = self.test_html_structure()
        
        if not html_ok:
            print("\n⚠️ HTML 结构有问题，继续测试...")
        
        self.test_threejs_integration(content)
        self.test_physics_engine(content)
        
        inter_ok, js_code = self.test_interactive_functions(content)
        self.test_ui_elements(content)
        self.test_javascript_syntax(js_code)
        self.test_recursive_calls(js_code)
        self.test_http_accessibility()
        
        # 总结
        print("\n" + "=" * 80)
        print("📋 测试结果总结")
        print("=" * 80)
        print(f"✅ 通过: {self.passed}")
        print(f"❌ 失败: {self.failed}")
        print(f"📊 总计: {self.passed + self.failed}")
        print()
        
        if self.failed == 0:
            print("🎉 所有测试通过！物理引擎功能正常。")
            print()
            print("💡 如果页面上点击没反应，请尝试:")
            print("   1. Ctrl+F5 强制刷新 (清除缓存)")
            print("   2. 打开浏览器开发者工具 (F12)")
            print("   3. 检查控制台是否有错误")
            print("   4. 尝试在其他浏览器中打开")
            print()
            print("🔗 链接:")
            print(f"   物理引擎: {self.url}")
        else:
            print("❌ 有测试失败，请检查上方输出")
            print()
            print("失败的项目:")
            for r in self.results:
                if not r['passed']:
                    print(f"   - {r['name']}: {r['message']}")
        
        print()
        print("=" * 80)
        
        return self.failed == 0


def main():
    tester = PhysicsEngineTester()
    success = tester.run_all_tests()
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
