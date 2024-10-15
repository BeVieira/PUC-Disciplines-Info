import psycopg2;
from site_disciplines_info.settings import DATABASES;

name = DATABASES['default']['NAME']
user = DATABASES['default']['USER']
password = DATABASES['default']['PASSWORD']
host = DATABASES['default']['HOST']
port = DATABASES['default']['PORT']

def buscar_disciplinas(termo_busca):
    try:
        # Conexão ao banco de dados PostgreSQL
        conexao = psycopg2.connect(
            dbname=name,
            user=user,
            password=name,
            host=host,
            port=port
        )
        cursor = conexao.cursor()

        query = """
            SELECT nome
            FROM disciplinas
            WHERE nome ILIKE %s;
        """
        cursor.execute(query, (f"%{termo_busca}%",))

        disciplinas_encontradas = cursor.fetchall()

        cursor.close()
        conexao.close()

        if not disciplinas_encontradas:
            return "Nenhuma disciplina encontrada."
        
        return [disciplina[0] for disciplina in disciplinas_encontradas]

    except Exception as e:
        return f"Erro ao buscar disciplinas: {e}"