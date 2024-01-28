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

  # sql do insert instituição
  sql = '''insert into public.institution 
  (instituicao,diretor, classif, ensino, estado, cidade,cep,rua,numero,email,senha) values ('School Obrian Oconnor','Carlos monte','São bernardo do campo','09951989','santa maira','900','obrian@exemplo.com','321123')'''
  
  # insert da instituição
  inserir_db('escola Genisis','Pedro do grau', 1, 2, 2, 'Diadema','09951090','maira e maraisa','980','cantamuito@exemplo.com','3jjshsh21123')
  
  # sql do select
  id = 1
  
  # retorna uma lista[] com tuplas()
  #a = select_all(id)
  #print(a[0][2])


  sql2 = '''SELECT * FROM public.institution WHERE id_inst = %s'''%(1)
  # a = select_one(sql2)
  