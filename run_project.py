
import os
import subprocess
import time

# 设置工作目录
os.chdir(r'e:\系统分析与设计')

# 路径配置
node_path = r'E:\Node.js\node.exe'
npm_path = r'E:\Node.js\npm.cmd'

print('检查 Node.js 和 npm...')
subprocess.run([node_path, '--version'], check=True)
subprocess.run([npm_path, '--version'], check=True)

print('\n检查 node_modules...')
if os.path.exists('node_modules'):
    print('node_modules 已存在，跳过安装')
else:
    print('正在安装依赖...')
    result = subprocess.run([npm_path, 'install'], capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(f'安装完成，退出码: {result.returncode}')

print('\n正在启动开发服务器...')
process = subprocess.Popen(
    [npm_path, 'run', 'dev'],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    encoding='utf-8',
    errors='replace'
)

# 等待服务器启动
time.sleep(5)

# 检查进程是否还在运行
if process.poll() is None:
    print('开发服务器已启动！')
    print('请在浏览器中访问 http://localhost:3000')
else:
    print('服务器启动失败')
    output, _ = process.communicate()
    print(output)
