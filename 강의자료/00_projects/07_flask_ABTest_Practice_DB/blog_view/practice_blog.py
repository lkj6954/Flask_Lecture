from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for

practice_blog_abtest = Blueprint('practice_blog', __name__)

@practice_blog_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        # print('set_email', request.headers)
        print('set_email', request.args.get('user_email'))
        return redirect(url_for('practice_blog.test_blog'))
    else:
        # print('set_email', request.headers)
        # content type 이 application/json 인 경우
        # print('set_email', request.get_json())
        print('set_email', request.form['user_email'])

        return redirect(url_for('practice_blog.test_blog'))

    # return redirect('/blog/test_blog')
    # return make_response(jsonify(success=True), 200)


@practice_blog_abtest.route('/test_blog')
def test_blog():
    return render_template('practice_blog_A.html')
