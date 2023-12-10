import re
# from db import serir_db

# Corrigir erro na função validString


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
        # verifica se a numeros na string
        padroes = ["[0-9]"]
        verifique = [self.data[0], self.data[1], self.data[5]]
        count = 0
        for i in verifique:
            print(f"Checking!... {i}")
            for padrao in padroes:
                if re.search(padrao, i):
                    print(f"Has a number: {i}")
                    count += 1
                    if count == len(verifique):
                        return True
                else:
                    print('No occurrence.')
                    count += 1
                    if count == len(verifique):
                        return False
    
    def validCep(self):
        if len(self.data[6]) > 3 and len(self.data[6]) <= 7:
            print(f"{self.data[6]}, size: {len(i)}")
            return True

    
    def validNum(self):
        if len(self.data[6]) >= 1 and len(self.data[6]) <= 6:
            print(f"{self.data[6]}, size: {len(i)}")
            return True

    
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



    def validUf(self):
        # veficica se o UF esta correto 
        uf =  ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RS", "RN", "RO", "RR", "SC", "SP", "SE", "TO"]
        
        for i in uf:
            if i  == self.data[4]:
                # print(f"pass: {self.data[4]}")
                return True


    def main(self):
        i = validacao()
        i.setData("escola", "Chaga", "Publico", "medio", "SP", "Diadema", "12345090", "Sonia maria", "273", "123sdjs" )
        if not i.validString:
            print("validString pass:")
        else:
            print("erro: validStr")




if __name__ == "__main__":
    i = validacao()
    i.setData("escola", "Chaga", "Publico", "medio", "SP", "Diadema", "12345090", "Sonia maria", "273", "123sdjs" )
    # d = i.getData()
    # print(i.validSize())
    # i.validUf()
    print(i.validString())
    # print(i.validTypeSchool())
    # i.main()