from flask import Flask, render_template

app = Flask(__name__)

# 首页路由
@app.route('/')
def home():
    return render_template('index.html')

# 学术经历页路由
@app.route('/academic')
def academic():
    return render_template('academic.html')

# 实践与作品页路由
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    # debug=True 可以在你修改代码后自动重启服务器，非常适合开发阶段
    app.run(debug=True)