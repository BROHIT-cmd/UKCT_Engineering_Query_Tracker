import sqlite3


def get_connection():
    return sqlite3.connect(
        "ukct_queries.db",
        check_same_thread=False
    )


def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS queries (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        query_id TEXT,

        project_name TEXT,

        category TEXT,

        priority TEXT,

        description TEXT,

        assigned_to TEXT,

        status TEXT,

        resolution TEXT,

        created_date TEXT,

        closed_date TEXT

    )
    """)

    conn.commit()
    conn.close()
`
