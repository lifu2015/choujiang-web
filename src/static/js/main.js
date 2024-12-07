new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],  // 避免与Flask模板语法冲突
    data: {
        rules: null,
        prizes: null,
        remainingCount: 0,
        currentPrizeIndex: 0,
        selectedAlgorithm: 'crypto',
        isDrawing: false,
        isComplete: false,
        currentWinners: [],
        allWinners: {},
        hasResults: false
    },
    computed: {
        currentPrize() {
            if (!this.rules || !this.prizes) return null;
            if (this.currentPrizeIndex >= this.rules.prizes.length) return null;
            
            const prizeConfig = this.rules.prizes[this.currentPrizeIndex];
            if (!prizeConfig) return null;
            
            const prizeInfo = this.prizes.prizes.find(p => p.level === prizeConfig.level);
            if (!prizeInfo) return null;
            
            return {
                level: prizeConfig.level,
                winners: prizeConfig.winners,
                image: prizeInfo.item.image
            };
        }
    },
    methods: {
        async initLottery() {
            try {
                const response = await axios.get('/api/init');
                this.rules = response.data.rules;
                this.prizes = response.data.prizes;
                this.remainingCount = response.data.remainingCount;
                this.currentPrizeIndex = 0;
                this.isComplete = false;
            } catch (error) {
                console.error('初始化失败:', error);
                alert('初始化失败，请刷新页面重试');
            }
        },
        async draw() {
            if (this.isDrawing || this.isComplete) return;
            
            this.isDrawing = true;
            this.currentWinners = [];
            
            try {
                const response = await axios.post('/api/draw', {
                    algorithm: this.selectedAlgorithm
                });
                
                const { level, winners, remainingCount, isComplete, currentPrizeIndex } = response.data;
                this.currentWinners = winners;
                this.allWinners[level] = winners;
                this.remainingCount = remainingCount;
                this.isComplete = isComplete;
                this.hasResults = true;
                this.currentPrizeIndex = currentPrizeIndex; // 更新当前奖项索引
                
                if (isComplete) {
                    setTimeout(() => {
                        alert('所有奖项已抽完！');
                    }, 500);
                }
            } catch (error) {
                console.error('抽奖失败:', error);
                alert('抽奖失败，请重试');
            } finally {
                this.isDrawing = false;
            }
        },
        async saveResults() {
            try {
                const response = await axios.post('/api/save', {
                    algorithm: this.selectedAlgorithm
                });
                alert(`结果已保存到文件: ${response.data.filename}`);
            } catch (error) {
                console.error('保存失败:', error);
                alert('保存失败，请重试');
            }
        },
        async reset() {
            try {
                await axios.post('/api/reset');
                this.currentPrizeIndex = 0;
                this.currentWinners = [];
                this.allWinners = {};
                this.isComplete = false;
                this.hasResults = false;
                await this.initLottery();
            } catch (error) {
                console.error('重置失败:', error);
                alert('重置失败，请刷新页面重试');
            }
        }
    },
    mounted() {
        this.initLottery();
    }
});
