import streamlit as st

st.title("Local DBMS")

st.sidebar.markdown("<h2 style='text-align: center; color: #FF5733'>Dynamic DBMS</h2>", unsafe_allow_html=True)
databbase = st.sidebar.selectbox("Select Database", ["Create Database", "Connect to Database", "Delete Database"])

if databbase == "Create Database":
    st.subheader("Create Database")
    db_name = st.text_input("Database Name")
    if st.button("Create"):
        try:
            conn = sqlite3.connect(f"{db_name}.db")
            st.success("Database created successfully.")
        except Exception as e:
            st.error(f"Error creating database: {str(e)}")
    