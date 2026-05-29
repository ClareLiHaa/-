
import os
import subprocess
import sys

# 设置环境变量
os.environ['PATH'] = r'E:\Node.js;' + os.environ['PATH']
os.chdir(r'e:\系统分析与设计')

print('=' * 50)
print('   🎓 CampusVibe - 校园搭子AI')
print('=' * 50)
print()

# 检查 node
try:
    result = subprocess.run(['node', '--version'], capture_output=True, text=True)
    print(f'✅ Node.js 版本: {result.stdout.strip()}')
except Exception as e:
    print(f'❌ 无法找到 Node.js: {e}')
    sys.exit(1)

print()
print('🚀 正在启动开发服务器...')
print('📍 访问地址: http://localhost:3000')
print()
print('按 Ctrl+C 停止服务器')
print('-' * 50)
print()

try:
    # 运行 npm run dev
    subprocess.run(['npm', 'run', 'dev'])
except KeyboardInterrupt:
    print()
    print('👋 服务器已停止')
except Exception as e:
    print(f'❌ 错误: {e}')
