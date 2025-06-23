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

# Museu do Aeroclube do Paraná - Projeto do Site

**Versão:** 1.0  
**Data:** 26 de outubro de 2023

## Visão Geral

Este projeto tem como objetivo criar um site dinâmico apresentando a história do Aeroclube do Paraná. O site contará com um tour virtual interativo pelo museu, um catálogo completo da coleção e uma área administrativa fácil de usar para gerenciamento e interação com visitantes. Este é um projeto colaborativo e interdisciplinar do Centro Universitário Uniopet.

## Objetivos do Projeto

*   Desenvolver um site bonito e informativo.
*   Criar um tour virtual interativo usando Three.js.
*   Construir um sistema com banco de dados para gerenciar a coleção do Aeroclube.
*   Fornecer uma área administrativa para gerenciar o conteúdo do site.
*   Criar uma base para futuras melhorias e expansões do site.

## Tecnologias Utilizadas

*   **Frontend:** HTML5, CSS3, JavaScript (JS puro & possivelmente jQuery), Bootstrap
*   **Backend:** Python (Flask)
*   **Banco de Dados:** SQLite
*   **Tour Virtual:** Three.js
*   **Login:** Flask-Login (Exemplo Simplificado)

## Estrutura do Projeto

O projeto está organizado nas seguintes pastas:

*   `src/`: Código-fonte do site, dividido em frontend e backend.
    *   `frontend/`: Arquivos HTML, CSS e JavaScript da interface do site.
    *   `backend/`: Arquivos Python (Flask) do sistema.
*   `docs/`: Documentação, diagramas e arquivos relacionados ao projeto.
*   `assets/`: Imagens e outros arquivos estáticos.
*   `requirements.txt`: Lista das dependências do Python usadas no projeto.

## Como Instalar e Rodar

### Método Rápido (Recomendado)

1.  **Instalar as dependências:**
    ```bash
    python run.py --install
    ```

2.  **Rodar a aplicação:**
    ```bash
    python run.py
    ```

### Método Manual

1.  **Instalar as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Rodar o sistema Flask:**
    ```bash
    cd src/backend
    python app.py
    ```

### Acesso ao Sistema

- **Site público:** http://localhost:5000
- **Painel administrativo:** http://localhost:5000/admin/login
- **Usuário e senha padrão:** usuário `admin` / senha `admin`

### Endereços principais do site

- `/` - Página inicial do site
- `/api/acervo` - API para listar itens do acervo
- `/api/contato` - API para formulário de contato
- `/admin/login` - Login do administrador
- `/admin/dashboard` - Painel do administrador
- `/admin/acervo` - Gerenciamento do acervo
- `/uploads/<filename>` - Imagens dos itens do acervo

## ✅ O que já está pronto

### Backend
- ✅ Estrutura Flask completa com SQLAlchemy e Flask-Login
- ✅ Sistema de login para administrador funcionando (login/logout)
- ✅ Modelos do banco de dados para usuários, categorias e itens do acervo
- ✅ CRUD completo para itens do acervo (criar, editar, listar, excluir)
- ✅ Upload de imagens com validação
- ✅ API REST para o frontend acessar dados (/api/acervo, /api/contato)
- ✅ Categorias cadastradas automaticamente
- ✅ Proteção das páginas administrativas
- ✅ Tratamento de erros e validações

### Frontend
- ✅ Interface moderna e responsiva
- ✅ Integração total com o backend via API
- ✅ Exibição dinâmica do acervo com imagens
- ✅ Formulário de contato funcionando e com validação
- ✅ Tour virtual 3D com Three.js
- ✅ Layout adaptável para celular e computador
- ✅ Galeria do acervo com visualização em grade

### Infraestrutura
- ✅ Arquivo requirements.txt completo com todas as dependências
- ✅ Script de inicialização automatizado (run.py)
- ✅ Configuração de arquivos estáticos
- ✅ Estrutura organizada para uploads
- ✅ Documentação atualizada

## 🚀 Próximos Passos (Opcionais)

- 📧 Implementar envio real de e-mails no formulário de contato
- 🧪 Adicionar testes automáticos (backend e frontend)
- 🔐 Sistema com múltiplos administradores
- 📱 Tornar o site um aplicativo web progressivo (PWA)
- 🌐 Publicar em produção (Heroku, Vercel, etc.)
- 📊 Adicionar métricas de visitação
- 🎨 Permitir troca de temas/cores do site
- 🔍 Sistema de busca no acervo

## Integrantes

*   [Liste os nomes e funções dos integrantes aqui]

## Contato

*   [Seu e-mail ou outra forma de contato]

## Licença

[Informe a licença do projeto - ex: MIT License] (Exemplo: "Este projeto está sob a licença MIT.")

## Como contribuir

[Explique como outras pessoas podem contribuir para o projeto, se desejar] (Exemplo: "Se você tem sugestões de melhorias ou quer contribuir com código, entre em contato com a equipe.")

