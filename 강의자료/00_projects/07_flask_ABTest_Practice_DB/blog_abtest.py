from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from blog_view import blog
import os

# https 만을 지원하는 기능을 http 에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secure_key = 'dave_server'

app.register_blueprint(blog.blog_abtest, url_prefix='/blog') #blog_view의 blog.py 파일의 blog_abtest 블루프린트 객체
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id) # Q. User 클래스는 blog_control\user_mgmt.py에 있는데 어떻게..? => 강사님이 실수. 엄밀히 말하면 여기서는 안써가지고 import 안하심.


@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=True)
