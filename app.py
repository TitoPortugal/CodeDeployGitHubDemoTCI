from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/suma/<int:s1>/<int:s2>',methods=['GET'])
def suma(s1,s2):
    return str(s1+s2)

@app.route('/dividir/<int:s1>/<int:s2>',methods=['GET'])
def divide(s1,s2):
    return str(s1/s2)

<<<<<<< HEAD
@app.route('/restar/<int:s1>/<int:s2>',methods=['GET'])
=======
@app.route('/resta/<int:s1>/<int:s2>',methods=['GET'])
>>>>>>> f26ce908271924bd969e70a4e72dd9aaf6068b74
def resta(s1,s2):
    return str(s1-s2)

@app.route('/multiplicar/<int:s1>/<int:s2>',methods=['GET'])
def multiplica(s1,s2):
    return str(s1*s2)

@app.route('/raiz/<int:s1>',methods=['GET'])
def raiz(s1):
    return str(math.sqrt(s1))

if __name__ == '__main__':
    app.run()
