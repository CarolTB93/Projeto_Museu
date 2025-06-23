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

# Museu do Aeroclube do Paraná - Projeto de Website

**Versão:** 1.0  
**Data:** 26 de outubro de 2023

## Visão Geral

Este projeto tem como objetivo criar um site dinâmico apresentando a história do Aeroclube do Paraná. O site contará com um tour virtual interativo pelo museu, um catálogo completo do acervo e uma interface amigável para administração e possível interação com visitantes. Este é um projeto colaborativo e interdisciplinar do Centro Universitário Uniopet.

## Objetivos do Projeto

*   Desenvolver um site visualmente atrativo e informativo.
*   Criar um tour virtual interativo usando Three.js.
*   Construir um sistema baseado em banco de dados para gerenciar o acervo do Aeroclube.
*   Fornecer uma interface administrativa para gerenciar o conteúdo do site.
*   Estabelecer uma base para futuras melhorias e expansão do site.

## Tecnologias Utilizadas

*   **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS & possivelmente jQuery), Bootstrap
*   **Backend:** Python (Flask)
*   **Database:** SQLite
*   **Tour Virtual:** Three.js
*   **Login:** Flask-Login (Exemplo Simplificado)

## Estrutura do Projeto

O projeto está organizado nas seguintes pastas:

*   `src/`: Contém o código-fonte do frontend e backend.
    *   `frontend/`: Arquivos HTML, CSS e JavaScript da interface do site.
    *   `backend/`: Arquivos da aplicação Python (Flask).
*   `docs/`: Documentação, diagramas e outros arquivos do projeto.
*   `assets/`: Imagens e outros arquivos estáticos.
*   `requirements.txt`: Lista todas as dependências Python do projeto.

## Instalação e Execução

### 🚀 Método Mais Fácil (Windows)

**Dê um duplo clique no arquivo:**
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

2.  **Executar a aplicação:**
    ```bash
    python run.py
    ```

3.  **Resetar o banco (se necessário):**
    ```bash
    python run.py --reset
    ```

### 🛠️ Método Manual

1.  **Instalar dependências:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Executar o servidor Flask:**
    ```bash
    cd src/backend
    python app.py
    ```

### 🌐 Como Acessar

**⚠️ IMPORTANTE**: Sempre acesse pelo servidor Flask, **NUNCA** abra o arquivo HTML diretamente no navegador!

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
- `/admin/dashboard` - Painel administrativo
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
- ✅ API REST para o frontend consumir dados (/api/acervo, /api/contato)
- ✅ Categorias pré-cadastradas automaticamente na primeira execução
- ✅ **6 itens de exemplo criados automaticamente** 
- ✅ Proteção das rotas administrativas com @login_required
- ✅ Tratamento de erros e validações no frontend/backend
- ✅ **Configuração CORS correta** para desenvolvimento
- ✅ **Logs de debug** para facilitar o desenvolvimento

### 🎨 Frontend
- ✅ Interface moderna e responsiva com CSS Grid
- ✅ **Integração completa funcionando** com backend via API
- ✅ **Exibição dinâmica do acervo** com placeholders para imagens
- ✅ Formulário de contato funcional com validação dupla
- ✅ **Tour virtual 3D melhorado** com ambiente de museu realista
- ✅ Design responsivo otimizado para mobile e desktop
- ✅ **Galeria do acervo com grid responsivo** e efeitos de hover
- ✅ **Console logs detalhados** para debug
- ✅ **Tratamento de erros visuais** para o usuário final

### 🚀 Infraestrutura e DevOps
- ✅ Requirements.txt completo com versões específicas
- ✅ **Scripts de inicialização múltiplos** (run.py, start.bat, start.sh)
- ✅ **Servidor de teste independente** (test_server.py)
- ✅ **Configuração correta de rotas estáticas** no Flask
- ✅ Estrutura de uploads organizada com nomes únicos
- ✅ **Documentação completa e atualizada**
- ✅ **Reset automático do banco** para desenvolvimento
- ✅ **Instruções claras de execução** para diferentes sistemas operacionais

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

## 🐛 Solução de Problemas

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


## Contribuindo

[Descreva como outras pessoas podem contribuir com o projeto - se aplicável] (ex: "Se você tem sugestões de melhorias ou quer contribuir com código, entre em contato com a equipe.")
