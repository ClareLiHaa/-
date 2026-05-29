
import os
import subprocess
import time

os.chdir(r'e:\系统分析与设计')

node_exe = r'E:\Node.js\node.exe'
vite_bin = r'e:\系统分析与设计\node_modules\vite\bin\vite.js'

print('正在启动 Vite 开发服务器...')
print('服务器地址: http://localhost:3000')
print('-' * 50)

try:
    # 直接使用 node 运行 vite
    process = subprocess.Popen(
        [node_exe, vite_bin],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    
    # 等待一会儿让服务器启动
    time.sleep(3)
    
    # 检查服务器是否正在运行
    if process.poll() is None:
        print('\n✅ 开发服务器已成功启动！')
        print('📍 请在浏览器中访问: http://localhost:3000')
        print('\n📝 服务器正在后台运行中...')
        
        # 保持进程运行
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print('\n\n正在停止服务器...')
            process.terminate()
            process.wait()
            print('服务器已停止')
    else:
        print('服务器启动失败')
        output = process.stdout.read()
        print(output)
        
except Exception as e:
    print(f'错误: {e}')
