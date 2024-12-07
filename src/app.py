"""
Web版抽奖程序主文件
实现抽奖API和页面路由
"""
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
import os
from algorithms.crypto_random import CryptoRandomDraw
from algorithms.simple_random import SimpleRandomDraw
from algorithms.entropy_random import EntropyRandomDraw
from datetime import datetime

app = Flask(__name__)
CORS(app)

# 全局变量存储抽奖状态
current_prize_index = 0
winners = {}
available_employees = []

def load_configs():
    """加载配置文件"""
    global available_employees
    
    # 加载员工信息
    with open('employees.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        available_employees = data['employees']
    
    # 加载奖项规则
    with open('prize_rules.json', 'r', encoding='utf-8') as f:
        rules = json.load(f)
    
    # 加载奖品信息
    with open('prize_items.json', 'r', encoding='utf-8') as f:
        prizes = json.load(f)
        
    return rules, prizes

def get_drawer(algo_type):
    """根据选择返回对应的抽奖器"""
    if algo_type == "crypto":
        return CryptoRandomDraw()
    elif algo_type == "simple":
        return SimpleRandomDraw()
    else:
        return EntropyRandomDraw()

@app.route('/')
def index():
    """渲染主页"""
    return render_template('index.html')

@app.route('/api/init', methods=['GET'])
def init_lottery():
    """初始化抽奖数据"""
    rules, prizes = load_configs()
    return jsonify({
        'rules': rules,
        'prizes': prizes,
        'remainingCount': len(available_employees)
    })

@app.route('/api/draw', methods=['POST'])
def draw():
    """执行抽奖"""
    global current_prize_index, winners, available_employees
    
    data = request.get_json()
    algo_type = data.get('algorithm', 'crypto')
    
    # 加载规则
    rules, _ = load_configs()
    prize_configs = rules['prizes']
    
    if current_prize_index >= len(prize_configs):
        return jsonify({'error': '所有奖项已抽完！'}), 400
    
    # 获取当前奖项
    current_prize = prize_configs[current_prize_index]
    level = current_prize['level']
    num_winners = current_prize['winners']
    
    # 获取抽奖器
    drawer = get_drawer(algo_type)
    drawer.available_employees = available_employees
    
    # 执行抽奖
    level_winners = []
    if num_winners == "remaining":
        # 鼓励奖：所有剩余员工
        level_winners = available_employees
        available_employees = []
    else:
        # 抽取指定数量的获奖者
        for _ in range(num_winners):
            if available_employees:
                winner = drawer.entropy_choice(available_employees)
                level_winners.append(winner)
                available_employees.remove(winner)
    
    # 保存结果
    winners[level] = level_winners
    current_prize_index += 1
    
    return jsonify({
        'level': level,
        'winners': level_winners,
        'remainingCount': len(available_employees),
        'isComplete': current_prize_index >= len(prize_configs),
        'currentPrizeIndex': current_prize_index
    })

@app.route('/api/save', methods=['POST'])
def save_results():
    """保存抽奖结果"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'results/lottery_result_{timestamp}.json'
    
    # 确保结果目录存在
    os.makedirs('results', exist_ok=True)
    
    # 准备保存的数据
    result_data = {
        'timestamp': datetime.now().isoformat(),
        'algorithm': request.json.get('algorithm', 'crypto'),
        'winners': winners
    }
    
    # 保存文件
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result_data, f, ensure_ascii=False, indent=4)
    
    return jsonify({'success': True, 'filename': filename})

@app.route('/api/reset', methods=['POST'])
def reset():
    """重置抽奖状态"""
    global current_prize_index, winners, available_employees
    current_prize_index = 0
    winners = {}
    load_configs()  # 重新加载员工数据
    return jsonify({'success': True})

if __name__ == '__main__':
    # 初始化数据
    load_configs()
    # 启动应用
    app.run(debug=True, host='0.0.0.0', port=5000)
