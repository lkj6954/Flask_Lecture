from flask import Blueprint

blog_ab = Blueprint('blog_ab', __name__)

@blog_ab.route('/main')
def blog_main():
    return "blog main page"