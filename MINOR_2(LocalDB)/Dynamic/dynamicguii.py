import streamlit as st
import pandas as pd
from dynamicdatab import DatabaseManager

st.set_page_config(page_title="Dynamic DB Manager", page_icon=":database:")
db_manager = DatabaseManager()

st.title("Dynamic Database Manager")

# Sidebar for database operations
with st.sidebar:
    st.header("Database Operations")
    
    # Database Management
    db_operation = st.selectbox("Database Operation", ["Create Database", "Select Database", "Delete Database"])
    
    if db_operation == "Create Database":
        db_name = st.text_input("Database Name")
        if st.button("Create Database"):
            success, msg = db_manager.create_database(db_name)
            st.sidebar.info(msg)
            
    elif db_operation == "Select Database":
        available_dbs = list(db_manager.databases.keys())
        if available_dbs:
            selected_db = st.selectbox("Select Database", available_dbs)
            if st.button("Select Database"):
                success, msg = db_manager.select_database(selected_db)
                st.sidebar.info(msg)
        else:
            st.sidebar.warning("No databases available. Create one first.")
            
    elif db_operation == "Delete Database":
        available_dbs = list(db_manager.databases.keys())
        if available_dbs:
            db_to_delete = st.selectbox("Delete Database", available_dbs)
            if st.button("Delete Database"):
                success, msg = db_manager.delete_database(db_to_delete)
                st.sidebar.info(msg)
        else:
            st.sidebar.warning("No databases available.")

# Main content area
if db_manager.selected_db:
    st.header(f"Current Database: {db_manager.selected_db}")
    
    # Table Operations
    table_operation = st.selectbox("Table Operation", ["Create Table", "Select Table", "Delete Table", "View Tables"])
    
    if table_operation == "Create Table":
        with st.form("create_table_form"):
            table_name = st.text_input("Table Name")
            
            st.write("Add Columns")
            columns = {}
            for i in range(5):  # Allow up to 5 columns
                col_name = st.text_input(f"Column {i+1} Name", key=f"col_name_{i}")
                col_type = st.selectbox(f"Column {i+1} Type", 
                                      ['TEXT', 'INTEGER', 'REAL', 'DATE', 'TIMESTAMP'],
                                      key=f"col_type_{i}")
                if col_name:
                    columns[col_name] = col_type
            
            if st.form_submit_button("Create Table"):
                if not table_name:
                    st.warning("Please enter a table name")
                elif not columns:
                    st.warning("Please add at least one column")
                else:
                    success, msg = db_manager.create_table(table_name, columns)
                    st.info(msg)
                    
    elif table_operation == "Select Table":
        tables, _ = db_manager.get_tables()
        if tables:
            selected_table = st.selectbox("Select Table", tables)
            if st.button("View Table"):
                df, _ = db_manager.fetch_data(selected_table)
                st.dataframe(df)
        else:
            st.warning("No tables available. Create one first.")
            
    elif table_operation == "Delete Table":
        tables, _ = db_manager.get_tables()
        if tables:
            table_to_delete = st.selectbox("Delete Table", tables)
            if st.button("Delete Table"):
                success, msg = db_manager.delete_table(table_to_delete)
                st.info(msg)
        else:
            st.warning("No tables available.")
            
    elif table_operation == "View Tables":
        tables, _ = db_manager.get_tables()
        if tables:
            st.write("Available Tables:")
            for table in tables:
                st.write(f"- {table}")
                if st.button(f"View {table} Details", key=f"view_{table}"):
                    columns, _ = db_manager.get_columns(table)
                    st.write("Columns:")
                    for col in columns:
                        st.write(f"- {col[1]} ({col[2]})")
        else:
            st.warning("No tables available.")

    # Data Operations
    st.header("Data Operations")
    
    tables, _ = db_manager.get_tables()
    if tables:
        selected_table = st.selectbox("Select Table for Data Operations", tables)
        
        # Insert Data
        if st.button("Insert Data"):
            columns, _ = db_manager.get_columns(selected_table)
            with st.form("insert_data_form"):
                data = {}
                for col in columns:
                    col_name = col[1]
                    col_type = col[2]
                    if col_type == 'TEXT':
                        data[col_name] = st.text_input(f"{col_name}")
                    elif col_type == 'INTEGER':
                        data[col_name] = st.number_input(f"{col_name}", step=1)
                    elif col_type == 'REAL':
                        data[col_name] = st.number_input(f"{col_name}", step=0.01)
                    elif col_type == 'DATE':
                        data[col_name] = st.date_input(f"{col_name}")
                    elif col_type == 'TIMESTAMP':
                        data[col_name] = st.date_input(f"{col_name}")
                
                if st.form_submit_button("Insert Data"):
                    success, msg = db_manager.insert_data(selected_table, data)
                    st.info(msg)
                    
        # View Data
        if st.button("View Data"):
            df, _ = db_manager.fetch_data(selected_table)
            st.dataframe(df)
            
            # Add visualization options
            if not df.empty:
                st.subheader("Data Visualization")
                viz_type = st.selectbox("Select Visualization Type", 
                                      ['Histogram', 'Bar Chart', 'Scatter Plot'])
                
                if viz_type == 'Histogram':
                    x_axis = st.selectbox("Select X Axis", df.columns)
                    st.bar_chart(df[x_axis].value_counts())
                
                elif viz_type == 'Bar Chart':
                    x_axis = st.selectbox("Select X Axis", df.columns)
                    y_axis = st.selectbox("Select Y Axis", df.columns)
                    st.bar_chart(df.groupby(x_axis)[y_axis].sum())
                
                elif viz_type == 'Scatter Plot':
                    x_axis = st.selectbox("Select X Axis", df.columns)
                    y_axis = st.selectbox("Select Y Axis", df.columns)
                    st.line_chart(df[[x_axis, y_axis]])
    else:
        st.warning("No tables available. Create one first.")