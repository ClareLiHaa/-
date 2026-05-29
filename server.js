const express = require('express');
const cors = require('cors');

const usersRouter = require('./routes/users');
const activitiesRouter = require('./routes/activities');
const chatsRouter = require('./routes/chats');

const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.json());

app.use('/api/users', usersRouter);
app.use('/api/activities', activitiesRouter);
app.use('/api/chats', chatsRouter);

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', message: 'CampusVibe API 服务正常运行' });
});

app.listen(PORT, () => {
  console.log(`🚀 CampusVibe API 服务器已启动`);
  console.log(`📍 服务地址: http://localhost:${PORT}`);
  console.log(`📊 健康检查: http://localhost:${PORT}/api/health`);
  console.log('');
  console.log('📚 API 接口:');
  console.log('  - POST /api/users/register - 用户注册');
  console.log('  - POST /api/users/login - 用户登录');
  console.log('  - GET  /api/activities - 获取活动列表');
  console.log('  - GET  /api/activities/:id - 获取活动详情');
  console.log('  - POST /api/activities - 创建活动');
  console.log('  - POST /api/activities/:id/join - 参加活动');
  console.log('  - POST /api/activities/:id/comments - 添加评论');
  console.log('  - GET  /api/chats - 获取聊天列表');
  console.log('  - GET  /api/chats/:id - 获取聊天详情');
  console.log('  - POST /api/chats/:id/messages - 发送消息');
});