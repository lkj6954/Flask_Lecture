from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def default_page():
    return "<h1>메인 페이지 입니다용</h1>"

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>라우팅 경로 이상하다 임마</h1>", 404

@app.route("/google")
def get_google():
    response = requests.get("http://www.google.co.kr")
    return response.text

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
