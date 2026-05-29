@echo off
echo ========================================
echo   CampusVibe 后端系统启动脚本
echo ========================================
echo.

cd backend

if not exist "node_modules" (
    echo [1/2] 安装后端依赖...
    call "E:\Node.js\npm.cmd" install
    if errorlevel 1 (
        echo ❌ 依赖安装失败！
        pause
        exit /b 1
    )
    echo ✅ 依赖安装成功！
    echo.
)

echo [2/2] 启动后端服务器...
echo.
echo 🚀 后端服务器即将启动在 http://localhost:3001
echo 💡 测试账号密码：123456
echo.
echo 按 Ctrl+C 可停止服务器
echo ========================================
echo.

call "E:\Node.js\node.exe" server.js

pause
