import streamlit as st
from database.database import init_db

st.set_page_config(
    page_title="UKCT Query Tracker",
    layout="wide"
)

init_db()

st.title("🏗 UKCT Engineering Query Tracker")

st.markdown("""
### Welcome

Use the left navigation panel.

Available Modules:

- Submit Query
- Open Queries
- My Queries
- Knowledge Base
- Dashboard
""")
