from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/test", methods = ['GET'])
def test():
    if request.method == "GET" :
        print('GET')
        user_email = request.args.get('email')
        print(user_email)

    return make_response(jsonify({'status': True}), 200)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8082")
