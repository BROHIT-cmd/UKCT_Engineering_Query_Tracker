import streamlit as st
import pandas as pd
import plotly.express as px
from database.database import get_connection

st.title("📊 Dashboard")

conn = get_connection()

df = pd.read_sql_query(
    "SELECT * FROM queries",
    conn
)

if len(df) == 0:

    st.warning("No Data Found")

else:

    col1, col2, col3 = st.columns(3)

    total_queries = len(df)

    open_queries = len(
        df[df["status"] != "Closed"]
    )

    resolved_queries = len(
        df[df["status"] == "Resolved"]
    )

    col1.metric(
        "Total",
        total_queries
    )

    col2.metric(
        "Open",
        open_queries
    )

    col3.metric(
        "Resolved",
        resolved_queries
    )

    st.subheader(
        "Queries by Engineer"
    )

    engineer_df = (
        df.groupby("assigned_to")
        .size()
        .reset_index(name="Count")
    )

    fig1 = px.bar(
        engineer_df,
        x="assigned_to",
        y="Count"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.subheader(
        "Queries by Category"
    )

    category_df = (
        df.groupby("category")
        .size()
        .reset_index(name="Count")
    )

    fig2 = px.pie(
        category_df,
        names="category",
        values="Count"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )
