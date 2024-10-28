# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord

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
  print("Here Are The Products: ")

  # Run the select query
  cursor.execute("SELECT * FROM products")

  # Fetch all of the records found
  rows = cursor.fetchall()
  for row in rows:
    # Print all of the records found
    print(row)

def updateProduct(cursor):
  updateRecord(cursor, "Products", ['ProductID'],
               ['ProductName',
                'ProductDescShort', 'ProductDescLong',
                'ProductImage', 'ProductPrice',
                'ProductQty', 'CategoryID'])

def deleteProduct(cursor):
  # Prompt for record to delete
  productID = input("Enter ProductID Of Record To Delete: ")

  # Run the delete query
  cursor.execute("""
                    DELETE FROM products
                    WHERE ProductID = ?
                """,
                (productID,))

  print("Product Deleted.")
