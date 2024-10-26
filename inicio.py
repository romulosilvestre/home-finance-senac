from flask import Flask,render_template,request,redirect,url_for
import urllib.parse
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from level import Level
app = Flask(__name__)
app.secret_key = 'seu_segredo_aqui'  # Necessário para usar flash messages

# informações do  banco

user = 'root'
password = urllib.parse.quote_plus('senac')
host = 'localhost'
database = 'homefinance'

# connection string

connection_string = f'mysql+pymysql://{user}:{password}@{host}/{database}'

# função create_engine

engine = create_engine(connection_string)

#  Refletindo o Banco de Dados

metadata = MetaData()
metadata.reflect(engine)

# mapeando 
Base = automap_base(metadata=metadata) 
Base.prepare()

# ligando as classes
# Ligando com a classe
Level =  Base.classes.level

# Criar a sessão do SQLAlchemy
Session = sessionmaker(bind=engine)

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

@app.route('/showlevel')
def show_level():
    return render_template('level.html')

@app.route('/addlevel', methods=['POST','GET'])
def insert_level():
    session_db = Session()  # Criar uma nova sessão
    name_level = request.form['name_level']
    level = Level(name_level=name_level) 
    try:
        session_db.add(level)
        session_db.commit()
    except:
        session_db.rollback()
    finally:
        session_db.close()
    return redirect(url_for('show_level'))


app.run(debug=True) 



