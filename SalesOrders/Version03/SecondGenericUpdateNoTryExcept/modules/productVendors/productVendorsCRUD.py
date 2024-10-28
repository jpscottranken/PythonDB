# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord

# Handle the CRUD operations for the ProductVendors table
def createProductVendor(cursor):
  # Input fields for new record
  productID                   = input("Enter ProductVendor ProductID: ")
  vendorID                    = input("Enter ProductVendor VendorID:  ")
  productVendorWholesalePrice = input("Enter ProductVendor Wholesale Price: ")
  productVendorDaysToDeliver  = input("Enter ProductVendor Days To Deliver: ")

  # Run the insert query
  cursor.execute("""
                      INSERT INTO productVendors
                      (ProductID, VendorID,
                       ProductVendorWholesalePrice, 
                       ProductVendorDaysToDeliver)
                      VALUES (?, ?, ?, ?)
                 """,
                (productID, vendorID,
                 productVendorWholesalePrice,
                 productVendorDaysToDeliver))

  print("ProductVendor Created.")

def readProductVendors(cursor):
  print("Here Are The ProductVendors: ")

  # Run the select query
  cursor.execute("SELECT * FROM productVendors")

  # Fetch all of the records found
  rows = cursor.fetchall()
  for row in rows:
    # Print all of the records found
    print(row)

def updateProductVendor(cursor):
  updateRecord(cursor, "ProductVendors", ['ProductID', 'VendorID'],
               ['ProductVendorWholesalePrice',
                'ProductVendorDaysToDeliver'])

def deleteProductVendor(cursor):
  # Prompt for record to delete
  productID = input("Enter ProductID Of Record To Delete: ")
  vendorID  = input("Enter VendorID  Of Record To Delete: ")

  # Run the delete query
  cursor.execute("""
                    DELETE FROM productVendors
                    WHERE ProductID = ?
                    AND   VendorID  = ?
                """,
                (productID, vendorID))

  print("ProductVendor Deleted.")
