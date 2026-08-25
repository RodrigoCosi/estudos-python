from conexao import conectar

def executar_consulta(sql, parametros=None, buscar=False):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(sql, parametros or())

        if buscar:
           return cursor.fetchall()

        conexao.commit()
        return cursor.rowcount  # Retorna o número de linhas afetadas

    except Exception:
        conexao.rollback()
        raise   

    finally:
        cursor.close()
        conexao.close()
    
    
def listar_produtos():
  sql = "SELECT * FROM produtos ORDER BY id"

  return executar_consulta(sql, buscar=True)


def cadastrar_produto(nome, descricao, quantidade, preco):
    sql =   """
        INSERT INTO produtos (nome, descricao, quantidade, preco)
        VALUES (%s, %s, %s, %s)
        """,
    return executar_consulta(
        sql,
        (nome, descricao, quantidade, preco)
    )
    

def atualizar_produto(id_produto, nome, descricao, quantidade, preco):
  
    sql = """
        UPDATE produtos
        SET nome = %s, 
        descricao = %s, 
        quantidade = %s, 
        preco = %s
        WHERE id = %s
        """,

    linhas_alteradas = executar_consulta(
        sql,
      (nome, descricao, quantidade, preco, id_produto)
    )

    return linhas_alteradas > 0  # Retorna True se algum registro foi atualizado, caso contrário, False


def excluir_produto(id_produto):
   
    sql = """
        DELETE FROM produtos
        WHERE id = %s
        """,

    linhas_excluidas = executar_consulta(
        sql,
        (id_produto,)
    )
    return linhas_excluidas > 0  # Retorna True se algum registro foi excluído, caso contrário, False


def buscar_produto(nome):
  sql = """  
        SELECT * FROM produtos
        WHERE nome ILIKE %s
        ORDER BY nome
    """

  return executar_consulta(
       sql,
         (f"%{nome}%",),
          buscar=True
    )