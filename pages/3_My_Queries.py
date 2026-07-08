import streamlit as st
import pandas as pd

from query_db import get_connection
from engineers import ENGINEERS

st.title("👨‍💻 My Queries")

selected_user = st.selectbox(
    "Engineer",
    list(ENGINEERS.keys())
)

conn = get_connection()

df = pd.read_sql_query(
    f"""
    SELECT *
    FROM queries
    WHERE assigned_to='{selected_user}'
    """,
    conn
)

st.dataframe(
    df,
    use_container_width=True
)

conn.close()
