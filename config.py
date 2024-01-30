from db import inserir_db, inserir_usr

class Responsavel(object):
    def __init__(self,  nome: str, sobrenome: str, nascimento: str, documento: int, email: str, senha: str, qrcode: str):
        self.nome = f'{nome} {sobrenome}'
        self.nascimento = nascimento
        self.documento = documento
        self.email = email
        self.senha = senha
        self.qrcode = qrcode
        self.saveDb()


    def saveDb(self):
        inserir_usr(self.nome, self.nascimento, self.documento, self.email, self.senha, self.qrcode)
        print("salvo no banco!")

class Institution(object):
    def __init__(self,  nome: str, diretor: str, tipo: int, ensino: int, estado: int, municipio: str, cep: str, rua: str, numero: str, email: str, senha: str):
        self.nome = nome
        self.diretor = diretor
        self.tipo = tipo
        self.ensino = ensino
        self.estado = estado
        self.municipio = municipio
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.email = email
        self.senha = senha
        self.saveDb()

    def saveDb(self):
        inserir_db(self.nome, self.diretor, self.tipo, self.ensino, self.estado, self.municipio, self.cep, self.rua, self.numero, self.email, self.senha)
        print("salvo no banco!")
        

if __name__ == "__main__":
    #   i = Institution("Escola Arco iris", "Chagas", 1, 3, 24, "Diadema", 12345090, "Sonia abrão", 273, "email@exemplo123.com", "123sdjs" )
    #   print(i.setInstitution())

       usr = Responsavel("acacio", "marques", "12/03/1992", 18182823, "acacio@gmail.com", "akjhojji383", "nahhuebe83878ww4")
       #usr.saveDb()
       print(usr.nome, usr.email, usr.qrcode)