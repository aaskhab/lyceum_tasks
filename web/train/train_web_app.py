from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/list_prof/<param>')
def training(param):
    return render_template('profession.html', param=param)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)