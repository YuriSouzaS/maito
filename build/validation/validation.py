import re

class ValidationInstitution(object):
    def __init__(self) -> None:
       self.data = []

    def setInstitution(self, nome: str, diretor: str, tipo: str, ensino: str, estado: str, municipio: str, cep: str, rua: str, numero: str, email: str, senha: str):
        self.data.append(nome)
        self.data.append(diretor)
        self.data.append(tipo)
        self.data.append(ensino)
        self.data.append(estado)
        self.data.append(municipio)
        self.data.append(cep)
        self.data.append(rua)
        self.data.append(numero)
        self.data.append(email)
        self.data.append(senha)


    def getData(self):
        # retorna uma list com dados
        return self.data

    def hasNumber(self):
        v = []
        # verifica se a numeros na string
        padroes = ["[0-9]"]
        verifique = [ self.data[1], self.data[5] ]
        for x in verifique:
            for padrao in padroes:
                if re.search(padrao, x):
                    # Has a number
                    v.append(True)
                else:
                    # No occurrence.
                    v.append(False)
        
        if v[0] or v[1]:
            return "Erro: Não deve conter numeros em Diretor ou Cidade."
        else:
            return True
   
    
    def checkSizeCep(self):
        if len(self.data[6]) <= 8:
            return True
        else:
            return "Erro: Digite o CEP com 8 Números, sem ponto ou traços."

    
    def checkSizeNumber(self):
        if len(self.data[8]) >= 1 and len(self.data[8]) <= 6:
            return True
        else:
            return "Erro: Máximo são 6 digitos."

            
    def validTypeSchool(self):
        typeSchool = ["Publico", "Particular"]
       
        for i in typeSchool:
            if i == self.data[2]:
                return True
            
            

    def typeTeaching(self):
        typeSchool = ["Creche", "Fundamental", "Médio", "Superior", "Profissionalizantes"]
       
        for i in typeSchool:
            if i == self.data[3]:
                return True
            



    def validUf(self):
        # veficica se o UF esta correto 
        uf =  ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RS", "RN", "RO", "RR", "SC", "SP", "SE", "TO"]
        
        for i in uf:
            if i  == self.data[4]:
                return True


    def nameValid(self):
        v = []
        # verifica se a numeros na string
        padroes = ["[0-9]"]
        verifique = [ self.data[1], self.data[5] ]
        for x in verifique:
            for padrao in padroes:
                if re.search(padrao, x):
                    v.append(True)
                else:
                    v.append(False)
        
        if v[0] or v[1]:
            return "Erro: Não deve conter numeros em Diretor ou Cidade."
        else:
            return True

class ValidationResponsavel(object):
    def __init__(self, nome: str, nascimento: str, documento: int, email: str, senha: str) -> None:
        self.nome = nome
        self.nascimento = nascimento
        self.documento = documento
        self.email = email
        self.senha = senha

    # Verificação: Numeros na string(nome)
    def checkNameValid(self):
        pattern = r'[0-9]'
        if re.search(pattern, self.nome):
            return False # Has a number, no valid
        else:
            return True # No occurrence, valid


    # Verificação: Tamanho mínimo e máximo da string(nome)
    def checkSizeName(self):
        if(len(self.nome) >= 3 and len(self.nome) <= 200):
            return True # pass
        else: 
            return False # failed

    # Verificação: Se tem caracteres 
    def checkHasString(self):
        pattern = r'[a-zA-Z]'
        if re.search(pattern, str(self.documento)):
            return True # Has a caracter
        else:
            return False # No occurrence

    # Verificação: Quantidade de digitos do Documento
    def checkDocument(self):
         if(len(str(self.documento)) == 9):
            return True
         else:
            return False

    # Verificação: Email é válido   
    def validateEmail(self):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if (re.match(pattern, self.email)):
            return True
        else:
            return False
       
if __name__ == "__main__":
    i = ValidationResponsavel("Paulo ricardo", "12-12-2000", 121112312, "paulo@email.com", "senha123")
    print(i.checkHasString(), i.checkHasString() )