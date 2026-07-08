import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Allow imports from parent folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from query_db import get_connection
from engineers import ENGINEERS

st.title("👨‍💻 My Queries")

selected_user = st.selectbox(
    "Engineer",
    list(ENGINEERS.keys())
)

conn = get_connection()

query = """
SELECT *
FROM queries
WHERE assigned_to = ?
"""

df = pd.read_sql_query(
    query,
    conn,
    params=(selected_user,)
)

if len(df) == 0:
    st.info("No queries assigned.")
else:
    st.dataframe(
        df,
        use_container_width=True
    )

conn.close()
