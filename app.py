from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Configuração do banco de dados MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'soucidadao123',
    'database': 'stockhub_db'
}

# Função para conectar ao banco de dados
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Rota para a página inicial (listagem de equipamentos)
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM equipamentos')
    equipamentos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', equipamentos=equipamentos)

# Rota para registrar um novo equipamento
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        modelo = request.form['modelo']
        numero_serie = request.form['numero_serie']
        cliente_nome = request.form['cliente_nome']
        data_instalacao = request.form['data_instalacao']

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO equipamentos (modelo, numero_serie, cliente_nome, data_instalacao) VALUES (%s, %s, %s, %s)',
                (modelo, numero_serie, cliente_nome, data_instalacao)
            )
            conn.commit()
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return "Erro ao registrar equipamento", 500
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('index'))
    return render_template('register.html')

# Rota para buscar equipamentos por número de série ou nome do cliente
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        termo = request.form['termo']
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = 'SELECT * FROM equipamentos WHERE numero_serie LIKE %s OR cliente_nome LIKE %s'
        cursor.execute(query, (f'%{termo}%', f'%{termo}%'))
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('search.html', resultados=resultados)
    return render_template('search.html', resultados=[])

if __name__ == '__main__':
    app.run(debug=True)