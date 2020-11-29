from flask import Flask, render_template

app = Flask(__name__)
@app.route('/loop_test')
def loop_test():
    temp_list = [1,2,3]
    return render_template('practice_loop.html', values = temp_list)

@app.route('/hello_loop')
def hello_loop():
    name_list = ['Sic', 'Parvis', 'Magna']
    return render_template('practice_loop.html', values = name_list)

if __name__ == "__main__" :
    app.run(host="127.0.0.1", port=8080)