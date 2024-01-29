import sqlite3

# Função para criar conexão no banco
def conecta_db():
  con = None
  
  try:
    con = sqlite3.connect("SIE.db")
  except Error as e:
    print(e)
  
  return con


# Função para inserir dados no banco
def inserir_db(instituicao, diretor, classif, ensino, estado, cidade, cep, rua, numero, email, senha):
  sql = f'''
          insert into INSTITUICAO 
          (instituicao,diretor,fk_classificacao, fk_ensino, fk_estado, cidade,cep,logradouro,numero,email,senha)
          values
          ('{instituicao}','{diretor}',{classif},{ensino},{estado},'{cidade}','{cep}','{rua}','{numero}','{email}','{senha}')
      '''
  
  con = conecta_db()
  cur = con.cursor()

  cur.execute(sql)
  con.commit()
  print('Dados inseridos com sucesso.')
  cur.close()


  # Função para inserir dados no banco
def inserir_usr(nome, data_nascimento, documento, email, senha, usr_qrcode):
  sql = f'''
          insert into responsavel 
          (nome,data_nascimento,numero_documento, email,senha,numero_qrcode)
          values
          ('{nome}','{data_nascimento}',{documento},'{email}','{senha}','{usr_qrcode}')
      '''
  
  con = conecta_db()
  cur = con.cursor()

  cur.execute(sql)
  con.commit()
  print('Dados inseridos com sucesso.')
  cur.close()

# Função para consulta na tebla instituição
def select_all(id):
  con = conecta_db()
  cur = con.cursor()

  cur.execute(f"SELECT * FROM INSTITUICAO WHERE id={id}")
  
  rows = cur.fetchall()
  registros = []
  
  for row in rows:
    registros.append(row)
  con.close()
  
  return registros


# 
def select_one(sql):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(sql)
  recset = cur.fetchone()
  con.close()
  return recset

if __name__ == "__main__":

  # insert da instituição
  #inserir_db('escola gael','Pedro marques', 2, 2, 2, 'Diadema','09951090','maira e maraisa','980','gael@exemplo.com','3jjshsh21123')

  inserir_usr('kali torres','17/02/1989', 129951090 ,'kalitorres@gmail.com','mahdnd980','majkdkuheo383n3')
  
  #print(select_all(2))
  