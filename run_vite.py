
import os
import subprocess
import sys

os.chdir(r'e:\系统分析与设计')

vite_cmd = r'e:\系统分析与设计\node_modules\.bin\vite.cmd'
node_path = r'E:\Node.js\node.exe'

print('🎯 正在启动 CampusVibe 开发服务器...')
print('📍 服务器地址: http://localhost:3000')
print('=' * 50)

try:
    # 使用 PowerShell 运行 vite.cmd
    process = subprocess.Popen(
        ['powershell', '-Command', f'&amp; "{vite_cmd}"'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    
    # 读取输出并显示
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
            
except KeyboardInterrupt:
    print('\n\n正在停止服务器...')
    process.terminate()
    print('服务器已停止')
except Exception as e:
    print(f'错误: {e}')
