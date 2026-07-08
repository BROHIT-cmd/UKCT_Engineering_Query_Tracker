import streamlit as st
from query_db import get_connection
from datetime import datetime
from engineers import ENGINEERS

st.title("📝 Submit Query")

project_name = st.text_input(
    "Project Name"
)

category = st.selectbox(
    "Category",
    [
        "Hydraulics",
        "Pump Selection",
        "Mechanical Design",
        "Wet Well Design",
        "Valve Selection",
        "Pipeline Design",
        "Commissioning",
        "Civil Interface",
        "Electrical Interface",
        "Client Comment",
        "Site Query",
        "General"
    ]
)

priority = st.selectbox(
    "Priority",
    ["High", "Medium", "Low"]
)

assigned_to = st.selectbox(
    "Assign To",
    list(ENGINEERS.keys())
)

description = st.text_area(
    "Description"
)

if st.button("Submit Query"):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM queries"
    )

    count = cursor.fetchone()[0] + 1

    query_id = f"UKCT-{count:04d}"

    cursor.execute("""
    INSERT INTO queries
    (
        query_id,
        project_name,
        category,
        priority,
        description,
        assigned_to,
        status,
        created_date
    )
    VALUES (?,?,?,?,?,?,?,?)
    """,
    (
        query_id,
        project_name,
        category,
        priority,
        description,
        assigned_to,
        "Open",
        datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )
    ))

    conn.commit()
    conn.close()

    st.success(
        f"{query_id} Created Successfully"
    )
