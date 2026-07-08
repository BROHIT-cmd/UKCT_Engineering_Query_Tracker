import streamlit as st
import pandas as pd
from database.database import get_connection

st.title("📚 Knowledge Base")

search = st.text_input(
    "Search"
)

conn = get_connection()

df = pd.read_sql_query(
    """
    SELECT *
    FROM queries
    WHERE status='Resolved'
    """,
    conn
)

if search:

    df = df[
        df["description"]
        .fillna("")
        .str.contains(
            search,
            case=False
        )
    ]

show_cols = [
    "query_id",
    "project_name",
    "category",
    "description",
    "resolution"
]

st.dataframe(df[show_cols])
