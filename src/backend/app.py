import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

# Inicialização do app Flask
app = Flask(__name__, static_folder='../frontend', static_url_path='/static')
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'  # Troque por uma chave segura em produção
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///museu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), '../../assets/images/acervo_imagens')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB máximo

CORS(app, supports_credentials=True)

from models import db

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'admin.login'  # Nome da rota de login do admin

# Importa e registra blueprint do admin APÓS o db.init_app(app)
from admin.admin import admin_bp
app.register_blueprint(admin_bp, url_prefix='/admin')

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/api/acervo')
def api_acervo():
    from models import ItemAcervo, Categoria
    itens = ItemAcervo.query.all()
    itens_json = [
        {
            'id': item.id,
            'nome': item.nome,
            'descricao': item.descricao,
            'categoria': item.categoria.nome if item.categoria else None,
            'imagem': item.imagem if hasattr(item, 'imagem') else None
        }
        for item in itens
    ]
    return jsonify({'itens': itens_json})

@app.route('/api/contato', methods=['POST'])
def api_contato():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'status': 'error', 'message': 'Dados não fornecidos'}), 400
        
        nome = data.get('nome', '').strip()
        email = data.get('email', '').strip()
        mensagem = data.get('mensagem', '').strip()
        
        # Validações
        if not nome or len(nome) < 2:
            return jsonify({'status': 'error', 'message': 'Nome deve ter pelo menos 2 caracteres'}), 400
        
        if not email or '@' not in email:
            return jsonify({'status': 'error', 'message': 'Email inválido'}), 400
        
        if not mensagem or len(mensagem) < 10:
            return jsonify({'status': 'error', 'message': 'Mensagem deve ter pelo menos 10 caracteres'}), 400
        
        # Aqui você pode implementar o envio de email ou salvar no banco
        # Por enquanto, apenas retornamos sucesso
        return jsonify({'status': 'success', 'message': 'Mensagem enviada com sucesso!'})
    
    except Exception as e:
        app.logger.error(f'Erro no formulário de contato: {str(e)}')
        return jsonify({'status': 'error', 'message': 'Erro interno do servidor'}), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/admin')
def admin_home():
    return render_template('admin_template.html')

@app.route('/admin/acervo')
@login_required
def listar_acervo():
    from models import ItemAcervo
    itens = ItemAcervo.query.all()
    return render_template('acervo_list.html', itens=itens)

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/admin/acervo/novo', methods=['GET', 'POST'])
@login_required
def novo_item():
    from models import Categoria, ItemAcervo
    categorias = Categoria.query.all()
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        categoria_id = request.form.get('categoria_id')
        
        imagem_filename = None
        if 'imagem' in request.files:
            file = request.files['imagem']
            if file and file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Garante nome único
                import uuid
                filename = f"{uuid.uuid4().hex}_{filename}"
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                imagem_filename = filename
        
        item = ItemAcervo(nome=nome, descricao=descricao, categoria_id=categoria_id, imagem=imagem_filename)
        db.session.add(item)
        db.session.commit()
        flash('Item cadastrado com sucesso!', 'success')
        return redirect(url_for('listar_acervo'))
    return render_template('acervo_form.html', categorias=categorias, item=None)

@app.route('/admin/acervo/editar/<int:item_id>', methods=['GET', 'POST'])
@login_required
def editar_item(item_id):
    from models import Categoria, ItemAcervo
    item = ItemAcervo.query.get_or_404(item_id)
    categorias = Categoria.query.all()
    if request.method == 'POST':
        item.nome = request.form['nome']
        item.descricao = request.form['descricao']
        item.categoria_id = request.form.get('categoria_id')
        
        # Lidar com upload de nova imagem
        if 'imagem' in request.files:
            file = request.files['imagem']
            if file and file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                import uuid
                filename = f"{uuid.uuid4().hex}_{filename}"
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # Remove imagem anterior se existir
                if item.imagem:
                    old_path = os.path.join(app.config['UPLOAD_FOLDER'], item.imagem)
                    if os.path.exists(old_path):
                        os.remove(old_path)
                item.imagem = filename
        
        db.session.commit()
        flash('Item atualizado com sucesso!', 'success')
        return redirect(url_for('listar_acervo'))
    return render_template('acervo_form.html', categorias=categorias, item=item)

@app.route('/admin/acervo/excluir/<int:item_id>', methods=['POST'])
@login_required
def excluir_item(item_id):
    from models import ItemAcervo
    item = ItemAcervo.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item excluído com sucesso!', 'success')
    return redirect(url_for('listar_acervo'))

@app.route('/admin/api/acervo')
@login_required
def api_listar_acervo():
    from models import ItemAcervo, Categoria
    itens = ItemAcervo.query.all()
    itens_json = [
        {
            'id': item.id,
            'nome': item.nome,
            'descricao': item.descricao,
            'categoria': item.categoria.nome if item.categoria else None
        }
        for item in itens
    ]
    return {'itens': itens_json}

if __name__ == '__main__':
    with app.app_context():
        from models import User, Categoria
        db.create_all()
        
        # Criar usuário admin se não existir
        if not User.query.filter_by(username='admin').first():
            admin_user = User(username='admin', is_admin=True)
            admin_user.set_password('admin')
            db.session.add(admin_user)
            db.session.commit()
            print('Usuário admin criado: admin / admin')
        
        # Criar categorias padrão se não existirem
        categorias_padrao = ['Aeronaves', 'Instrumentos', 'Fotografias', 'Documentos', 'Troféus', 'Uniformes']
        for nome_categoria in categorias_padrao:
            if not Categoria.query.filter_by(nome=nome_categoria).first():
                categoria = Categoria(nome=nome_categoria)
                db.session.add(categoria)
        db.session.commit()
        print('Categorias padrão criadas')
        
    app.run(debug=True, use_reloader=True, host='0.0.0.0')
