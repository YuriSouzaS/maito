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
  cur.close()

# Função para consulta na tebla instituição
def select_all(tabela, id):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(f"SELECT * FROM {tabela} WHERE id={id}")
  rows = cur.fetchall()
  registros = []
  
  for row in rows:
    registros.append(row)
  con.close()
  
  return registros


# 
def select_user(tabela, email):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(f"SELECT * FROM {tabela} WHERE email='{email}'")
  recset = cur.fetchone()
  con.close()
  return recset
