from flask import Flask, render_template
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

@app.route('/restar/<int:s1>/<int:s2>',methods=['GET'])
def resta(s1,s2):
    return str(s1-s2)

@app.route('/multiplicar/<int:s1>/<int:s2>',methods=['GET'])
def multiplica(s1,s2):
    return str(s1*s2)


if __name__ == '__main__':
    app.run()
