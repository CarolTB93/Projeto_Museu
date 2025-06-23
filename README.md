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

### Método Rápido (Recomendado)

1.  **Instalar dependências:**
    ```bash
    python run.py --install
    ```

2.  **Executar a aplicação:**
    ```bash
    python run.py
    ```

### Método Manual

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Flask Application:**
    ```bash
    cd src/backend
    python app.py
    ```

### Acesso ao Sistema

- **Site público:** http://localhost:5000
- **Painel administrativo:** http://localhost:5000/admin/login
- **Credenciais padrão:** usuário `admin` / senha `admin`

### Estrutura de URLs

- `/` - Página inicial do site
- `/api/acervo` - API para listar itens do acervo
- `/api/contato` - API para formulário de contato
- `/admin/login` - Login do administrador
- `/admin/dashboard` - Painel do administrador
- `/admin/acervo` - Gestão do acervo
- `/uploads/<filename>` - Imagens dos itens do acervo

## ✅ O que já foi implementado

### Backend
- ✅ Estrutura Flask completa com SQLAlchemy e Flask-Login
- ✅ Sistema de autenticação de admin funcional (login/logout)
- ✅ Modelos de banco de dados para usuários, categorias e itens do acervo
- ✅ CRUD completo para itens do acervo (criar, editar, listar, excluir)
- ✅ Sistema de upload de imagens com validação
- ✅ API REST para frontend consumir dados (/api/acervo, /api/contato)
- ✅ Categorias pré-populadas automaticamente
- ✅ Proteção de rotas administrativas
- ✅ Tratamento de erros e validações

### Frontend
- ✅ Interface moderna e responsiva
- ✅ Integração completa com backend via API
- ✅ Exibição dinâmica do acervo com imagens
- ✅ Formulário de contato funcional com validação
- ✅ Tour virtual 3D melhorado com Three.js
- ✅ Design responsivo para mobile e desktop
- ✅ Galeria de acervo com grid responsivo

### Infraestrutura
- ✅ Requirements.txt completo com todas as dependências
- ✅ Script de inicialização automatizado (run.py)
- ✅ Configuração de arquivos estáticos
- ✅ Estrutura de uploads organizada
- ✅ Documentação atualizada

## 🚀 Próximos Passos (Opcionais)

- 📧 Implementar envio real de emails no formulário de contato
- 🧪 Adicionar testes automatizados (backend e frontend)
- 🔐 Sistema de múltiplos usuários admin
- 📱 Progressive Web App (PWA)
- 🌐 Deploy em produção (Heroku, Vercel, etc.)
- 📊 Analytics e métricas de visitação
- 🎨 Temas customizáveis
- 🔍 Sistema de busca no acervo

## Team Members

*   [List Team Members Here - Add Names and Roles]

## Contact

*   [Your Email Address / Contact Information]

## License

[Specify the License - e.g., MIT License] (A simple statement like "This project is licensed under the MIT License.")

## Contributing

[Outline how others can contribute to the project - if applicable] (e.g., "If you have suggestions for improvements, or if you'd
like to contribute code, please contact the team.")
