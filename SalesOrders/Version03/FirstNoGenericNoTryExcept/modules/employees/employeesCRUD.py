# Handle the CRUD operations for the Employee table
def createEmployee(cursor):
  # Input fields for new record
  employeeFirstName       = input("Enter Employee First Name: ")
  employeeLastName        = input("Enter Employee Last  Name: ") 
  employeeStreetAddress   = input("Enter Employee Street Address: ")
  employeeCity            = input("Enter Employee City: ")
  employeeState           = input("Enter Employee State: ")
  employeeZipCode         = input("Enter Employee Zip Code: ")
  employeeAreaCode        = input("Enter Employee Area Code: ")
  employeePhoneNumber     = input("Enter Employee Phone Number: ") 

  # Run the insert query
  cursor.execute("""
                      INSERT INTO employees
                      (EmployeeFirstName, EmployeeLastName,
                       EmployeeStreetAddress,
                       EmployeeCity, EmployeeState, EmployeeZipCode,
                       EmployeeAreaCode, EmployeePhoneNumber)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                 """,
                (employeeFirstName, employeeLastName,
                 employeeStreetAddress,
                 employeeCity, employeeState, employeeZipCode,
                 employeeAreaCode, employeePhoneNumber,))
  print("Employee Created.")

def readEmployees(cursor):
  print("Here Are The Employees: ")

  # Run the select query
  cursor.execute("SELECT * FROM employees")

  # Fetch all of the records found
  rows = cursor.fetchall()
  for row in rows:
    # Print all of the records found
    print(row)

def updateEmployee(cursor):
  print("NOTE: You CANNOT Update The EmployeeID (PK)!")
  # Determine row to update
  employeeID = input("Enter employeeID of record to update: ")

  # Add updated fields
  newEmployeeFirstName       = input("Enter Updated Employee First Name: ")
  newEmployeeLastName        = input("Enter Updated Employee Last  Name: ") 
  newEmployeeStreetAddress   = input("Enter Updated Employee Street Address: ")
  newEmployeeCity            = input("Enter Updated Employee City: ")
  newEmployeeState           = input("Enter Updated Employee State: ")
  newEmployeeZipCode         = input("Enter Updated Employee Zip Code: ")
  newEmployeeAreaCode        = input("Enter Updated Employee Area Code: ")
  newEmployeePhoneNumber     = input("Enter Updated Employee Phone Number: ") 

  # Update the database
  cursor.execute("""
                    UPDATE employees
                    SET    EmployeeFirstName      = ?,
                           EmployeeLastName       = ?,
                           EmployeeStreetAddress  = ?,
                           EmployeeCity           = ?,
                           EmployeeState          = ?,
                           EmployeeZipCode        = ?,
                           EmployeeAreaCode       = ?,
                           EmployeePhoneNumber    = ?           
                    WHERE  EmployeeID             = ?
                """,
                (newEmployeeFirstName, newEmployeeLastName, 
                 newEmployeeStreetAddress,
                 newEmployeeCity, newEmployeeState, newEmployeeZipCode,
                 newEmployeeAreaCode, newEmployeePhoneNumber,
                 employeeID,))
  print ("Employee Updated.")

def deleteEmployee(cursor):
  # Prompt for record to delete
  employeeID = input("Enter EmployeeID Of Record To Felete: ")

  # Run the delete query
  cursor.execute("""
                    DELETE FROM employees
                    WHERE EmployeeID = ?
                """,
                (employeeID,))
  print ("Employee Deleted.")
