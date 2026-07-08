import sqlite3

DB_NAME = "ukct_queries.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS queries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query_id TEXT,
        project_name TEXT,
        project_type TEXT,
        category TEXT,
        priority TEXT,
        description TEXT,
        assigned_to TEXT,
        status TEXT,
        reassign_reason TEXT,
        resolution TEXT,
        created_date TEXT,
        closed_date TEXT
    )
    """)

    conn.commit()
    conn.close()
