from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/despesa', methods=['POST', 'GET'])
def despesas():
    return render_template('despesa.html')

app.run(debug=True) 



