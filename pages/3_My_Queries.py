import streamlit as st
import pandas as pd
from database.database import get_connection

st.title("👨‍💻 My Queries")

engineers = [
    "Rohit",
    "Engineer A",
    "Engineer B",
    "Engineer C",
    "Engineer D"
]

selected_user = st.selectbox(
    "Select Engineer",
    engineers
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

st.dataframe(df)
