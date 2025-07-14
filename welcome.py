import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to the ILUTE Data Website! 👋")

st.sidebar.success("What would you like to look at?")

st.markdown(
    """
    This is a simple Streamlit app that provides an overview of the datasets used in the ILUTE Research Group.
    You can filter the datasets by year, geographical scope, and tags.
"""
)
