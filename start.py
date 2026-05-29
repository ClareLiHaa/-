
import os
import subprocess
import sys
import io

# 设置输出编码
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# 设置环境变量
os.environ['PATH'] = r'E:\Node.js;' + os.environ['PATH']
os.chdir(r'e:\系统分析与设计')

print('=' * 50)
print('   CampusVibe - Campus Buddy AI')
print('=' * 50)
print()

# 检查 node
try:
    result = subprocess.run(['node', '--version'], capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(f'Node.js version: {result.stdout.strip()}')
except Exception as e:
    print(f'Cannot find Node.js: {e}')
    sys.exit(1)

print()
print('Starting development server...')
print('URL: http://localhost:3000')
print()
print('Press Ctrl+C to stop server')
print('-' * 50)
print()

try:
    # 运行 npm run dev
    subprocess.run(['npm', 'run', 'dev'])
except KeyboardInterrupt:
    print()
    print('Server stopped')
except Exception as e:
    print(f'Error: {e}')
