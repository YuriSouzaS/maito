import re

class validacao(object):
    def __init__(self) -> None:
       self.data = []

    def setData(self, nome: str, diretor: str, tipo: str, ensino: str, estado: str, municipio: str, cep: str, rua: str, numero: str, senha: str):
        self.data.append(nome)
        self.data.append(diretor)
        self.data.append(tipo)
        self.data.append(ensino)
        self.data.append(estado)
        self.data.append(municipio)
        self.data.append(cep)
        self.data.append(rua)
        self.data.append(numero)
        self.data.append(senha)


    def getData(self):
        # retorna uma list com dados
        return self.data

    def validString(self):
        v = []
        # verifica se a numeros na string
        padroes = ["[0-9]"]
        verifique = [self.data[0], self.data[1], self.data[5]]
        for x in verifique:
            for padrao in padroes:
                if re.search(padrao, x):
                    # print(f"Has a number: {x}")
                    v.append(True)
                else:
                    # print('No occurrence.')
                    v.append(False)
        
        # print(v)
        if v[0] or v[1] or v[2]:
            return False
        else:
            return True
   
    
    def sizeCep(self):
        if len(self.data[6]) <= 8:
            # print(f"{self.data[6]}, size: {len(self.data[6])}")
            return True
        else:
            return False

    
    def sizeNum(self):
        if len(self.data[8]) >= 1 and len(self.data[8]) <= 6:
            print(f"{self.data[8]}, size: {len(self.data[8])}")
            return True
        else:
            return False

    
    # verifica o tamanho da string
    def validSize(self):
        for i in self.data:            
            if len(i) > 3 and len(i) < 30:
                # print(f"Pass: {i}, size: {len(i)}")
                return True
            else:
                # print(f"Pass: {i}, size: {len(i)}")
                return False
            
    def validTypeSchool(self):
        typeSchool = ["Publico", "Particular"]
       
        for i in typeSchool:
            if i == self.data[2]:
                # print(f"tipo: {i}")
                return True
            else:
                return False



    def validUf(self):
        # veficica se o UF esta correto 
        uf =  ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RS", "RN", "RO", "RR", "SC", "SP", "SE", "TO"]
        
        for i in uf:
            if i  == self.data[4]:
                # print(f"pass: {self.data[4]}")
                return True
            else:
                return False


if __name__ == "__main__":
    i = validacao()
    i.setData("escola", "Chaga2", "ublico", "medio", "SP", "Diadema", "12345090", "Sonia maria", "", "123sdjs")
    