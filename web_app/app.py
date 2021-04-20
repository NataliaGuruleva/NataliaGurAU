import flask
import m_prim
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/test')
def wilson_test():
    if request.method == 'GET':
        n=request.args.get('name')
    if n != None:
        n = int(n)
        n = m_prim.wilson_test(n)
        if n == False:
            n = 'Число составное'
        else:
            n = 'Число простое'
    return flask.render_template('test.html', name = n)

if __name__ == '__main__':
   app.run(debug = True)
