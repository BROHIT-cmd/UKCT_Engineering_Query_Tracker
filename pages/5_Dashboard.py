import streamlit as st
import pandas as pd
import plotly.express as px

from query_db import get_connection

st.title("📊 Dashboard")

conn = get_connection()

df = pd.read_sql_query(
    "SELECT * FROM queries",
    conn
)

if len(df) == 0:

    st.warning("No Data Available")

else:

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Queries",
        len(df)
    )

    col2.metric(
        "Open Queries",
        len(
            df[df["status"] == "Open"]
        )
    )

    col3.metric(
        "Resolved",
        len(
            df[df["status"] == "Resolved"]
        )
    )

    chart_df = (
        df.groupby("assigned_to")
        .size()
        .reset_index(name="Count")
    )

    fig = px.bar(
        chart_df,
        x="assigned_to",
        y="Count",
        title="Queries by Engineer"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

conn.close()
