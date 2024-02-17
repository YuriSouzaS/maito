from build.model.db import inserir_db, inserir_usr, buscar_temporario
from build.geradorKey import sessionKey
from build.validation.validation import ValidationResponsavel, ValidationInstitution

class Responsavel(object):
    def __init__(self,  nome: str, sobrenome: str, nascimento: str, documento: int, email: str, senha: str):
        self.nome = f'{nome} {sobrenome}'
        self.nascimento = nascimento
        self.documento = documento
        self.email = email
        self.senha = senha
        self.qrcode = sessionKey()
        self.saveDb()


    def saveDb(self):
        inserir_usr(self.nome, self.nascimento, self.documento, self.email, self.senha, self.qrcode)

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
        

class Temporario:
    def formatarDados(data):
        a = []
        for i in data:
            a.append(i[0])
        return a

if(__name__ == "__main__"):
    
    Temporario.formatarDados()
    