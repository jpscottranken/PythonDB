import sqlite3
"""
    To import the modules below in main.py, I ensured 
    that Python recognizes the modules folder and its 
    subfolders as packages by adding an empty
    __init__.py file to each folder (including modules)
    This file marks the directories as Python packages,
    as shown below:

root/
│
├── main.py
└── modules/
	├── __init__.py
    ├── categories/
		├── __init__.py
    │   └── categoriesCRUD.py
    ├── customers/
		├── __init__.py
    │   └── customersCRUD.py
    ├── employees/
		├── __init__.py
    │   └── employeesCRUD.py
    ├── orderDetails/
		├── __init__.py
    │   └── orderDetailsCRUD.py
    ├── orders/
		├── __init__.py
    │   └── ordersCRUD.py
    ├── products/
		├── __init__.py
    │   └── productsCRUD.py
    ├── productVendors/
		├── __init__.py
    │   └── productVendorsCRUD.py
    └── vendors/
		├── __init__.py
        └── vendorsCRUD.py

    Next, import in main.py i.e., you can import 
    the specific modules in your main.py by referencing 
    the folder path to each module.

# Import the CRUD modules
# For example, Import all methods in the categories module
from modules.categories.categoriesCRUD import *

However, I replaced the * imports with specific function 
imports to avoid polluting the namespace. As shown in
lines 52 - 98 below.
"""
# Import the Categories CRUD modules
from modules.categories.categoriesCRUD import createCategory
from modules.categories.categoriesCRUD import readCategories
from modules.categories.categoriesCRUD import updateCategory
from modules.categories.categoriesCRUD import deleteCategory

# Import the Customers CRUD modules
from modules.customers.customersCRUD import createCustomer
from modules.customers.customersCRUD import readCustomers
from modules.customers.customersCRUD import updateCustomer
from modules.customers.customersCRUD import deleteCustomer

# Import the Employees CRUD modules
from modules.employees.employeesCRUD import createEmployee
from modules.employees.employeesCRUD import readEmployees
from modules.employees.employeesCRUD import updateEmployee
from modules.employees.employeesCRUD import deleteEmployee

# Import the OrderDetails CRUD modules
from modules.orderDetails.orderDetailsCRUD import createOrderDetail
from modules.orderDetails.orderDetailsCRUD import readOrderDetails
from modules.orderDetails.orderDetailsCRUD import updateOrderDetail
from modules.orderDetails.orderDetailsCRUD import deleteOrderDetail

# Import the Orders CRUD modules
from modules.orders.ordersCRUD import createOrder
from modules.orders.ordersCRUD import readOrders
from modules.orders.ordersCRUD import updateOrder
from modules.orders.ordersCRUD import deleteOrder

# Import the Products CRUD modules
from modules.products.productsCRUD import createProduct
from modules.products.productsCRUD import readProducts
from modules.products.productsCRUD import updateProduct
from modules.products.productsCRUD import deleteProduct

# Import the ProductVendors CRUD modules
from modules.productVendors.productVendorsCRUD import createProductVendor
from modules.productVendors.productVendorsCRUD import readProductVendors
from modules.productVendors.productVendorsCRUD import updateProductVendor
from modules.productVendors.productVendorsCRUD import deleteProductVendor

# Import the Vendors CRUD modules
from modules.vendors.vendorsCRUD import createVendor
from modules.vendors.vendorsCRUD import readVendors
from modules.vendors.vendorsCRUD import updateVendor
from modules.vendors.vendorsCRUD import deleteVendor

# Connect to SQLite3 database
def connectDB():
  return sqlite3.connect("SalesOrders.db")

# Function to display the main menu()
def displayMainMenu():
  print("\nSalesOrders DB Main Menu:")
  print("1. Categories")
  print("2. Customers")
  print("3. Employees")
  print("4. OrderDetails")
  print("5. Orders")
  print("6. Products")
  print("7. ProductVendors")
  print("8. Vendors")
  print("9. Exit Program")

  # Choose an option
  choice = input("Select a table option (1 - 8) or 9 to Exit: ")
  return choice

# Function to display main CRUD menu
def displayCRUDMenu():
  print("\nCRUD Operations Menu: ")
  print("1. Create")
  print("2. Read")
  print("3. Update")
  print("4. Delete")
  print("5. Return to the Main Menu")

  # Choose an option
  choice = input("Select An Operation (1 - 4) Or 5 To Return To Main Menu: ")
  return choice

# Function to display CRUD menu for each table
def handleCRUD(conn, cursor, tableName):
  while True:
    operation = displayCRUDMenu()

    if (operation == "1"):      # Create
      if (tableName == "Categories"):
        createCategory(cursor)
      elif (tableName == "Customers"):
        createCustomer(cursor)
      elif (tableName == "Employees"):
        createEmployee(cursor)
      elif (tableName == "OrderDetails"):
        createOrderDetail(cursor)
      elif (tableName == "Orders"):
        createOrder(cursor)
      elif (tableName == "Products"):
        createProduct(cursor)
      elif (tableName == "ProductVendors"):
        createProductVendor(cursor)
      elif (tableName == "Vendors"):
        createVendor(cursor)
    elif (operation == "2"):      # Read
      if (tableName == "Categories"):
        readCategories(cursor)
      elif (tableName == "Customers"):
        readCustomers(cursor)
      elif (tableName == "Employees"):
        readEmployees(cursor)
      elif (tableName == "OrderDetails"):
        readOrderDetails(cursor)
      elif (tableName == "Orders"):
        readOrders(cursor)
      elif (tableName == "Products"):
        readProducts(cursor)
      elif (tableName == "ProductVendors"):
        readProductVendors(cursor)
      elif (tableName == "Vendors"):
        readVendors(cursor)
    elif (operation == "3"):      # Update
      if (tableName == "Categories"):
        updateCategory(cursor)
      elif (tableName == "Customers"):
        updateCustomer(cursor)
      elif (tableName == "Employees"):
        updateEmployee(cursor)
      elif (tableName == "OrderDetails"):
        updateOrderDetail(cursor)
      elif (tableName == "Orders"):
        updateOrder(cursor)
      elif (tableName == "Products"):
        updateProduct(cursor)
      elif (tableName == "ProductVendors"):
        updateProductVendor(cursor)
      elif (tableName == "Vendors"):
        updateVendor(cursor)
    elif (operation == "4"):      # Delete
      if (tableName == "Categories"):
        deleteCategory(cursor)
      elif (tableName == "Customers"):
        deleteCustomer(cursor)
      elif (tableName == "Employees"):
        deleteEmployee(cursor)
      elif (tableName == "OrderDetails"):
        deleteOrderDetail(cursor)
      elif (tableName == "Orders"):
        deleteOrder(cursor)
      elif (tableName == "Products"):
        deleteProduct(cursor)
      elif (tableName == "ProductVendors"):
        deleteProductVendor(cursor)
      elif (tableName == "Vendors"):
        deleteVendor(cursor)
    elif (operation == "5"):   # Go back to main menu
      break
    else:
      print("Invalid Choice. Please Try Again.")
      return
    
    conn.commit()             # Commit changes to the SalesOrders DB

def main():
  # Establish connection to SalesOrders DB
  conn   = connectDB()

  # Create cursor to perform database operations
  cursor = conn.cursor()
 
  while True:
    tableChoice = displayMainMenu()

    if (tableChoice == "1"):        # Categories table
      handleCRUD(conn, cursor, "Categories")
    elif (tableChoice == "2"):      # Customers table
      handleCRUD(conn, cursor, "Customers")
    elif (tableChoice == "3"):      # Employees table
      handleCRUD(conn, cursor, "Employees")
    elif (tableChoice == "4"):      # OrderDetails table
      handleCRUD(conn, cursor, "OrderDetails")
    elif (tableChoice == "5"):      # Orders table
      handleCRUD(conn, cursor, "Orders")
    elif (tableChoice == "6"):      # Products table
      handleCRUD(conn, cursor, "Products")
    elif (tableChoice == "7"):      # ProductVendors table
      handleCRUD(conn, cursor, "ProductVendors")
    elif (tableChoice == "8"):      # Vendors table
      handleCRUD(conn, cursor, "Vendors")
    elif (tableChoice == "9"):      # Exit Program
      print("Exiting Program Now.")
      cursor.close()
      break
    else:
      print("Invalid Choice. Please Try Again.")
      return
     

if (__name__ == "__main__"):
  main()