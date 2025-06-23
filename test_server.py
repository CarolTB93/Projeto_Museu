#!/usr/bin/env python3
"""
Servidor de teste simples para o projeto Museu
"""

import os
import sys
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS

# Adiciona o diretório backend ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'backend'))

app = Flask(__name__, static_folder='src/frontend', static_url_path='')
CORS(app)

@app.route('/')
def index():
    """Serve a página principal"""
    return send_from_directory('src/frontend', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    """Serve arquivos estáticos do frontend"""
    return send_from_directory('src/frontend', filename)

@app.route('/api/acervo')
def api_acervo():
    """API de teste para o acervo"""
    itens_teste = [
        {
            'id': 1,
            'nome': 'Cessna 152',
            'descricao': 'Aeronave de treinamento básico utilizada em escolas de aviação.',
            'categoria': 'Aeronaves',
            'imagem': None
        },
        {
            'id': 2,
            'nome': 'Piper Cherokee',
            'descricao': 'Aeronave monomotor popular para treinamento avançado.',
            'categoria': 'Aeronaves',
            'imagem': None
        },
        {
            'id': 3,
            'nome': 'Altímetro Vintage',
            'descricao': 'Instrumento de medição de altitude da década de 1960.',
            'categoria': 'Instrumentos',
            'imagem': None
        }
    ]
    print(f'API /api/acervo chamada - retornando {len(itens_teste)} itens')
    return jsonify({'itens': itens_teste})

@app.route('/api/contato', methods=['POST'])
def api_contato():
    """API de teste para contato"""
    data = request.get_json()
    print(f'Contato recebido: {data}')
    return jsonify({'status': 'success', 'message': 'Mensagem enviada com sucesso!'})

if __name__ == '__main__':
    print("🧪 Servidor de Teste do Museu")
    print("=" * 40)
    print("🌐 Site: http://localhost:3000")
    print("📋 API Acervo: http://localhost:3000/api/acervo")
    print("-" * 40)
    
    app.run(debug=True, port=3000, host='0.0.0.0')