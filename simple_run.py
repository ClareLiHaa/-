
import os
import subprocess
import sys

# 设置编码
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

os.chdir(r'e:\系统分析与设计')

node = r'E:\Node.js\node.exe'
npm = r'E:\Node.js\npm.cmd'

print('=== 步骤 1: 检查 Node.js ===')
result = subprocess.run([node, '--version'], capture_output=True, text=True)
print(f'Node.js 版本: {result.stdout.strip()}')

print('\n=== 步骤 2: 检查 npm ===')
result = subprocess.run([node, npm, '--version'], capture_output=True, text=True)
print(f'npm 版本: {result.stdout.strip()}')

print('\n=== 步骤 3: 安装依赖 ===')
if not os.path.exists('node_modules'):
    print('正在安装 node_modules...')
    result = subprocess.run([node, npm, 'install'])
    print(f'安装结果: {result.returncode}')
else:
    print('node_modules 已存在')

print('\n=== 步骤 4: 启动开发服务器 ===')
print('服务器将在 http://localhost:3000 启动')
print('按 Ctrl+C 停止服务器')
print('-' * 50)

try:
    subprocess.run([node, npm, 'run', 'dev'])
except KeyboardInterrupt:
    print('\n服务器已停止')
