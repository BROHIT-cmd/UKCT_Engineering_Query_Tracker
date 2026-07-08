import streamlit as st
import pandas as pd

from query_db import get_connection
from engineers import ENGINEERS

st.title("📂 Open Queries")

conn = get_connection()

df = pd.read_sql_query(
    "SELECT * FROM queries",
    conn
)

if len(df) == 0:

    st.info("No Queries Found")

else:

    st.dataframe(
        df,
        use_container_width=True
    )

    selected = st.selectbox(
        "Select Query",
        df["query_id"]
    )

    row = df[
        df["query_id"] == selected
    ].iloc[0]

    st.write(
        "Current Owner:",
        row["assigned_to"]
    )

    st.write(
        "Status:",
        row["status"]
    )

    new_owner = st.selectbox(
        "Reassign To",
        list(ENGINEERS.keys())
    )

    if st.button("Reassign Query"):

        cursor = conn.cursor()

        cursor.execute("""
        UPDATE queries
        SET assigned_to=?
        WHERE query_id=?
        """,
        (
            new_owner,
            selected
        ))

        conn.commit()

        st.success(
            f"Query reassigned to {new_owner}"
        )

    resolution = st.text_area(
        "Resolution"
    )

    if st.button("Resolve Query"):

        cursor = conn.cursor()

        cursor.execute("""
        UPDATE queries
        SET status='Resolved',
            resolution=?
        WHERE query_id=?
        """,
        (
            resolution,
            selected
        ))

        conn.commit()

        st.success(
            "Query Resolved"
        )

conn.close()
