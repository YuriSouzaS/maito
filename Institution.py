from db import inserir_db, conecta_db

class Institution(object):
    def __init__(self,  nome: str, diretor: str, tipo: str, ensino: str, estado: str, municipio: str, cep: str, rua: str, numero: int, email: str, senha: str):
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
        

    def setInstitution(self):
        self.inst = {}
        self.inst['nome'] = self.nome 
        self.inst['diretor'] = self.diretor
        self.inst['tipo'] = self.tipo
        self.inst['ensino'] = self.ensino
        self.inst['estado'] = self.estado
        self.inst['municipio'] = self.municipio
        self.inst['cep'] = self.cep
        self.inst['rua'] = self.rua
        self.inst['numero'] = self.numero
        self.inst['email'] = self.email
        return self.inst
       
    
    def getInstitution(self):
        getData = self.setInstitution()
        return getData
    

    def getNome(self):
        return self.nome
    
    def setEndereco(self):
        endereco = {}
        endereco['estado'] = self.estado
        endereco['municipio'] = self.municipio
        endereco['cep'] = self.cep
        endereco['rua'] = self.rua
        endereco['numero'] = self.numero
        return endereco


    def getEndereco(self):
        ender = self.setEndereco()
        return ender


if __name__ == "__main__":
    i = Institution("Escola Arco iris", "Chagas", "publica", "medio", "SP", "Diadema", "12345090", "Sonia abrão", 273, "email@exemplo123.com", "123sdjs" )
    # i.getInstitution()
    # print(i.nome)
    # v = Validaction()
    # v.sizeString()
    sql = f'''insert into public.institution 
(nome,diretor,municipio,cep,rua,numero,email,senha) values ('{i.nome}','{i.diretor}','{i.municipio}','{i.cep}','{i.rua}','{i.numero}','{i.email}','{i.senha}')'''
    inserir_db(sql)
    