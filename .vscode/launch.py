from flask import Flask, session, request
from flask import render_template
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)



@app.route('/')
def main(name=None):
    return render_template('index.html', name=name)

@app.route('/py')
def py(name=None):
    return render_template('pyindex.html', name=name)

@app.route('/java')
def java(name=None):
    return render_template('javaindex.html', name=name)

@app.route('/js')
def js(name=None):
    return render_template('jsindex.html', name=None)

@app.route('/bio')
def bio(name=None):
    return render_template('bioindex.html', name=None)

if __name__ == '__main__':
    app.run(debug=True)