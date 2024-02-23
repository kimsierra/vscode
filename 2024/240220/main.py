import flask as fk
from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def index():
    #return "Hello World"
    return render_template("index.html")

## localhost:8080/second요청시
## 아래의 함수를 호출
@app.route("/second")
def second():
    return "Second Page"



## class 내부의 함수 run() 호출 : 웹서버를 오픈
app.run(port=8080)

