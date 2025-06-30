import streamlit as st 
from helper import DatabaseHelper

st.page_config(page_title="Database Management", page_icon=":package:", layout="wide")
db_helper = DatabaseHelper()