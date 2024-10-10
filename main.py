import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# Conexão com o banco de dados.
Session = sessionmaker(bind=db)
session = Session()

# Criando tabela.
Base = declarative_base()

class Usuario(Base):
    # Definindo nome da tabela.
    __tablename__ = "usuarios"

    # Definindo atributos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

os.system("cls || clear")

# Salvar no banco de dados.
# usuario = Usuario("Marta", "marta@gmail.com", "123")
# usuario = Usuario(senha="123", nome="José", email="jose@gmail.com")

for i in range(2):
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha=  input("Digite sua senha: ")

    usuario =  Usuario(senha=senha, nome=nome, email=email)
    session.add(usuario)
    session.commit()
    print()

# Mostrando conteúdo do banco de dados.
print("\nListando usuários no banco de dados.")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")

# Deletando um usuário.
usuario = session.query(Usuario).filter_by(email ="joao@gmail.com").first()
session.delete(usuario)
session.commit()
print("\nUsuário deletado com sucesso.")

# Mostrando conteúdo do banco de dados.
print("\nListando usuários no banco de dados.")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")

