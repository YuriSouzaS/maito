import psycopg2

# Função para criar conexão no banco
def conecta_db():
  con = psycopg2.connect(database="db_sie",
                        host="localhost",
                        user="postgres",
                        password="088011",
                        port="5433")
  return con


# Função para inserir dados no banco
def inserir_db(sql):
    con = conecta_db()
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

# Função para consulta na tebla instituição
def select_all(sql):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(sql)
  recset = cur.fetchall()
  registros = []
  for rec in recset:
    registros.append(rec)
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
  (nome,diretor,municipio,cep,rua,numero,email,senha) values ('School Obrian Oconnor','Carlos monte','São bernardo do campo','09951989','santa maira','900','obrian@exemplo.com','321123')'''
  
  # insert da instituição
  # inserir_db(sql)
  
  # sql do select
  sql1 = '''SELECT * FROM public.institution'''
  
  # retorna uma lista[] com tuplas()
  # a = select_all(sql1)

  sql2 = '''SELECT * FROM public.institution WHERE id_inst = %s'''%(1)
  # a = select_one(sql2)
  