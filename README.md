# CampusVibe 后端 API

## 技术栈
- Node.js + Express
- SQLite (better-sqlite3)
- bcryptjs (密码加密)

## 快速开始

### 1. 安装依赖
```bash
cd backend
npm install
```

### 2. 初始化数据库
```bash
npm run init-db
```

### 3. 启动服务器
```bash
# 开发模式（自动重启）
npm run dev

# 生产模式
npm start
```

服务器将在 http://localhost:3001 启动

## API 文档

### 用户相关
- `POST /api/users/register` - 用户注册
- `POST /api/users/login` - 用户登录
- `GET /api/users/:id` - 获取用户信息

### 活动相关
- `GET /api/activities` - 获取活动列表
- `GET /api/activities/:id` - 获取活动详情
- `POST /api/activities` - 创建活动
- `POST /api/activities/:id/join` - 参加活动
- `POST /api/activities/:id/comments` - 添加评论

### 聊天相关
- `GET /api/chats?userId=xxx` - 获取用户聊天列表
- `GET /api/chats/:id` - 获取聊天详情
- `POST /api/chats/:id/messages` - 发送消息

## 默认测试账号
所有用户密码都是: `123456`

- 火锅爱好者 (u001)
- 小辣椒 (u002)
- 吃货一枚 (u003)
- 期末战士 (u004)
- ... 等等
