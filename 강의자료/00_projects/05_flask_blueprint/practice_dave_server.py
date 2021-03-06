from flask import Flask
from sub_blueprint import practice_blog_test

app = Flask(__name__)
app.register_blueprint(practice_blog_test.blog_ab, url_prefix='/blog_ab')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")