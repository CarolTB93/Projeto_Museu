# Estrutura do Projeto Museu

Este repositório segue a seguinte estrutura de diretórios e arquivos:

```
├── README.md
├── src/
│   ├── frontend/
│   │   ├── index.html
│   │   ├── style.css
│   │   ├── script.js
│   │   ├── threejs-example.js
│   │   └── ...
│   ├── backend/
│   │   ├── app.py
│   │   ├── templates/
│   │   │   ├── index.html
│   │   │   ├── admin_template.html
│   │   │   └── ...
│   │   └── models.py
│   └── admin/
│       ├── admin.py
│       └── ...
├── docs/
│   ├── DiagramaFluxo.drawio
│   ├── RoteiroCronograma.docx
│   └── ...
├── assets/
│   ├── images/
│   │   ├── acervo_imagens/
│   │   ├── ...
│   └── ...
├── requirements.txt
└── .gitignore
```

# Museu do Aeroclube do Paraná - Website Project

**Version:** 1.0
**Date:** October 26, 2023

## Overview

This project aims to create a dynamic website showcasing the history of the Aeroclube do Paraná. The website will feature an
interactive virtual tour of the museum, a comprehensive catalog of the collection, and a user-friendly interface for
administration and potential visitor engagement.  This is a collaborative, interdisciplinary project for the Centro Universitário
Uniopet.

## Project Goals

*   Develop a visually appealing and informative website.
*   Create an interactive virtual tour using Three.js.
*   Build a database-driven system to manage the Aeroclube's collection.
*   Provide an administrative interface for managing the site's content.
*   Establish a foundation for future website enhancements and expansion.

## Technologies Used

*   **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS & potentially jQuery), Bootstrap
*   **Backend:** Python (Flask)
*   **Database:** SQLite
*   **Virtual Tour:** Three.js
*   **Login:** Flask-Login (Simplified Example)

## Project Structure

The project is organized into the following folders:

*   `src/`: Contains the source code for the frontend and backend.
    *   `frontend/`: HTML, CSS, and JavaScript files for the website interface.
    *   `backend/`:  Python (Flask) application files.
*   `docs/`: Documentation, diagrams, and other project-related files.
*   `assets/`: Images and other static assets.
*   `requirements.txt`: Lists all the project's Python dependencies.

## Setup and Running

### 🚀 Método Mais Fácil (Windows)

**Duplo clique no arquivo:**
```
start.bat
```

### 🚀 Método Fácil (Linux/Mac)

```bash
chmod +x start.sh
./start.sh
```

### 🔧 Método com Script Python

1.  **Instalar dependências (primeira vez):**
    ```bash
    python run.py --install
    ```

2.  **Executar aplicação:**
    ```bash
    python run.py
    ```

3.  **Reset do banco (se necessário):**
    ```bash
    python run.py --reset
    ```

### 🛠️ Método Manual

1.  **Instalar dependências:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Executar servidor Flask:**
    ```bash
    cd src/backend
    python app.py
    ```

### 🌐 Como Acessar

**⚠️ IMPORTANTE**: Sempre acesse através do servidor Flask, **NUNCA** abra o arquivo HTML diretamente no navegador!

1. **Execute um dos métodos acima**
2. **Aguarde** a mensagem: "Running on http://0.0.0.0:5000"
3. **Abra o navegador** em: **http://localhost:5000**

### 📋 URLs Disponíveis

- **🏠 Site público:** http://localhost:5000
- **⚙️ Painel administrativo:** http://localhost:5000/admin/login
- **👤 Credenciais padrão:** usuário `admin` / senha `admin`
- **📊 API do acervo:** http://localhost:5000/api/acervo
- **📧 API de contato:** http://localhost:5000/api/contato

### 🔧 Estrutura de Rotas

- `/` - Página inicial do site
- `/api/acervo` - API REST para listar itens do acervo
- `/api/contato` - API REST para formulário de contato
- `/admin/login` - Login do administrador
- `/admin/dashboard` - Painel do administrador
- `/admin/acervo` - CRUD do acervo (listar, criar, editar, excluir)
- `/admin/acervo/novo` - Formulário para novo item
- `/admin/acervo/editar/<id>` - Formulário para editar item
- `/uploads/<filename>` - Servidor de imagens dos itens

### 🧪 Servidor de Teste

Para debug rápido, execute:
```bash
python test_server.py
```
Acesse: http://localhost:3000

## ✅ O que já foi implementado

### 🔧 Backend
- ✅ Estrutura Flask completa com SQLAlchemy e Flask-Login
- ✅ Sistema de autenticação de admin funcional (login/logout)
- ✅ Modelos de banco de dados para usuários, categorias e itens do acervo
- ✅ CRUD completo para itens do acervo (criar, editar, listar, excluir)
- ✅ Sistema de upload de imagens com validação de tipos
- ✅ API REST para frontend consumir dados (/api/acervo, /api/contato)
- ✅ Categorias pré-populadas automaticamente na primeira execução
- ✅ **6 itens de exemplo criados automaticamente** 
- ✅ Proteção de rotas administrativas com @login_required
- ✅ Tratamento de erros e validações frontend/backend
- ✅ **Configuração CORS correta** para desenvolvimento
- ✅ **Logs de debug** para facilitar desenvolvimento

### 🎨 Frontend
- ✅ Interface moderna e responsiva com CSS Grid
- ✅ **Integração completa funcionando** com backend via API
- ✅ **Exibição dinâmica do acervo** com placeholders para imagens
- ✅ Formulário de contato funcional com validação dupla
- ✅ **Tour virtual 3D melhorado** com ambiente de museu realista
- ✅ Design responsivo otimizado para mobile e desktop
- ✅ **Galeria de acervo com grid responsivo** e hover effects
- ✅ **Console logs detalhados** para debug
- ✅ **Tratamento de erros visuais** para usuário final

### 🚀 Infraestrutura e DevOps
- ✅ Requirements.txt completo com versões específicas
- ✅ **Scripts de inicialização múltiplos** (run.py, start.bat, start.sh)
- ✅ **Servidor de teste independente** (test_server.py)
- ✅ **Configuração correta de rotas estáticas** no Flask
- ✅ Estrutura de uploads organizada com nomes únicos
- ✅ **Documentação completa e atualizada**
- ✅ **Reset automático de banco** para desenvolvimento
- ✅ **Instruções claras de execução** para diferentes OS

## 🚀 Próximos Passos (Opcionais)

- 📧 Implementar envio real de emails no formulário de contato
- 🧪 Adicionar testes automatizados (backend e frontend)
- 🔐 Sistema de múltiplos usuários admin com diferentes permissões
- 📱 Progressive Web App (PWA) para acesso offline
- 🌐 Deploy em produção (Heroku, Vercel, Railway, etc.)
- 📊 Analytics e métricas de visitação (Google Analytics)
- 🎨 Temas customizáveis e modo escuro
- 🔍 Sistema de busca e filtros no acervo
- 📱 App mobile com React Native/Flutter
- 🤖 Chatbot para informações do museu
- 🎮 Gamificação do tour virtual
- 📈 Dashboard com estatísticas de visitação

## 🐛 Troubleshooting

### Problema: "❌ Erro ao carregar acervo"
**Solução**: Verifique se está acessando via servidor Flask (http://localhost:5000) e não abrindo o arquivo HTML diretamente.

### Problema: "ModuleNotFoundError"
**Solução**: Execute `python run.py --install` ou `pip install -r requirements.txt`

### Problema: Banco de dados corrompido
**Solução**: Execute `python run.py --reset` para recriar o banco

### Problema: Porta 5000 ocupada
**Solução**: Use o servidor de teste: `python test_server.py` (porta 3000)

### Problema: Imagens não carregam
**Solução**: Verifique se a pasta `assets/images/acervo_imagens/` existe e tem permissões de escrita


## Contributing

[Outline how others can contribute to the project - if applicable] (e.g., "If you have suggestions for improvements, or if you'd
like to contribute code, please contact the team.")
