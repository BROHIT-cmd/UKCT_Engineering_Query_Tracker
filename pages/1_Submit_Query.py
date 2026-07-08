import streamlit as st
from database.database import get_connection
from datetime import datetime

st.title("📝 Submit Query")

engineers = [
    "Rohit",
    "Engineer A",
    "Engineer B",
    "Engineer C",
    "Engineer D"
]

project_types = [
    "Infrastructure PS",
    "TOPS Station",
    "Foul Water PS",
    "Surface Water PS"
]

categories = [
    "Hydraulics",
    "Pump Selection",
    "Mechanical Design",
    "Wet Well Design",
    "Valve Selection",
    "Commissioning",
    "General"
]

project_name = st.text_input("Project Name")

project_type = st.selectbox(
    "Project Type",
    project_types
)

category = st.selectbox(
    "Category",
    categories
)

priority = st.selectbox(
    "Priority",
    ["High", "Medium", "Low"]
)

assigned_to = st.selectbox(
    "Assign To",
    engineers
)

description = st.text_area(
    "Description"
)

if st.button("Submit"):

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
        project_type,
        category,
        priority,
        description,
        assigned_to,
        status,
        created_date
    )
    VALUES (?,?,?,?,?,?,?,?,?)
    """,
    (
        query_id,
        project_name,
        project_type,
        category,
        priority,
        description,
        assigned_to,
        "Assigned",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()

    st.success(
        f"{query_id} Created Successfully"
    )
