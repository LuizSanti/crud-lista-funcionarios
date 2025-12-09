import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cadastro_funcionarios"
    )
    cursor = conexao.cursor()
    print("Conexão MySQL estabelecida com sucesso!")
except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")
    conexao = None
    cursor = None

@app.route('/teste')
def rota_de_teste():
    return "Funcionou! O servidor Flask está vivo."

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/cadastrar')
def form_adicionar():
    return render_template('cadastrar.html', conexao_status=conexao is not None)

@app.route('/cadastrar', methods=['POST'])
def criar_funcionario_web():
    if not conexao:
        return "Erro de conexão com o banco de dados.", 500

    nome = request.form['nome']
    cargo = request.form['cargo']
    salario = request.form['salario']
    setor = request.form['setor']
    telefone = request.form['telefone']
    email = request.form['email']
    data_admissao = request.form['data_admissao']

    try:
        sql = "INSERT INTO funcionarios (nome, cargo, salario, setor, telefone, email, data_admissao) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (nome, cargo, salario, setor, telefone, email, data_admissao)
        
        cursor.execute(sql, valores)
        conexao.commit()
        
        return redirect(url_for('listar_funcionarios_web')) 

    except mysql.connector.Error as err:
        return f"Erro ao inserir funcionário: {err}", 500 
    

@app.route('/listar')
def listar_funcionarios_web():
    if not conexao:
        return "Erro de conexão com o banco de dados.", 500

    try:
        cursor.execute("SELECT * FROM funcionarios")
        funcionarios = cursor.fetchall()  
        
        return render_template('listar.html', lista=funcionarios)

    except mysql.connector.Error as err:
        return f"Erro ao listar funcionários: {err}", 500
    

@app.route('/consultar/<int:funcionario_id>') 
def consultar_funcionario_web(funcionario_id): 
    if not conexao:
        return "Erro de conexão com banco de dados", 500

    try:
        sql = "SELECT * FROM funcionarios WHERE id = %s"
        
        cursor.execute(sql, (funcionario_id,)) 
        
        funcionario = cursor.fetchone() 

        return render_template('consultar.html', funcionario=funcionario) 

    except mysql.connector.Error as err:
        return f"Erro ao listar funcionário: {err}", 500
    
@app.route('/deletar/<int:funcionario_id>', methods = ['GET' ,'POST'])
def deletar_funcionario_web(funcionario_id):
    if not conexao:
        return "Erro de conexão com banco de dados", 500
    
    try:
        sql = "DELETE FROM funcionarios WHERE id = %s"
        cursor.execute(sql, (funcionario_id,))
        conexao.commit()

        return redirect(url_for('listar_funcionarios_web'))
    except mysql.connector.Error as err:
        return f"Erro ao deletar funcionário {err}", 500
    
@app.route('/editar/<int:funcionario_id>')
def editar_funcionario_web(funcionario_id):
    if not conexao:
        return "Erro de conexão com banco de dados", 500
    try:
        sql = "SELECT * FROM funcionarios WHERE id = %s"
        cursor.execute(sql, (funcionario_id,))
        funcionario = cursor.fetchone()

        if not funcionario:
            return "Funcionário não encontrado", 404
        return render_template('editar.html', funcionario=funcionario)
    except mysql.connector.Error as err:
        return "Erro ao buscar funcionário para edição {err}", 500
    

@app.route('/editar/<int:funcionario_id>', methods=['POST'])
def atualizar_funcionario_web(funcionario_id):
    if not conexao:
        return "Erro de conexão com o banco de dados.", 500
    
    nome = request.form['nome']
    cargo = request.form['cargo']
    salario = request.form['salario']
    setor = request.form['setor']
    telefone = request.form['telefone']
    email = request.form['email']
    data_admissao = request.form['data_admissao']

    try:
        sql = """
            UPDATE funcionarios 
            SET nome=%s, cargo=%s, salario=%s, setor=%s, telefone=%s, email=%s, data_admissao=%s
            WHERE id=%s
        """
        valores = (nome, cargo, salario, setor, telefone, email, data_admissao, funcionario_id)
        
        cursor.execute(sql, valores)
        conexao.commit()

        return redirect(url_for('listar_funcionarios_web'))
        
    except mysql.connector.Error as err:
        return f"Erro ao atualizar funcionário: {err}", 500

if __name__ == '__main__':
    print("\nIniciando servidor Flask...")
    app.run(debug=True)