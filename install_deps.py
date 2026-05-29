
import os
import subprocess

# 设置工作目录
os.chdir(r'e:\系统分析与设计')

# npm 路径
npm_path = r'E:\Node.js\npm.cmd'

print('正在安装项目依赖...')

# 运行 npm install
process = subprocess.Popen(
    [npm_path, 'install'],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    encoding='utf-8',
    errors='replace'
)

# 实时输出
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.strip())

exit_code = process.poll()
print(f'\n安装完成，退出码: {exit_code}')
