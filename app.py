import streamlit as st
from query_db import create_table

create_table()

st.set_page_config(
    page_title="UKCT Engineering Query Tracker",
    layout="wide"
)

st.sidebar.image(
    "ukct_logo.png",
    width=180
)

st.sidebar.markdown(
    "### UKCT Team"
)

st.title(
    "🏗 UKCT Engineering Query Tracker"
)

st.write("""
Welcome to the UKCT Engineering Query Tracker.

Use the left navigation menu:

✅ Submit Query

✅ Open Queries

✅ My Queries

✅ Dashboard
""")
