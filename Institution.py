class Institution(object):
    def __init__(self, nome, diretor, tipo, ensino, estado, municipio, cep, rua, numero, senha):
        self.nome = nome
        self.diretor = diretor
        self.tipo = tipo
        self.ensino = ensino
        self.estado = estado
        self.municipio = municipio
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.senha = senha

    def setInstitution(self):
        inst = {}
        inst['nome'] = self.nome
        inst['diretor'] = self.diretor
        inst['tipo'] = self.tipo
        inst['ensino'] = self.ensino
        inst['estado'] = self.estado
        inst['municipio'] = self.municipio
        inst['cep'] = self.cep
        inst['rua'] = self.rua
        inst['numero'] = self.numero
        return inst
       
    
    def getInstitution(self):
        inst = self.setInstitution()
        return inst

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
    inst = Institution("Escola adonias", "Chaga", "publica", "medio", "SP", "Diadema", "12345-090", "Sonia maria", 273, "123sdjs" )
    print(inst.Institution())