from comunidadeImpressonadora import app, database
from comunidadeImpressonadora.models import Usuario

with app.app_context():
    database.drop_all()
    database.create_all()
# with app.app_context():
#     usuario1 = Usuario(username="marcio", email="marcio@hotmail.com", senha="123456")
#     usuario2 = Usuario(username="joao", email="joao@hotmail.com", senha="123456")
#     usuario3 = Usuario(username="Matheus", email="matheus@hotmail.com", senha="123456")
#     usuario4 = Usuario(username="Felipe", email="felipe@hotmail.com", senha="123456")
#
#     database.session.add(usuario1)
#     database.session.add(usuario2)
#     database.session.add(usuario3)
#     database.session.add(usuario4)
#
#     database.session.commit()


# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#
#     print(meus_usuarios)
    # print(meus_usuarios)
    # print(meus_usuarios[0].email)
    # print("--" * 20)


    # print("--" * 30)
    # print(meus_usuarios[1].email)

# with app.app_context():
#     database.drop_all()
#     database.create_all()


