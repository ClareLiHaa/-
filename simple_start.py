
import os
import subprocess

os.chdir(r'e:\系统分析与设计')

node = r'E:\Node.js\node.exe'
vite_js = r'e:\系统分析与设计\node_modules\vite\bin\vite.js'

print('Starting Vite server...')
print('Open http://localhost:3000 in your browser')
print()

try:
    subprocess.run([node, vite_js])
except KeyboardInterrupt:
    print('\nServer stopped')
