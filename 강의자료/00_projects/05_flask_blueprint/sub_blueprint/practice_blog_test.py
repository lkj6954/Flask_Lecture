from flask import Blueprint

blog_ab = Blueprint('blog2', __name__)

@blog_ab.route('/blog1')
def blog():
    return 'test Blueprint'