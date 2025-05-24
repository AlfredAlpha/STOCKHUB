from flask import Flask, render_template, request, redirect, url_for, send_file
import mysql.connector
from datetime import datetime
import csv
import io

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'soucidadao123',
    'database': 'stockhub_db'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM equipamentos')
    equipamentos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', equipamentos=equipamentos)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        modelo = request.form['modelo']
        numero_serie = request.form['numero_serie']
        cliente_nome = request.form['cliente_nome']
        data_instalacao = request.form['data_instalacao']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO equipamentos (modelo, numero_serie, cliente_nome, data_instalacao) VALUES (%s, %s, %s, %s)',
            (modelo, numero_serie, cliente_nome, data_instalacao)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM equipamentos WHERE id = %s', (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('delete_confirm.html', id=id)

@app.route('/search', methods=['GET', 'POST'])
def search():
    resultados = []
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

@app.route('/relatorio')
def relatorio():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM equipamentos')
    equipamentos = cursor.fetchall()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Modelo', 'Número de Série', 'Cliente', 'Data de Instalação'])
    for row in equipamentos:
        writer.writerow(row)
    output.seek(0)
    cursor.close()
    conn.close()
    return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv', as_attachment=True, download_name='relatorio_equipamentos.csv')

if __name__ == '__main__':
    app.run(debug=True)