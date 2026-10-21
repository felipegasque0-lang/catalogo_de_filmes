from flask import Flask, jsonify, request, render_template
from psycopg2.extras import RealDictCursor

from database import criar_conexao

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

@app.route('/filme', methods=['GET'])
def listar_filme():
    conn = criar_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM filmes")
    resposta = cursor.fetchall()

    conn.close()

    return render_template("index.html", filmes=resposta)

@app.route('/filme', methods=['POST'])
def cadastrar_filme():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    print(f"Novo filme: {dados}")

    conn = criar_conexao()
    cursor = conn.cursor()

    cursor.execute(
        '''
            INSERT INTO filmes (usuario_id, titulo, ano_lancamento, 
            genero, nota, capa_url)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id; 
        ''',
        (dados['usuario_id'], dados['titulo'], dados['ano_lancamento'],
         dados['genero'], dados['nota'], dados['capa_url'])
    )

    novo_id = cursor.fetchone()[0]
    conn.commit()

    conn.close()

    return jsonify(
        {"Menssage": "Filme Salvo com sucesso!",
         "Filme_id": novo_id}
    ), 201


@app.route('/produto', methods=['PUT'])
def atualizar_produto():
    produto = {
        "id": 1,
        "nome": "Caneta azul",
        "preco": "1.5",
        "descricao": "Caneta esferográfica",
        "marca": "Bic"
    }

    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    if dados ['id'] == produto['id']:
        produto = dados

        print(f'Produto atualizado: {produto}')

        return jsonify({"message": "Produto atualizado com sucesso!"}), 201
    else:
        return jsonify({"Message": "Produto não encontrado!"}), 404

@app.route('/teste/db', methods=['GET'])
def testar_conexao():
    conn = criar_conexao()
    print('Testando conexão: ', conn)
    conn.close()
    return jsonify({"message": "Banco conectado com  sucesso!"}), 200







if __name__ == '__main__':
    app.run(debug=True)