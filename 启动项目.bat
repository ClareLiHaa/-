
@echo off
chcp 65001 &gt;nul
title CampusVibe - 校园搭子AI

echo ========================================
echo    CampusVibe - 校园搭子AI
echo ========================================
echo.

REM 设置 Node.js 路径
set PATH=E:\Node.js;%PATH%

REM 切换到项目目录
cd /d "e:\系统分析与设计"

echo [1/3] 检查 Node.js...
node --version
if errorlevel 1 (
    echo ❌ Node.js 未找到！
    pause
    exit /b 1
)
echo ✅ Node.js 检查通过
echo.

echo [2/3] 检查项目依赖...
if not exist "node_modules" (
    echo 📦 正在安装依赖...
    call npm install
    if errorlevel 1 (
        echo ❌ 依赖安装失败！
        pause
        exit /b 1
    )
    echo ✅ 依赖安装完成
) else (
    echo ✅ 依赖已安装
)
echo.

echo [3/3] 启动开发服务器...
echo 🚀 服务器将在 http://localhost:3000 启动
echo.
echo 按 Ctrl+C 停止服务器
echo ========================================
echo.

call npm run dev

pause
