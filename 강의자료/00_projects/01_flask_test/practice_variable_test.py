from flask import Flask, render_template

app = Flask(__name__)
@app.route('/jinja2_test/<var>')
def jinja2_test(var):
    return render_template('practice_variable.html', name1=var, name2=var)

if __name__ == "__main__" :
    app.run(host="127.0.0.1", port=8080)