import streamlit as st
from database.database import get_connection
from datetime import datetime

from utils.email_utils import send_email
from utils.email_config import ENGINEERS

st.title("📝 Submit Engineering Query")

# =====================================
# Dropdown Data
# =====================================

engineers = list(ENGINEERS.keys())

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
    "Pipeline Design",
    "Commissioning",
    "Civil Interface",
    "Electrical Interface",
    "Client Comment",
    "Site Query",
    "General"
]

# =====================================
# Form Fields
# =====================================

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

# =====================================
# Submit Button
# =====================================

if st.button("Submit Query"):

    if project_name.strip() == "":
        st.error("Please enter Project Name")
        st.stop()

    conn = get_connection()
    cursor = conn.cursor()

    # Generate Query Number
    cursor.execute(
        "SELECT COUNT(*) FROM queries"
    )

    count = cursor.fetchone()[0] + 1

    query_id = f"UKCT-{count:04d}"

    created_date = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    assigned_email = ENGINEERS[assigned_to]

    # Save Query
    cursor.execute(
        """
        INSERT INTO queries (
            query_id,
            project_name,
            project_type,
            category,
            priority,
            description,
            assigned_to,
            assigned_email,
            status,
            created_date
        )
        VALUES (?,?,?,?,?,?,?,?,?,?)
        """,
        (
            query_id,
            project_name,
            project_type,
            category,
            priority,
            description,
            assigned_to,
            assigned_email,
            "Assigned",
            created_date
        )
    )

    conn.commit()
    conn.close()

    # ============================
    # Send Email Notification
    # ============================

    try:

        subject = f"[UKCT] New Query Assigned - {query_id}"

        body = f"""
Hello {assigned_to},

A new engineering query has been assigned to you.

Query ID: {query_id}

Project Name: {project_name}

Project Type: {project_type}

Category: {category}

Priority: {priority}

Description:
{description}

Please review and update the query.

Regards,
UKCT Engineering Query Tracker
"""

        send_email(
            assigned_email,
            subject,
            body
        )

        st.success(
            f"{query_id} created successfully. Email sent to {assigned_to}."
        )

    except Exception as e:

        st.warning(
            f"{query_id} created successfully but email failed."
        )

        st.error(str(e))
