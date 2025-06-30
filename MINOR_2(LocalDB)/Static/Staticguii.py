import streamlit as st
import pandas as pd
import plotly.express as px
from staticdatab import UserDatabase

st.set_page_config(page_title="Local DB", page_icon=":package:")
db = UserDatabase()

st.title("Local DB")

menu = ["Describe Table", "Fetch All Users", "Insert User", "Delete User", "Update User", "Get User by ID", "Visualize Data", "Analytics"]
choice = st.sidebar.selectbox("Menu", menu)
st.sidebar.subheader("Table Description")
st.sidebar.code('''
table user 
[
id 
name 
email 
password 
phone_number 
address 
date_of_birth 
created_at 
updated_at 
status 
]
''')

if choice == "Insert User":
    st.subheader("Insert New User")
    with st.form(key='insert_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        phone_number = st.text_input("Phone Number")
        address = st.text_area("Address")
        date_of_birth = st.date_input("Date of Birth")
        
        if st.form_submit_button("Insert"):
            if name and email and password:
                db.insert(name, email, password, phone_number, address, date_of_birth)
                st.success("Data inserted successfully.")
            else:
                st.warning("Please fill all required fields.")




elif choice == "Fetch All Users":
    st.subheader("All Users")
    data = db.fetch()
    if data:
        # Get the actual column names from database
        df = pd.DataFrame(data[0], columns=data[1])
        st.dataframe(df)
    else:
        st.info("No users found.")



elif choice == "Describe Table":
    st.subheader("Table Structure")
    data = db.describe()
    st.dataframe(data)




elif choice == "Delete User":
    data = db.fetch()
    if data:
        # Get the actual column names from database
        df = pd.DataFrame(data[0], columns=data[1])
        st.dataframe(df)
    st.subheader("Delete User")
    id = st.number_input("Enter ID to delete", min_value=1, step=1)
    if st.button("Delete"):
        db.delete(id)
        st.success("Data deleted successfully.")






elif choice == "Update User":
    st.subheader("Update User")
    id = st.number_input("User ID", min_value=1)
    if id:
        data = db.fetch()
        df = pd.DataFrame(data[0], columns=data[1])
        user_data = df[df['ID'] == id]
        
        if not user_data.empty:
            with st.form(key='update_form'):
                name = st.text_input("Name", value=user_data['Name'].iloc[0])
                email = st.text_input("Email", value=user_data['Email'].iloc[0])
                password = st.text_input("Password", type="password")
                phone_number = st.text_input("Phone Number", value=user_data['Phone_Number'].iloc[0])
                address = st.text_area("Address", value=user_data['Address'].iloc[0])
                date_of_birth = st.date_input("Date of Birth", value=pd.to_datetime(user_data['Date_of_Birth'].iloc[0]))
                status = st.selectbox("Status", ['active', 'inactive', 'deleted'], index=['active', 'inactive', 'deleted'].index(user_data['Status'].iloc[0]))
                
                if st.form_submit_button("Update"):
                    db.update(id, name, email, password, phone_number, address, date_of_birth, status)
                    st.success("Data updated successfully.")
        else:
            st.warning("User not found.")






elif choice == "Get User by ID":
    st.subheader("Get User by ID")
    id = st.number_input("Enter ID to fetch user", min_value=1, step=1)
    if st.button("Fetch User"):
        user = db.get_user_by_id(id)
        if user:
            st.write(user)
        else:
            st.warning("User not found.")








elif choice == "Visualize Data":
    st.subheader("Visualize Data")
    data = db.fetch()
    if data:
        df = pd.DataFrame(data[0], columns=data[1])
        st.dataframe(df)
        
        st.subheader("Data Visualization Options")
        viz_type = st.selectbox("Select Visualization Type", ['Histogram', 'Bar Chart', 'Pie Chart'])
        
        x_axis = st.selectbox("Select X Axis", df.columns)
        y_axis = st.selectbox("Select Y Axis", df.columns)
        
        if viz_type == 'Histogram':
            st.subheader("Histogram")
            st.bar_chart(df[x_axis].value_counts().sort_index())
            
        elif viz_type == 'Bar Chart':
            st.subheader("Bar Chart")
            st.bar_chart(df.groupby(x_axis)[y_axis].sum())
            
        elif viz_type == 'Pie Chart':
            st.subheader("Pie Chart")
            st.pie_chart(df[y_axis].value_counts())
            
    else:
        st.info("No data to visualize.")

elif choice == "Analytics":
    st.subheader("Analytics")
    data = db.fetch()
    if data:
        df = pd.DataFrame(data[0], columns=data[1])
        st.dataframe(df)
        
        st.subheader("Analytics Options")
        analytics_type = st.selectbox("Select Analytics Type", ['Summary Statistics', 'Visual Analytics'])
        
        if analytics_type == "Summary Statistics":
            st.subheader("Summary Statistics")
            st.write(df.describe())
            

            
        elif analytics_type == "Visual Analytics":
            st.subheader("Visual Analytics")
            
            # Distribution plots
            numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
            if len(numeric_cols) > 0:
                st.subheader("Distribution Plots")
                for col in numeric_cols:
                    fig = px.histogram(df, x=col, title=f'Distribution of {col}')
                    st.plotly_chart(fig)
            
            # Box plots
            if len(numeric_cols) > 0:
                st.subheader("Box Plots")
                for col in numeric_cols:
                    fig = px.box(df, y=col, title=f'Box Plot of {col}')
                    st.plotly_chart(fig)
            
            # Scatter plots
            if len(numeric_cols) > 1:
                st.subheader("Scatter Plots")
                for i in range(len(numeric_cols)):
                    for j in range(i+1, len(numeric_cols)):
                        fig = px.scatter(df, x=numeric_cols[i], y=numeric_cols[j], 
                                       title=f'Scatter Plot: {numeric_cols[i]} vs {numeric_cols[j]}')
                        st.plotly_chart(fig)
            
            # Bar charts for categorical data
            categorical_cols = df.select_dtypes(include=['object']).columns
            if len(categorical_cols) > 0:
                st.subheader("Categorical Data Distribution")
                for col in categorical_cols:
                    fig = px.bar(df[col].value_counts(), 
                                title=f'Distribution of {col}',
                                labels={'value': 'Count', 'index': col})
                    st.plotly_chart(fig)
            
    else:
        st.info("No data to analyze.")
