from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

app = Flask(__name__) # Se crea nueva instancia de la clase Flask
bootstrap = Bootstrap(app)

app.config.update(PORT = 5000, DEBUG = False, 
    ENV = 'development', SECRET_KEY = 'SUPER SECRETO'
)
todos = ['Comprar café', 'Enviar solicitud de compra', 'Entregar video a productor']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index ():
    user_ip = request.remote_addr # IP del browser
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    # response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    # user_ip = request.cookies.get('user_ip')
    # return 'Hello World Flask, tu IP es {}'.format(user_ip)
    context = {
        'user_ip' : user_ip, 
        'todos' : todos,
    }
    return render_template('hello.html', **context)

if __name__ == '__main__': # Para correr el servido r flask con debug
    app.run()