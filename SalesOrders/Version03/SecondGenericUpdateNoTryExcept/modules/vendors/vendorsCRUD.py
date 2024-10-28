# Import the genericCRUD CRUD modules
from modules.genericCRUD.crudFunctions import updateRecord

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
  print("Here Are The Vendors: ")

  # Run the select query
  cursor.execute("SELECT * FROM vendors")

  # Fetch all of the records found
  rows = cursor.fetchall()
  for row in rows:
    # Print all of the records found
    print(row)

def updateVendor(cursor):
  updateRecord(cursor, "Vendors", ['VendorID'],
               ['VendorName', 'VendorStreetAddress',
                'VendorCity', 'VendorState', 'VendorZipCode',
                'VendorPhoneNumber', 'VendorFaxNumber',
                'VendorWebPage', 'VendorEmailAddress'])

def deleteVendor(cursor):
  # Prompt for record to delete
  vendorID = input("Enter VendorID Of Record To Delete: ")

  # Run the delete query
  cursor.execute("""
                    DELETE FROM Vendors
                    WHERE VendorID = ?
                """,
                (vendorID,))

  print("Vendor Deleted.")
