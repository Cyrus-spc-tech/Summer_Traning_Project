# 📦 Local Database Management System

## 🎯 Project Overview

This project is a **comprehensive database management system** built with Python and Streamlit that provides an intuitive graphical user interface for managing both **User** and **Product** databases. The system leverages SQLite for local data storage and offers powerful CRUD operations (Create, Read, Update, Delete) along with advanced data visualization and analytics capabilities.

---

## 🌟 Key Features

### 👥 User Management System
- **Complete User Profile Management**: Store and manage user information including name, email, password, phone number, address, and date of birth
- **User Status Tracking**: Monitor user status (active/inactive/deleted)
- **Timestamp Tracking**: Automatic tracking of creation and update timestamps
- **Secure Data Handling**: Password protection and secure data storage

### 📦 Product Management System
- **Inventory Management**: Track product name, price, quantity, stock ID, and detailed descriptions
- **Stock Monitoring**: Real-time inventory tracking with stock IDs
- **Product Status Management**: Monitor product availability and status
- **Comprehensive Product Details**: Store detailed product descriptions and metadata

### 📊 Data Visualization & Analytics
- **Multiple Chart Types**: 
  - Histogram for distribution analysis
  - Bar charts for comparative analysis
  - Pie charts for proportion visualization
- **Interactive Visualizations**: Built with Plotly for dynamic, interactive charts
- **Summary Statistics**: Comprehensive statistical analysis of your data
- **Visual Analytics**: Distribution plots and trend analysis

### 🔧 Database Operations
- **CRUD Operations**: Full Create, Read, Update, Delete functionality
- **Table Structure Inspection**: View database schema and column information
- **ID-Based Retrieval**: Fetch specific records by ID
- **Bulk Data Display**: View all records in a clean, tabular format

---

## 🏗️ Project Architecture

### Database Layer
```
📁 Static/
├── 📄 userdb.py          # User database class with CRUD operations
├── 📄 productdb.py       # Product database class with CRUD operations
├── 🗄️ Users.db           # SQLite database for user data
└── 🗄️ Product.db         # SQLite database for product data
```

### Presentation Layer
```
📁 Static/
├── 📄 userdbgui.py       # Streamlit GUI for user management
└── 📄 productdbgui.py    # Streamlit GUI for product management
```

---

## 💾 Database Schema

### User Table Structure
| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | Primary key (auto-increment) |
| `name` | TEXT | User's full name |
| `email` | TEXT | User's email address |
| `password` | TEXT | User's password |
| `phone_number` | TEXT | Contact number |
| `address` | TEXT | Physical address |
| `date_of_birth` | DATE | Date of birth |
| `created_at` | TIMESTAMP | Record creation time |
| `updated_at` | TIMESTAMP | Last update time |
| `status` | TEXT | User status (active/inactive/deleted) |

### Product Table Structure
| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | Primary key (auto-increment) |
| `name` | TEXT | Product name |
| `price` | TEXT | Product price |
| `quantity` | TEXT | Available quantity |
| `stockid` | TEXT | Unique stock identifier |
| `description` | TEXT | Product description |
| `created_at` | TIMESTAMP | Record creation time |
| `updated_at` | TIMESTAMP | Last update time |
| `status` | TEXT | Product status |

---

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.7 or higher
```

### Required Libraries
```bash
pip install streamlit
pip install pandas
pip install plotly
pip install sqlite3  # Usually comes pre-installed with Python
```

### Installation Steps

1. **Clone or Download the Project**
   ```bash
   cd d:\REPO\Summer_Traning_Project\MINOR_2(LocalDB)\Static
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the User Management System**
   ```bash
   streamlit run userdbgui.py
   ```

4. **Run the Product Management System**
   ```bash
   streamlit run productdbgui.py
   ```

---

## 📖 How to Use

### User Management Interface

1. **Insert New User**
   - Navigate to "Insert User" from the sidebar menu
   - Fill in all required fields (name, email, password)
   - Optional fields: phone number, address, date of birth
   - Click "Insert" to save the user

2. **View All Users**
   - Select "Fetch All Users" from the menu
   - Browse all users in a clean table format
   - View all user details including timestamps and status

3. **Update User Information**
   - Choose "Update User" from the menu
   - Enter the user ID you want to update
   - Modify the fields as needed
   - Click "Update" to save changes

4. **Delete User**
   - Select "Delete User" from the menu
   - View the current user list
   - Enter the ID of the user to delete
   - Confirm deletion

5. **Get User by ID**
   - Choose "Get User by ID"
   - Enter the specific user ID
   - View detailed user information

### Product Management Interface

1. **Insert New Product**
   - Navigate to "Insert Product"
   - Fill in product details (name, price, quantity, stock ID, description)
   - Submit the form to add the product

2. **View All Products**
   - Select "Fetch All Products"
   - Browse the complete product inventory
   - View all product details in table format

3. **Update Product**
   - Choose "Update Product"
   - Enter the product ID
   - Modify product information
   - Save the changes

4. **Delete Product**
   - Select "Delete Product"
   - View current products
   - Enter product ID to delete
   - Confirm deletion

5. **Visualize Data**
   - Choose "Visualize Data"
   - Select visualization type (Histogram, Bar Chart, Pie Chart)
   - Choose X and Y axes
   - View interactive charts

6. **Analytics Dashboard**
   - Select "Analytics"
   - Choose between Summary Statistics or Visual Analytics
   - View comprehensive data analysis
   - Explore distribution plots and trends

---

## 🎨 User Interface Features

### Sidebar Navigation
- **Clean Menu System**: Easy-to-navigate sidebar with all features
- **Table Description**: Quick reference to database schema
- **Color-Coded Headers**: Visual distinction for better UX

### Interactive Forms
- **Form Validation**: Ensures all required fields are filled
- **Success/Warning Messages**: Clear feedback on operations
- **Pre-filled Update Forms**: Current values loaded automatically

### Data Display
- **Pandas DataFrames**: Clean, sortable table displays
- **Responsive Design**: Adapts to different screen sizes
- **Real-time Updates**: Immediate reflection of database changes

---

## 🔐 Security Features

- **Password Protection**: Secure password storage for users
- **Input Validation**: Prevents invalid data entry
- **Status Management**: Soft delete capability with status flags
- **Timestamp Auditing**: Track when records are created and modified

---

## 🛠️ Technical Implementation

### Object-Oriented Design
- **Database Classes**: Separate classes for User and Product databases
- **Encapsulation**: Private methods for table creation and management
- **Reusability**: Modular code structure for easy maintenance

### Automatic Table Management
- **Dynamic Schema Updates**: Automatically adds missing columns
- **Table Creation**: Creates tables if they don't exist
- **Migration Support**: Handles database schema evolution

### Error Handling
- **Graceful Degradation**: Handles missing data appropriately
- **User Feedback**: Clear error messages and warnings
- **Data Validation**: Ensures data integrity

---

## 📊 Visualization Capabilities

### Chart Types
1. **Histograms**: Distribution analysis of data
2. **Bar Charts**: Comparative analysis across categories
3. **Pie Charts**: Proportion and percentage visualization

### Analytics Features
1. **Summary Statistics**: Mean, median, standard deviation, etc.
2. **Distribution Plots**: Visual representation of data spread
3. **Interactive Charts**: Zoom, pan, and hover for details

---

## 🎓 Use Cases

### Business Applications
- **Inventory Management**: Track products and stock levels
- **Customer Database**: Manage customer information
- **Sales Analytics**: Analyze product performance

### Educational Projects
- **Database Learning**: Understand CRUD operations
- **GUI Development**: Learn Streamlit framework
- **Data Visualization**: Practice creating charts and graphs

### Personal Projects
- **Personal Inventory**: Track personal belongings
- **Contact Management**: Store contact information
- **Data Analysis**: Analyze personal data

---

## 🔄 Future Enhancements

### Potential Features
- [ ] User authentication and login system
- [ ] Export data to CSV/Excel
- [ ] Import data from external files
- [ ] Advanced search and filtering
- [ ] Multi-user support with roles and permissions
- [ ] Cloud database integration
- [ ] Mobile responsive design
- [ ] Email notifications
- [ ] Backup and restore functionality
- [ ] API endpoints for external integration

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: Database file not found
- **Solution**: The database files are created automatically on first run

**Issue**: Module not found error
- **Solution**: Install all required dependencies using pip

**Issue**: Port already in use
- **Solution**: Streamlit will automatically use a different port

**Issue**: Data not updating
- **Solution**: Refresh the page or rerun the Streamlit app

---

## 📝 Code Structure

### UserDatabase Class (`userdb.py`)
```python
- __init__(): Initialize database connection
- _create_table(): Create user table with schema
- insert(): Add new user
- fetch(): Retrieve all users
- update(): Modify user information
- delete(): Remove user
- get_user_by_id(): Fetch specific user
- describe(): View table structure
```

### ProductDatabase Class (`productdb.py`)
```python
- __init__(): Initialize database connection
- _create_table(): Create product table with schema
- insert(): Add new product
- fetch(): Retrieve all products
- update(): Modify product information
- delete(): Remove product
- get_product_by_id(): Fetch specific product
- describe(): View table structure
```

---

## 🤝 Contributing

This project was developed as part of a summer training program. Contributions and suggestions are welcome!

---

## 📄 License

This project is part of an educational training program.

---

## 👨‍💻 Developer Information

**Project Type**: Summer Training Project - Minor Project 2  
**Technology Stack**: Python, Streamlit, SQLite, Pandas, Plotly  
**Database**: Local SQLite Database  
**GUI Framework**: Streamlit  

---

## 📞 Support

For questions or issues, please refer to the code documentation or contact the development team.

---

## 🎤 Presentation Tips

When presenting this project, emphasize:

1. **Problem Statement**: Need for simple, local database management
2. **Solution**: User-friendly GUI with powerful features
3. **Technology Choices**: Why Streamlit, SQLite, and Python
4. **Key Features**: CRUD operations, visualization, analytics
5. **Demo**: Live demonstration of adding, updating, and visualizing data
6. **Future Scope**: Potential enhancements and scalability
7. **Learning Outcomes**: Skills gained during development

---

## 🌟 Project Highlights

✅ **Easy to Use**: Intuitive interface for non-technical users  
✅ **Comprehensive**: Full CRUD operations for both users and products  
✅ **Visual**: Built-in data visualization and analytics  
✅ **Scalable**: Modular design for easy expansion  
✅ **Local**: No internet required, complete data privacy  
✅ **Fast**: SQLite provides quick data access  
✅ **Modern**: Built with current Python best practices  

---

**Built with ❤️ using Python and Streamlit**
