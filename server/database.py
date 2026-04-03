import sqlite3

DB_NAME = "readings.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leituras (
        id TEXT PRIMARY KEY,
        sensor_id TEXT,
        temperatura REAL,
        status_logico TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_reading(id, sensor_id, temperatura, status, timestamp):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO leituras (id, sensor_id, temperatura, status_logico, timestamp)
        VALUES (?, ?, ?, ?, ?)
        """, (id, sensor_id, temperatura, status, timestamp))

        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def check_uuid(uuid):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM leituras WHERE id=?", (uuid,))
    result = cursor.fetchone()

    conn.close()

    return result is not None