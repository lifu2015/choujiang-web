# TechVision Solutions Web版员工抽奖系统使用指南

这是一个基于Web的员工抽奖系统（BS架构），支持多人同时在线观看抽奖过程，采用服务器端随机源，确保抽奖的公平性和透明度。

## 系统架构

- 后端：Python Flask
- 前端：Vue.js + Bootstrap
- 数据存储：JSON文件
- 部署方式：支持本地服务器或云服务器部署

## 系统要求

### 服务器端要求
- Python 3.8 或更高版本
- 4GB 或以上内存
- 支持 Windows/Linux/MacOS

### 客户端要求
- 现代浏览器（Chrome 90+、Firefox 90+、Edge 90+）
- 最小屏幕分辨率：1366x768
- 稳定的网络连接

## 部署指南

### 1. 本地开发环境部署

1. **安装 Python 环境**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **启动服务**
   ```bash
   cd src
   python app.py
   ```

### 2. 生产环境部署

1. **使用 gunicorn（Linux/MacOS）**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **使用 Nginx 反向代理（推荐）**
   ```nginx
   server {
       listen 80;
       server_name lottery.your-domain.com;

       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

## 系统配置

### 1. 员工信息配置 (employees.json)
```json
{
    "employees": [
        {
            "name": "张三",
            "age": 28,
            "position": "软件工程师",
            "department": "研发部",
            "level": "P5",
            "years": 3,
            "skills": ["Python", "Java"],
            "performance": "A"
        }
    ]
}
```

### 2. 奖项规则配置 (prize_rules.json)
```json
{
    "prizes": [
        {
            "level": "特等奖",
            "winners": 1
        },
        {
            "level": "一等奖",
            "winners": 2
        }
    ]
}
```

### 3. 奖品信息配置 (prize_items.json)
```json
{
    "prizes": [
        {
            "level": "特等奖",
            "item": {
                "name": "iPhone 15 Pro",
                "description": "最新款苹果手机",
                "image": "iphone15.jpg"
            }
        }
    ]
}
```

## 使用说明

### 管理员操作指南

1. **系统启动**
   - 确保服务器正常运行
   - 检查配置文件完整性
   - 确认网络端口开放

2. **抽奖前准备**
   - 检查员工名单是否最新
   - 确认奖品信息正确
   - 测试网络连接稳定性

3. **抽奖操作**
   - 访问抽奖系统网址
   - 选择随机算法
   - 点击"开始抽奖"按钮
   - 保存抽奖结果

### 用户访问指南

1. **访问系统**
   - 打开浏览器
   - 输入抽奖系统网址
   - 等待页面加载完成

2. **查看抽奖过程**
   - 实时显示当前奖项
   - 显示获奖者信息
   - 查看剩余抽奖名额

## 界面说明

1. **顶部区域**
   - 系统标题
   - 当前奖项信息
   - 剩余抽奖人数

2. **中央区域**
   - 奖品图片展示
   - 获奖者信息显示

3. **控制区域**
   - 随机算法选择
   - 操作按钮
   - 结果显示面板

## 特色功能

1. **多重随机算法**
   - 密码学安全随机（最高安全性）
   - 简单随机（快速抽取）
   - 混合熵源随机（平衡方案）

2. **实时结果展示**
   - 动态更新获奖信息
   - 自动保存抽奖记录
   - 支持结果导出

3. **多人同步观看**
   - 所有客户端同步显示
   - 实时更新抽奖状态
   - 支持大屏幕投影

## 注意事项

1. **系统维护**
   - 定期备份配置文件
   - 检查日志信息
   - 及时更新系统

2. **数据安全**
   - 定期更改管理密码
   - 控制访问权限
   - 备份抽奖结果

3. **网络要求**
   - 确保网络稳定
   - 建议使用有线连接
   - 预留足够带宽

## 故障排除

1. **页面无法访问**
   - 检查服务器状态
   - 确认网络连接
   - 查看错误日志

2. **抽奖按钮无响应**
   - 刷新页面
   - 清除浏览器缓存
   - 检查 JavaScript 错误

3. **图片显示异常**
   - 确认图片文件存在
   - 检查文件权限
   - 验证文件格式

## 技术支持

如果遇到问题，请联系：
- 系统管理员：[管理员联系方式]
- 技术支持：[技术支持联系方式]
- 问题反馈：[反馈邮箱]

## 更新记录

- 2023.12.07：
  - 优化界面布局
  - 添加结果导出功能
  - 提升系统稳定性
- 2023.12.06：
  - 首次发布
  - 基础功能实现
  - 多重随机算法支持
