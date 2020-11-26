from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/login')
def login():
    id = request.args.get('id')
    pw = request.args.get('pw')
    name = request.args.get('name')
    print("<입력한 정보>\n아이디 : %s\n비밀번호 : %s\n이름 : %s" %(id,pw,name))

    if id == "rltkwpdntm" and pw == "meditation!!1" and name == "이경준" :
        return_info = {'auth' : 'success'}
    else :
        return_info = {'auth' : 'fail'}
    return jsonify(return_info)

if __name__ == "__main__" :
    app.run(host="127.0.0.1", port=8080)