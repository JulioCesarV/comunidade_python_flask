from comunidadeimpressionadora import database, login_manager
from datetime import datetime
from flask_login import UserMixin
from flask import url_for, current_app
import os

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não informado')

    def contar_posts(self):
        return len(self.posts)

    @property
    def foto_perfil_url(self):
        nome_foto = self.foto_perfil
        caminho_foto = os.path.join(current_app.root_path, 'static', 'fotos_perfil', nome_foto or '')
        if not nome_foto or not os.path.isfile(caminho_foto):
            nome_foto = 'default.jpg'
        return url_for('static', filename='fotos_perfil/' + nome_foto)



class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)