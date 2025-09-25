from flask import render_template, redirect, url_for, flash, request, abort, current_app
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormLogin, FormCadastro, FormLoginBotoes, FormEditarPerfil, FormCriarPost
from comunidadeimpressionadora.modules import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image

def salvar_imagem(imagem):
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_completo = nome + codigo + extensao
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_completo)
    tamanho = (200, 200)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    imagem_reduzida.save(caminho_completo)
    return nome_completo

def atualizar_cursos(form):
    lista_cursos = []
    for campo in form:
        if 'curso_' in campo.name:
            if campo.data:
                lista_cursos.append(campo.label.text)
    cursos_str = ''
    for i in range(len(lista_cursos)):
        cursos_str += lista_cursos[i]
        if i < len(lista_cursos) - 1:
            cursos_str += ';'
    return cursos_str

def obter_foto_perfil(usuario):
    foto_nome = usuario.foto_perfil
    if not foto_nome or not os.path.isfile(os.path.join(current_app.root_path, 'static/fotos_perfil', foto_nome)):
        foto_nome = 'default.jpg'
    return url_for('static', filename='fotos_perfil/' + foto_nome)

@app.route("/")
def home():
    lista_posts = Post.query.order_by(Post.id.desc())
    return render_template('home.html', lista_posts=lista_posts)

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
@login_required
def usuarios():
    lista_usuarios = Usuario.query.all()
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_login_botoes = FormLoginBotoes()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login feito com sucesso no email: {form_login.email.data}', 'alert-success')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            return redirect(url_for('home'))
        flash('Falha no login. E-mail ou senha incorretos.', 'alert-danger')

    if form_login_botoes.validate_on_submit() and 'botao_esqueceu_senha' in request.form:
        return redirect(url_for('contato'))
    if form_login_botoes.validate_on_submit() and 'botao_criar_conta' in request.form:
        return redirect(url_for('cadastro'))

    return render_template('login.html', form_login=form_login, form_login_botoes=form_login_botoes)

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    form_cadastro = FormCadastro()
    if form_cadastro.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_cadastro.senha.data).decode("utf-8")
        usuario = Usuario(email=form_cadastro.email.data, username=form_cadastro.username.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada para o e-mail: {form_cadastro.email.data}', 'alert-success')
        return redirect(url_for('login'))
    return render_template('cadastro.html', form_cadastro=form_cadastro)

@app.route("/sair")
@login_required
def sair():
    logout_user()
    flash('Logout feito com sucesso.', 'alert-success')
    return redirect(url_for('home'))

@app.route("/perfil")
@login_required
def perfil():
    foto_perfil = obter_foto_perfil(current_user)
    return render_template('perfil.html', foto_perfil=foto_perfil)

@app.route("/perfil/editar", methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form = FormEditarPerfil()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.username = form.username.data
        if form.foto_perfil.data:
            current_user.foto_perfil = salvar_imagem(form.foto_perfil.data)
        current_user.cursos = atualizar_cursos(form)
        database.session.commit()
        flash('Perfil atualizado com sucesso!', 'alert-success')
        return redirect(url_for('perfil'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    foto_perfil = obter_foto_perfil(current_user)
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form=form)

@app.route("/post/criar", methods=['GET', 'POST'])
@login_required
def criar_post():
    form = FormCriarPost()
    if form.validate_on_submit():
        post = Post(titulo=form.titulo.data, corpo=form.corpo.data, autor=current_user)
        database.session.add(post)
        database.session.commit()
        flash('Post criado com sucesso!', 'alert-success')
        return redirect(url_for('home'))
    return render_template('criarpost.html', form=form)

@app.route("/post/<post_id>", methods=['GET', 'POST'])
def exibir_post(post_id):
    post = Post.query.get(post_id)
    form = None
    if current_user == post.autor:
        form = FormCriarPost()
        if request.method == 'GET':
            form.titulo.data = post.titulo
            form.corpo.data = post.corpo
        elif form.validate_on_submit():
            post.titulo = form.titulo.data
            post.corpo = form.corpo.data
            database.session.commit()
            flash('Post atualizado com sucesso!', 'alert-success')
            return redirect(url_for('home'))
    return render_template('post.html', post=post, form=form)

@app.route("/post/<post_id>/excluir", methods=['GET', 'POST'])
@login_required
def excluir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        database.session.delete(post)
        database.session.commit()
        flash('Post excluído com sucesso!', 'alert-danger')
        return redirect(url_for('home'))
    abort(403)
