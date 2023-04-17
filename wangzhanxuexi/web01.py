from flask import Flask,render_template

app = Flask(__name__)

@app.route("/show/info")
def index():
    # return "中国大学生"
    # return "<h1>中</h1><h1>国</h1><span style='color:blue;'>大学生</span>"
    return render_template("index.html")

@app.route("/get/news")
def get_news():
    return render_template("get_news.html")

@app.route("/goods/bs")
def goods_bs():
    return render_template("goods_bs.html")

@app.route("/user/list")
def user_list():
    return render_template("user_list.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(port=5000)