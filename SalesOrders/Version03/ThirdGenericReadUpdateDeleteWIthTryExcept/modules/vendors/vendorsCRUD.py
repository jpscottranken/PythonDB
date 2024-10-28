# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord
from modules.genericCRUD.crudFunctions import readRecords
from modules.genericCRUD.crudFunctions import deleteRecord

# Handle the CRUD operations for the Vendors table
def createVendor(cursor):
# Input fields for new record
  vendorName          = input("Enter Vendor Name: ")
  vendorStreetAddress = input("Enter Vendor Street Address: ")
  vendorCity          = input("Enter Vendor City: ")
  vendorState         = input("Enter Vendor State: ")
  vendorZipCode       = input("Enter Vendor Zip Code: ")
  vendorPhoneNumber   = input("Enter Vendor Phone Number: ")
  vendorFaxNumber     = input("Enter Vendor Fax   Number: ")
  vendorWebPage       = input("Enter Vendor Web Page URL: ")
  vendorEmailAddress  = input("Enter Vendor Email Address: ")

  # Run the insert query
  cursor.execute("""
                      INSERT INTO vendors
                      (VendorName, VendorStreetAddress,
                       VendorCity, VendorState, VendorZipCode,
                       VendorPhoneNumber, VendorFaxNumber,
                       VendorWebPage, VendorEmailAddress)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                 """,
                (vendorName, vendorStreetAddress,
                 vendorCity, vendorState, vendorZipCode,
                 vendorPhoneNumber, vendorFaxNumber,
                 vendorWebPage, vendorEmailAddress))

  print("Vendor Created.")

def readVendors(cursor):
  readRecords(cursor, "Vendors")

def updateVendor(conn, cursor):
  updateRecord(conn, cursor, "Vendors", ['VendorID'],
               ['VendorName', 'VendorStreetAddress',
                'VendorCity', 'VendorState', 'VendorZipCode',
                'VendorPhoneNumber', 'VendorFaxNumber',
                'VendorWebPage', 'VendorEmailAddress'])

def deleteVendor(conn, cursor):
  vendorIDValue = input("Enter the number (VendorID) of the record to delete: ")

  # Then pass it into the deleteRecord function
  primaryKeys = {"VendorID": vendorIDValue}
  deleteRecord(conn, cursor, "Vendors", primaryKeys)
