import streamlit as st
import pandas as pd
from database.database import get_connection

st.title("📂 Open Queries")

conn = get_connection()

df = pd.read_sql_query(
    """
    SELECT * FROM queries
    WHERE status != 'Closed'
    """,
    conn
)

if len(df) == 0:
    st.info("No open queries")

else:

    st.dataframe(df)

    selected = st.selectbox(
        "Select Query",
        df["query_id"]
    )

    row = df[df["query_id"] == selected].iloc[0]

    st.subheader(selected)

    st.write("Project:", row["project_name"])
    st.write("Assigned:", row["assigned_to"])
    st.write("Status:", row["status"])

    engineers = [
        "Rohit",
        "Engineer A",
        "Engineer B",
        "Engineer C",
        "Engineer D"
    ]

    new_owner = st.selectbox(
        "Reassign To",
        engineers
    )

    reason = st.text_input(
        "Reason"
    )

    if st.button("Reassign"):

        cursor = conn.cursor()

        cursor.execute("""
        UPDATE queries
        SET assigned_to=?,
            reassign_reason=?,
            status='Assigned'
        WHERE query_id=?
        """,
        (
            new_owner,
            reason,
            selected
        ))

        conn.commit()

        st.success("Query Reassigned")

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

        st.success("Query Resolved")
