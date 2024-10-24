from flask import Flask,flash,render_template,request,redirect,url_for

app = Flask(__name__)
app.secret_key = 'seu_segredo_aqui'  # Necessário para usar flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/despesa', methods=['POST', 'GET'])
def despesas():
    return render_template('despesa.html')

@app.route('/logar',methods=['POST','GET'])
def logar():
    login = request.form['login']
    senha = request.form['senha']
    if login == 'romulo' and senha == '123':
       return f"login:{login} e senha:{senha}"
    else:
        return 'sem sucesso'



@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/listadespesas')
def listar_despesas():
    return render_template('listadespesas.html')


@app.route('/cadastrardesp')
def cadastrar_despesa():
    pass

app.run(debug=True) 



