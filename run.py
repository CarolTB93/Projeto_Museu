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

def run_application():
    """Executa a aplicação Flask"""
    print("🚀 Iniciando aplicação...")
    print("📝 Acesso admin: http://localhost:5000/admin/login")
    print("👤 Usuário: admin | Senha: admin")
    print("🌐 Site público: http://localhost:5000")
    print("-" * 50)
    
    # Muda para o diretório do backend
    backend_dir = os.path.join("src", "backend")
    os.chdir(backend_dir)
    
    try:
        subprocess.call([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n🛑 Aplicação encerrada pelo usuário")

if __name__ == "__main__":
    print("🏛️  Projeto Museu do Aeroclube do Paraná")
    print("=" * 50)
    
    if len(sys.argv) > 1 and sys.argv[1] == "--install":
        if install_dependencies():
            print("\n✅ Projeto configurado com sucesso!")
            print("Execute 'python run.py' para iniciar a aplicação")
    else:
        print("Verificando dependências...")
        run_application()