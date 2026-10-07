from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

@app.route('/usuario', methods=['GET'])
def buscar_usuario():
    usuario = {
        "nome": "Usuario",
        "idade": 40,
        "telefone": "(19) 988446677"
    }

    return usuario

@app.route('/produto', methods=['POST'])
def cadastrar_produto():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    print(f"Novo produto: {dados}")

    return jsonify({"Menssage": "Produto Salvo com sucesso!",
                    "Produto_cadastrado": dados}), 201


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

if __name__ == '__main__':
    app.run(debug=True)