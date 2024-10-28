# Handle the CRUD operations for the Customers table
def createCustomer(cursor):
  # Input fields for new record
  customerFirstName       = input("Enter Customer First Name: ")
  customerLastName        = input("Enter Customer Last  Name: ") 
  customerStreetAddress   = input("Enter Customer Street Address: ")
  customerCity            = input("Enter Customer City: ")
  customerState           = input("Enter Customer State: ")
  customerZipCode         = input("Enter Customer Zip Code: ")
  customerAreaCode        = input("Enter Customer Area Code: ")
  customerPhoneNumber     = input("Enter Customer Phone Number: ") 

  # Run the insert query
  cursor.execute("""
                      INSERT INTO customers
                      (CustomerFirstName, CustomerLastName,
                       CustomerStreetAddress,
                       CustomerCity, CustomerState, CustomerZipCode,
                       CustomerAreaCode, CustomerPhoneNumber)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                 """,
                (customerFirstName, customerLastName,
                 customerStreetAddress,
                 customerCity, customerState, customerZipCode,
                 customerAreaCode, customerPhoneNumber,))
  print("Customer Created.")

def readCustomers(cursor):
  print("Here Are The Customers: ")

  # Run the select query
  cursor.execute("SELECT * FROM customers")

  # Fetch all of the records found
  rows = cursor.fetchall()
  for row in rows:
    # Print all of the records found
    print(row)

def updateCustomer(cursor):
  print("NOTE: You CANNOT Update The CustomerID (PK)!")
  # Determine row to update
  customerID = input("Enter CustomerID of record to update: ")

  # Add fields to update
  newCustomerFirstName       = input("Enter Updated Customer First Name: ")
  newCustomerLastName        = input("Enter Updated Customer Last  Name: ") 
  newCustomerStreetAddress   = input("Enter Updated Customer Street Address: ")
  newCustomerCity            = input("Enter Updated Customer City: ")
  newCustomerState           = input("Enter Updated Customer State: ")
  newCustomerZipCode         = input("Enter Updated Customer Zip Code: ")
  newCustomerAreaCode        = input("Enter Updated Customer Area Code: ")
  newCustomerPhoneNumber     = input("Enter Updated Customer Phone Number: ") 

  # Update the database
  cursor.execute("""
                    UPDATE customers
                    SET    customerFirstName      = ?,
                           customerLastName       = ?,
                           customerStreetAddress  = ?,
                           customerCity           = ?,
                           customerState          = ?,
                           customerZipCode        = ?,
                           customerAreaCode       = ?,
                           customerPhoneNumber    = ?           
                    WHERE  customerID             = ?
                """,
                (newCustomerFirstName, newCustomerLastName, 
                 newCustomerStreetAddress,
                 newCustomerCity, newCustomerState, newCustomerZipCode,
                 newCustomerAreaCode, newCustomerPhoneNumber,
                 customerID))
  print ("Customer Updated.")

def deleteCustomer(cursor):
  # Prompt for record to delete
  customerID = input("Enter CustomerID Of Record To Delete: ")

  # Run the delete query
  cursor.execute("""
                    DELETE FROM customers
                    WHERE CustomerID = ?
                """,
                (customerID,))
  print ("Customer Deleted.")
