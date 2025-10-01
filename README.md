# Comunidade Python Flask

Um site de comunidade onde usuários podem se cadastrar, criar posts e visualizar perfis de outros membros. O projeto foi desenvolvido com **Python** e **Flask**, e está hospedado no **Render**.


## 🌐 Link do site

[Comunidad Python Flask no Render](https://comunidade-python-flask.onrender.com/)


## 🎥 Demonstração

Foi gravado um vídeo mostrando o funcionamento do site.  
Você pode acessá-lo aqui: https://www.linkedin.com/posts/julio-cesar-88220893_python-flask-flaskform-ugcPost-7379172423654539264-Jzzr?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAABPJQuIBRJYffqf6DSF9adLAoC3ZVgqpSQA


## ⚙️ Tecnologias utilizadas

- **Backend:** Python 3.13, Flask  
- **Banco de dados:** SQLite  
- **Autenticação:** Flask-Login, Flask-Bcrypt  
- **Frontend:** HTML, CSS, Bootstrap  
- **Deploy:** Render  


## 📂 Estrutura do projeto
```
comunidade_python_flask/
│
├── comunidadeimpressionadora/ # Aplicação Flask
│ ├── static/ # Arquivos estáticos (CSS, imagens)
│ ├── templates/ # Templates HTML
│ ├── init.py # Inicialização da aplicação
│ ├── routes.py # Rotas do Flask
│ ├── modules.py # Models do SQLAlchemy
│ └── forms.py # Forms do Flask-WTF
│
├── instance/ # Banco de dados SQLite
├── main.py # Arquivo principal para rodar a aplicação
├── requirements.txt # Dependências do Python
└── README.md # Este arquivo
```

## 📝 Funcionalidades

- Cadastro de usuários com email, username e senha criptografada  
- Login e logout de usuários  
- Edição de perfil, incluindo upload de foto de perfil  
- Criação, edição e exclusão de posts  
- Visualização de posts de todos os usuários  
- Contagem de cursos e posts de cada usuário  
- Foto de perfil padrão caso o usuário não tenha enviado uma imagem  


## 📌 Como rodar localmente
```bash
1. Clone o repositório:  

git clone https://github.com/JulioCesarV/comunidade_python_flask.git


2. Entre na pasta do projeto:

cd comunidade_python_flask


3. Crie um ambiente virtual (recomendado):

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows


4. Instale as dependências:

pip install -r requirements.txt


5. Rode a aplicação:

python main.py


Acesse no navegador: http://127.0.0.1:5000


📦 Repositório no GitHub

Código fonte disponível em: https://github.com/JulioCesarV/comunidade_python_flask


📝 Observações

O deploy está hospedado no Render, tornando o site acessível online.

Fotos de perfil são armazenadas localmente na pasta static/fotos_perfil.

Caso o usuário não envie uma foto, será exibida a imagem padrão default.jpg.

