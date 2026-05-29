
@echo off
chcp 65001 &gt;nul
cd /d "e:\系统分析与设计"

echo 正在检查 Node.js...
"E:\Node.js\node.exe" --version
if errorlevel 1 (
    echo Node.js 未找到！
    pause
    exit /b 1
)

echo.
echo 正在检查 npm...
"E:\Node.js\npm.cmd" --version
if errorlevel 1 (
    echo npm 未找到！
    pause
    exit /b 1
)

echo.
if not exist "node_modules" (
    echo 正在安装依赖...
    "E:\Node.js\npm.cmd" install
    if errorlevel 1 (
        echo 依赖安装失败！
        pause
        exit /b 1
    )
) else (
    echo 依赖已安装，跳过安装步骤
)

echo.
echo 正在启动开发服务器...
echo 请在浏览器中访问 http://localhost:3000
echo.
"E:\Node.js\npm.cmd" run dev

pause
