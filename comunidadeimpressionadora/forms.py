from flask_wtf import  FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.modules import Usuario
from flask_login import current_user

class FormCadastro(FlaskForm):
    username = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    confirmacao_email = StringField('Confirmação do E-mail', validators=[DataRequired(), EqualTo('email')])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar.')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Entrar')

class FormLoginBotoes(FlaskForm):
    botao_esqueceu_senha = SubmitField('Click Aqui!')
    botao_criar_conta = SubmitField('Crie sua conta')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil (.jpg ou .png)', validators=[FileAllowed(['jpg', 'png'])])
    curso_excel = BooleanField('Curso de Excel')
    curso_vba = BooleanField('Curso de VBA')
    curso_powerbi = BooleanField('Curso de Power BI')
    curso_python = BooleanField('Curso de Python')
    curso_ppt = BooleanField('Curso de PowerPoint')
    curso_sql = BooleanField('Curso de SQL')
    botao_editar_perfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já esxiste um usuário cadastrado com esse e-mail. Cadastre outro e-mail')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva Seu Post Aqui', validators=[DataRequired()])
    botao_criar_post = SubmitField('Criar Post')
