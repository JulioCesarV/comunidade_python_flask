# from comunidadeimpressionadora import app, database
# from comunidadeimpressionadora.modules import Usuario, Post
#
# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(email='julio@gmail.com', senha='123456')
#     usuario2 = Usuario(email='lira@gmail.com', senha='123456')
#
#     database.session.add(usuario)
#     database.session.add(usuario2)
#
#     database.session.commit()

# with app.app_context():
#     meus_usuarios = Usuario.query.first()
#     print(meus_usuarios.senha)
    # usuario_teste = Usuario.query.filter_by(id=2).first()
    # print(usuario_teste.senha)

# with app.app_context():
#     meu_post = Post(id_usuario = 1, titulo='Primeiro Post do Julio', corpo='Julio Voando')
#     database.session.add(meu_post)
#     database.session.commit()

# with app.app_context():
#      post = Post.query.first()
#      print(post.corpo)
#      print(post.autor.email)

# with app.app_context():
#     database.drop_all()
#     database.create_all()

# with app.app_context():
#     post = Post.query.filter_by(id_usuario=1).first()
#     print(post.corpo)