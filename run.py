#!/usr/bin/env python3
"""
Script de inicialização do Projeto Museu do Aeroclube do Paraná
"""

import subprocess
import sys
import os

def install_dependencies():
    """Instala as dependências do projeto"""
    print("📦 Instalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
    except subprocess.CalledProcessError:
        print("❌ Erro ao instalar dependências")
        return False
    return True

def clean_database():
    """Remove bancos de dados antigos para recriação"""
    db_paths = [
        "instance/museu.db",
        "src/backend/instance/museu.db",
        "museu.db"
    ]
    
    for db_path in db_paths:
        if os.path.exists(db_path):
            try:
                os.remove(db_path)
                print(f"🗑️  Removido banco antigo: {db_path}")
            except PermissionError:
                print(f"⚠️  Não foi possível remover: {db_path}")

def run_application():
    """Executa a aplicação Flask"""
    print("🚀 Iniciando aplicação...")
    print("📝 Acesso admin: http://localhost:5000/admin/login")
    print("👤 Usuário: admin | Senha: admin")
    print("🌐 Site público: http://localhost:5000")
    print("📋 API do acervo: http://localhost:5000/api/acervo")
    print("-" * 50)
    
    # Muda para o diretório do backend
    backend_dir = os.path.join("src", "backend")
    if not os.path.exists(backend_dir):
        print("❌ Diretório backend não encontrado!")
        return
    
    original_dir = os.getcwd()
    os.chdir(backend_dir)
    
    try:
        subprocess.call([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n🛑 Aplicação encerrada pelo usuário")
    finally:
        os.chdir(original_dir)

if __name__ == "__main__":
    print("🏛️  Projeto Museu do Aeroclube do Paraná")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--install":
            if install_dependencies():
                print("\n✅ Projeto configurado com sucesso!")
                print("Execute 'python run.py' para iniciar a aplicação")
        elif sys.argv[1] == "--reset":
            print("🔄 Resetando banco de dados...")
            clean_database()
            print("✅ Banco limpo! Execute 'python run.py' para recriar.")
        else:
            print("Uso: python run.py [--install|--reset]")
    else:
        run_application()