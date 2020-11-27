from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/login')
def login():
    user_name = request.args.get('user_name')
    print(user_name)

@app.route('/html_test')
def html_test():
    user_name = request.args.get('user_name')
    print(user_name)
    return render_template('login_rawtest.html')

if __name__ == "__main__" :
    app.run(host="127.0.0.1", port=8080)