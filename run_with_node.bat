
@echo off
setlocal

REM 设置 Node.js 路径
set "PATH=E:\Node.js;%PATH%"

REM 切换到项目目录
cd /d "e:\系统分析与设计"

REM 运行参数中指定的命令
%*

endlocal
