# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord
from modules.genericCRUD.crudFunctions import readRecords
from modules.genericCRUD.crudFunctions import deleteRecord

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
  readRecords(cursor, "ProductVendors")

def updateProductVendor(conn, cursor):
  updateRecord(conn, cursor, "ProductVendors", ['ProductID', 'VendorID'],
               ['ProductVendorWholesalePrice',
                'ProductVendorDaysToDeliver'])

def deleteProductVendor(conn, cursor):
    productIDValue = input("Enter the number (ProductID) of the record to delete: ")
    vendorIDValue  = input("Enter the number (VendorID)  of the record to delete: ")

    # Then pass it into the deleteRecord function
    primaryKeys = {"ProductID": productIDValue, "VendorID": vendorIDValue}
    deleteRecord(conn, cursor, "ProductVendors", primaryKeys)
    