const bcrypt = require('bcryptjs');
const { v4: uuidv4 } = require('uuid');

const hashedPassword = bcrypt.hashSync('123456', 10);

const users = [
  { id: 'u001', username: '火锅爱好者', password: hashedPassword, mbti: 'ENFP', tags: ['美食', '旅行'] },
  { id: 'u002', username: '小辣椒', password: hashedPassword, mbti: 'ESTP', tags: ['美食', '健身'] },
  { id: 'u003', username: '吃货一枚', password: hashedPassword, mbti: 'INFP', tags: ['美食', '摄影'] },
  { id: 'u004', username: '期末战士', password: hashedPassword, mbti: 'INTJ', tags: ['学习搭子', '编程'] },
  { id: 'u005', username: '微积分杀手', password: hashedPassword, mbti: 'INTP', tags: ['学习搭子', '数学'] },
  { id: 'u006', username: '骑行侠', password: hashedPassword, mbti: 'ESTP', tags: ['骑行', '户外'] },
  { id: 'u007', username: '风一样的男子', password: hashedPassword, mbti: 'ESFP', tags: ['骑行', '摄影'] },
  { id: 'u008', username: '山地车选手', password: hashedPassword, mbti: 'ISTP', tags: ['骑行', '健身'] },
  { id: 'u009', username: '周末不宅', password: hashedPassword, mbti: 'ENFJ', tags: ['骑行', '旅行'] },
  { id: 'u010', username: '国服鲁班', password: hashedPassword, mbti: 'ENTP', tags: ['游戏', '王者'] },
  { id: 'u011', username: '打野贼6', password: hashedPassword, mbti: 'ISTJ', tags: ['游戏', '王者'] },
  { id: 'u012', username: '辅助永远的神', password: hashedPassword, mbti: 'ISFJ', tags: ['游戏', '王者'] },
  { id: 'u013', username: '快门狂魔', password: hashedPassword, mbti: 'ISFP', tags: ['摄影', '艺术'] },
  { id: 'u014', username: '富士党', password: hashedPassword, mbti: 'INFJ', tags: ['摄影', '旅行'] }
];

const activities = [
  {
    id: 'a001',
    title: '明晚南门火锅，缺2个人！',
    type: '美食',
    typeIcon: '🍲',
    description: '周五晚上去南门新开的重庆火锅店，听说毛肚特别新鲜。目前3个人，再找2个搭子，AA制大概人均60，能吃辣的优先~',
    location: '学校南门·重庆老火锅',
    time: '2026-05-30 19:00',
    maxPeople: 5,
    joinedCount: 3,
    creatorId: 'u001',
    tags: ['火锅', 'AA制', '南门'],
    coverGradient: 'linear-gradient(135deg, #FF6B6B 0%, #EE5A24 100%)',
    createdAt: new Date().toISOString(),
    participants: ['u001', 'u002', 'u003'],
    comments: [
      { id: 'cmt1', username: '火锅爱好者', text: '终于等到火锅局了！', aiGenerated: false, time: Date.now() - 7200000 },
      { id: 'cmt2', username: '小辣椒', text: '能吃辣的来！我带特辣底料', aiGenerated: false, time: Date.now() - 3600000 }
    ]
  },
  {
    id: 'a002',
    title: '期末复习局——图书馆自习搭子',
    type: '学习',
    typeIcon: '📚',
    description: '期末了，一个人复习效率太低。找2-3个同学组队去图书馆，互相监督。我高数还行可以帮忙答疑~ 每天下午2点到6点。',
    location: '图书馆三楼自习区',
    time: '2026-05-31 14:00',
    maxPeople: 4,
    joinedCount: 2,
    creatorId: 'u004',
    tags: ['图书馆', '期末复习', '高数'],
    coverGradient: 'linear-gradient(135deg, #74B9FF 0%, #0984E3 100%)',
    createdAt: new Date().toISOString(),
    participants: ['u004', 'u005'],
    comments: []
  },
  {
    id: 'a003',
    title: '周末骑行去东湖，找骑行搭子',
    type: '运动',
    typeIcon: '🚴',
    description: '周六早上8点从校门口出发，骑行到东湖绿道，全程约30公里。沿途风景超美，中午在湖边野餐。欢迎有骑行经验的同学加入！',
    location: '校门口集合→东湖绿道',
    time: '2026-06-01 08:00',
    maxPeople: 6,
    joinedCount: 4,
    creatorId: 'u006',
    tags: ['骑行', '东湖', '户外', '周末'],
    coverGradient: 'linear-gradient(135deg, #00B894 0%, #00CEC9 100%)',
    createdAt: new Date().toISOString(),
    participants: ['u006', 'u007', 'u008', 'u009'],
    comments: [
      { id: 'cmt3', username: '骑行侠', text: '目前4人，还可以加2个！', aiGenerated: false, time: Date.now() - 10800000 }
    ]
  },
  {
    id: 'a004',
    title: '王者开黑五排车队，来上分',
    type: '游戏',
    typeIcon: '🎮',
    description: '钻石-星耀段位，主打野和辅助，找中单和射手。每天晚上8-10点，语音连麦，心态好不骂人。上大分！',
    location: '线上·王者荣耀',
    time: '2026-06-02 20:00',
    maxPeople: 5,
    joinedCount: 3,
    creatorId: 'u010',
    tags: ['王者荣耀', '开黑', '语音'],
    coverGradient: 'linear-gradient(135deg, #A29BFE 0%, #6C5CE7 100%)',
    createdAt: new Date().toISOString(),
    participants: ['u010', 'u011', 'u012'],
    comments: []
  },
  {
    id: 'a005',
    title: '摄影约拍——校园初夏主题',
    type: '摄影',
    typeIcon: '📷',
    description: '校园里的蔷薇花开了，想找几个喜欢摄影的同学一起约拍。可以互拍，也可以一起交流摄影技巧。后期可以一起修图~',
    location: '校园蔷薇花廊',
    time: '2026-06-03 15:00',
    maxPeople: 5,
    joinedCount: 2,
    creatorId: 'u013',
    tags: ['摄影', '约拍', '蔷薇', '初夏'],
    coverGradient: 'linear-gradient(135deg, #FDCB6E 0%, #E17055 100%)',
    createdAt: new Date().toISOString(),
    participants: ['u013', 'u014'],
    comments: []
  }
];

const chats = [];
const messages = [];

module.exports = {
  users,
  activities,
  chats,
  messages,
  getUserById: (id) => users.find(u => u.id === id),
  getUserByUsername: (username) => users.find(u => u.username === username),
  addUser: (user) => { users.push(user); return user; },
  getActivityById: (id) => activities.find(a => a.id === id),
  addActivity: (activity) => { activities.unshift(activity); return activity; },
  getChatsByUserId: (userId) => chats.filter(c => c.participants.includes(userId)),
  getChatById: (id) => chats.find(c => c.id === id),
  addChat: (chat) => { chats.push(chat); return chat; },
  getMessagesByChatId: (chatId) => messages.filter(m => m.chatId === chatId),
  addMessage: (msg) => { messages.push(msg); return msg; }
};
