
import os
import subprocess
import sys

# 设置环境
os.chdir(r'e:\系统分析与设计')

# 完整路径
node = r'E:\Node.js\node.exe'
npm_cli = r'E:\Node.js\node_modules\npm\bin\npm-cli.js'

print('Installing dependencies...')
print('This may take a few minutes...')
print()

# 运行 npm install
try:
    result = subprocess.run(
        [node, npm_cli, 'install'],
        check=True
    )
    print()
    print('Dependencies installed successfully!')
except subprocess.CalledProcessError as e:
    print(f'Error installing dependencies: {e}')
    sys.exit(1)
