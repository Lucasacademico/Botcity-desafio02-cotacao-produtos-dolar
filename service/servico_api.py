from flask import Flask, make_response, jsonify, request, Response
import sys
import os

modulo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../', 'repository'))
sys.path.append(modulo)

import produto
from busca_dolar import search_dolar  # Adicione esta importação

# Instanciar 
app_api = Flask('api_database')
app_api.config['JSON_SORT_KEYS'] = False

# Implementar a lógica de programação

# --------------- Inicio : Serviços da api produto ---------------------
@app_api.route('/produto', methods=['POST'])
def criar_produto():
    produto_json = request.json  # corpo da requisição
    try:
        # Converte os campos necessários para o tipo correto
        produto_json['quantidade'] = float(produto_json['quantidade'])
        produto_json['preco_real'] = float(produto_json['preco_real'])
        
        # Busca o preço do dólar
        produto_json['preco_dolar'] = search_dolar()  # Chama a função para obter o preço do dólar

        id_produto = produto.criar_produto(produto_json)
        sucesso = True
        _mensagem = 'Produto inserido com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Inclusão do produto: {ex}'
        id_produto = None  # inicializa para evitar UnboundLocalError

    return make_response(
        jsonify(
            status=sucesso,
            mensagem=_mensagem,
            id=id_produto
        )
    )

# ... (mantenha as outras rotas inalteradas, exceto o método para atualizar o preço do dólar)

@app_api.route('/produto/atualizar-preco-dolar', methods=['PUT'])
def atualizar_preco_dolar():
    produto_json = request.json  # corpo da requisição
    try:
        # Busca o preço do dólar
        novo_preco_dolar = search_dolar()  # Chama a função para obter o preço do dólar
        produto_json['preco_dolar'] = novo_preco_dolar  # Atualiza o preço do dólar no JSON

        produto.atualizar_preco_dolar(produto_json)
        sucesso = True
        _mensagem = 'Preço em dólar atualizado com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Atualização do preço em dólar: {ex}'

    return make_response(
        jsonify(
            status=sucesso,
            mensagem=_mensagem
        )
    )

@app_api.route('/produto', methods=['PUT'])
def atualizar_produto():
    produto_json = request.json # corpo da requisição
    try:
        produto.atualizar_produto(produto_json)
        sucesso = True
        _mensagem = 'produto alterado com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Alteração do produto: {ex}'
    
    return make_response(
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )


@app_api.route('/produto', methods=['GET'])
def lista_produto():
    lista_produto = list()
    lista_produto = produto.lista_produto()
    if len(lista_produto) == 0:
        sucesso = False
        _mensagem = 'Lista de produto vazia'
    else:
        sucesso = True
        _mensagem = 'Lista de produto'

    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso, 
                mensagem = _mensagem,
                dados = lista_produto
        )
    )

@app_api.route('/produto/<int:id>', methods=['GET'])
def get_obter_produto_id(id):
    produto_id = list()
    produto_id = produto.obter_produto_id(id)
    if len(produto_id) == 0:
        sucesso = False
        _mensagem = 'produto nao cadastrado'
    else:
        sucesso = True
        _mensagem = 'produto cadastrado'

    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso, 
                mensagem = _mensagem,
                dados = produto_id
        )
    )

@app_api.route('/produto/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    try:
        produto.deletar_produto(id)
        sucesso = True
        _mensagem = 'produto deletado com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Exclusão de produto: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    ) 

# Levantar/Executar API REST: api_database
app_api.run()
