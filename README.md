# Web版员工抽奖系统

这是一个基于Web的员工抽奖系统，采用BS架构，支持多人同时在线查看抽奖过程。

## 技术栈

- 后端：Flask (Python)
- 前端：Vue.js + Bootstrap
- 随机算法：支持三种随机算法
  - 密码学安全随机（推荐）
  - 简单随机
  - 混合熵源随机

## 系统要求

- Python 3.8+
- 现代浏览器（Chrome、Firefox、Edge等）

## 安装步骤

1. 创建虚拟环境（推荐）：
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行应用：
```bash
cd src
python app.py
```

4. 访问系统：
打开浏览器访问 http://localhost:5000

## 部署说明

1. 在生产环境中，建议使用 gunicorn 作为 WSGI 服务器：
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

2. 为了更好的安全性，建议：
   - 配置反向代理（如 Nginx）
   - 启用 HTTPS
   - 添加访问控制

## 文件结构

```
choujiang-web/
├── requirements.txt    # 项目依赖
├── src/               # 源代码目录
│   ├── app.py        # Flask应用主文件
│   ├── algorithms/   # 随机算法实现
│   ├── static/       # 静态文件
│   │   ├── css/     # 样式文件
│   │   ├── js/      # JavaScript文件
│   │   ├── goods/   # 奖品图片
│   │   └── photo/   # 员工照片
│   └── templates/    # HTML模板
├── employees.json    # 员工数据
├── prize_rules.json  # 奖项规则
└── prize_items.json  # 奖品信息
```

## 功能特点

1. 支持三种随机算法，可根据需要切换
2. 实时显示抽奖过程和结果
3. 支持保存抽奖结果
4. 可随时重置抽奖
5. 响应式设计，支持各种设备访问
6. 使用服务器端随机源，提供更好的随机性

## 注意事项

1. 首次运行前确保 `goods` 和 `photo` 目录中有相应的图片文件
2. 确保 `results` 目录存在且有写入权限
3. 生产环境部署时建议配置日志记录
4. 建议定期备份抽奖结果
