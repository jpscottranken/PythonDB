# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord
from modules.genericCRUD.crudFunctions import readRecords
from modules.genericCRUD.crudFunctions import deleteRecord

# Handle the CRUD operations for the Products table
def createProduct(cursor):
  # Input fields for new record
  productName       = input("Enter Product Name: ")
  productDescShort  = input("Enter short Product Description: ") 
  productDescLong   = input("Enter long  Product Description: ")
  productImage      = input("Enter Product Image URL: ")
  productPrice      = input("Enter Product Price: ")
  productQty        = input("Enter Product Quantity: ")
  categoryID        = input("Enter CategoryID: ")

  # Run the insert query
  cursor.execute("""
                      INSERT INTO products
                      (ProductName,
                       ProductDescShort, ProductDescLong,
                       ProductImage, ProductPrice,
                       ProductQty, CategoryID)
                      VALUES (?, ?, ?, ?, ?, ?, ?)
                 """,
                (productName,
                 productDescShort, productDescLong,
                 productImage, productPrice,
                 productQty, categoryID,))
  print("Product Created.")

def readProducts(cursor):
  readRecords(cursor, "Products")

def updateProduct(conn, cursor):
  updateRecord(conn, cursor, "Products", ['ProductID'],
               ['ProductName',
                'ProductDescShort', 'ProductDescLong',
                'ProductImage', 'ProductPrice',
                'ProductQty', 'CategoryID'])

def deleteProduct(conn, cursor):
  productIDValue = input("Enter the number (ProductID) of the record to delete: ")

  # Then pass it into the deleteRecord function
  primaryKeys = {"ProductID": productIDValue}
  deleteRecord(conn, cursor, "Products", primaryKeys)
