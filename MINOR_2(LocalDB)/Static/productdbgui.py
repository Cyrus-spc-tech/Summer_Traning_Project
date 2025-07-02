import streamlit as st
import pandas as pd
import plotly.express as px
from productdb import ProductDatabase   



st.set_page_config(page_title="Product Database", page_icon=":package:")

st.title("Product Database")
db=ProductDatabase()

st.sidebar.markdown("<h2 style='text-align: center; color: #FF5733'>Product Database</h2>", unsafe_allow_html=True)
menu=["Insert Product","Fetch All Products","Describe Table","Delete Product","Update Product","Get Product by ID","Vizulize Data","Analytics"]
choice=st.sidebar.selectbox("Menu",menu)
st.sidebar.subheader("Table Description")
st.sidebar.code('''
table Product 
[
id 
name 
price 
quantity 
stockid 
description 
created_at 
updated_at 
status 
]
''')

if choice=="Insert Product":
    st.subheader("Insert New Product")
    with st.form(key='insert_form'):
        name = st.text_input("Name")
        price = st.text_input("Price")
        quantity = st.text_input("Quantity")
        stockid = st.text_input("Stock ID")
        description = st.text_area("Description")
        
        if st.form_submit_button("Insert"):
            if name and price and quantity and stockid and description:
                db.insert(name, price, quantity, stockid, description)
                st.success("Data inserted successfully.")
            else:
                st.warning("Please fill all required fields.")







elif choice=="Fetch All Products":
    st.subheader("All Products")
    data = db.fetch()
    if data:
        # Get the actual column names from database
        df = pd.DataFrame(data[0], columns=data[1])
        st.dataframe(df)
    else:
        st.info("No products found.")








elif choice=="Describe Table":
    st.subheader("Table Structure")
    data = db.describe()
    st.dataframe(data)









elif choice=="Delete Product":
    data = db.fetch()
    if data:
        df = pd.DataFrame(data[0], columns=data[1])
        st.dataframe(df)
    st.subheader("Delete Product")
    id = st.number_input("Enter ID to delete", min_value=1, step=1)
    if st.button("Delete"):
        db.delete(id)
        st.success("Data deleted successfully.")

    





elif choice  == "Update Product":
    data = db.fetch()
    if data:
        df = pd.DataFrame(data[0], columns=data[1])
        st.dataframe(df)
    st.subheader("Update Product")
    id = st.number_input("User ID", min_value=1)
    if id:
        data = db.fetch()
        df = pd.DataFrame(data[0], columns=data[1])
        user_data = df[df['id'] == id]
        
        if not user_data.empty:
            with st.form(key='update_form'):
                name = st.text_input("Name", value=user_data['Name'].iloc[0])
                price = st.text_input("Price", value=user_data['Price'].iloc[0])
                quantity = st.text_input("Quantity", value=user_data['Quantity'].iloc[0])
                stockid = st.text_input("Stock ID", value=user_data['StockID'].iloc[0])
                description = st.text_area("Description", value=user_data['Description'].iloc[0])
                
                if st.form_submit_button("Update"):
                    db.update(id, name, price, quantity, stockid, description)
                    st.success("Data updated successfully.")
        else:
            st.warning("User not found.")
            







elif choice == "Get Product by ID":
    st.subheader("Get Product by ID")
    id = st.number_input("Enter ID to fetch product", min_value=1, step=1)
    if st.button("Fetch Product"):
        product = db.get_product_by_id(id)
        if product:
            st.write(product)
        else:
            st.warning("Product not found.")






elif choice == "Vizulize Data":
    st.subheader("Vizulize Data")
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
            fig = px.pie(df, names=x_axis, values=y_axis, title=f'{y_axis} Distribution by {x_axis}')
            st.plotly_chart(fig)
            
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
            
            numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
            if len(numeric_cols) > 0:
                st.subheader("Distribution Plots")
                for col in numeric_cols:
                    fig = px.histogram(df, x=col, title=f'Distribution of {col}')
                    st.plotly_chart(fig)
            
    else:
        st.info("No data to analyze.")
