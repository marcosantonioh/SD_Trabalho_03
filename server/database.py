import sqlite3

NOME_BD = "readings.db"

def criar_tabela():
    conexao = sqlite3.connect(NOME_BD)
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leituras (
        id TEXT PRIMARY KEY,
        sensor_id TEXT,
        temperatura REAL,
        status_logico TEXT,
        timestamp TEXT
    )
    """)

    conexao.commit()
    conexao.close()


def inserir_leitura(id, sensor_id, temperatura, status, timestamp):
    conexao = sqlite3.connect(NOME_BD)
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO leituras (id, sensor_id, temperatura, status_logico, timestamp)
        VALUES (?, ?, ?, ?, ?)
        """, (id, sensor_id, temperatura, status, timestamp))

        conexao.commit()
        return True
    except:
        return False
    finally:
        conexao.close()


def check_uuid(uuid):
    conexao = sqlite3.connect(NOME_BD)
    cursor = conexao.cursor()

    cursor.execute("SELECT id FROM leituras WHERE id=?", (uuid,))
    result = cursor.fetchone()

    conexao.close()

    return result is not None