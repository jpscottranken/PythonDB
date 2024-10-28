'''
	Make the non-Object Oriented program created in application
   demo02DB.py an object-oriented program.
   
   To do this, create an Employee class for the employee table
   fields and a Database class to hold the CRUD operations 
   (and other) methods.

	Key Changes:
	============
	1.	Employee Class: This class encapsulates the employee data 
		(first name, last name, and email).
	
	2.	Database Class: Manages the database connection and CRUD 
		operations. It also handles the creation of the employees table.

	3.	Object-oriented CRUD operations: Methods inside the Database class 
		handle inserting, reading, updating, and deleting employees.

	4.	Cleaner insertion of multiple employees: Now uses a list of Employee 
		objects rather than tuples.

	5.	This refactored code follows the principles of object-oriented 
		programming, making it more modular, reusable, and easier to maintain.
'''
import sqlite3

class Employee:
  def __init__(self, firstName, lastName, email=None):
    self.firstName = firstName
    self.lastName  = lastName
    self.email     = email
  
  # https://www.pythontutorial.net/python-oop/python-__repr__/
  # https://realpython.com/python-repr-vs-str/
  def __repr__(self):
    return f"Employee({self.firstName}, {self.lastName}, {self.email})"

class Database:
  def __init__(self, dbName = "test3.db"):
    self.dbName = dbName
    self.conn   = self.createConnection()

  # Step 1: Create database connection
  def createConnection(self):
    try:
      conn = sqlite3.connect(self.dbName)
      print(f"\nConnection established.")
      return conn
    except sqlite3.Error as e:
      print(f"\nError trying to connect to database: {e}")
      return None
  
  # Step 2: Create a database table
  def createTable(self):
    try:
      c = self.conn.cursor()
      createTableQuery = """
        CREATE TABLE IF NOT EXISTS employees
        (
            firstName     TEXT      NOT NULL,
            lastName      TEXT      NOT NULL,
            email         TEXT          NULL
        )
      """

      c.execute(createTableQuery)
      self.conn.commit()

      print(f"\nEmployees table successfully created.")
    except sqlite3.Error as e:
        print(f"\nError trying to create table employees: {e}")

  # Step 3: Insert one record into employees table
  def insertSingleEmployee(self, employee):
    try:
      c = self.conn.cursor()
      insertEmployeeQuery = """
          INSERT INTO employees(firstName, lastName, email)
          Values (?, ?, ?)
      """
      c.execute(insertEmployeeQuery, \
              (employee.firstName, employee.lastName, employee.email))
      self.conn.commit()

      print(f"\nRecord for {employee.firstName} {employee.lastName} successfully inserted.")
    except sqlite3.Error as e:
        print(f"\nError trying to insert record into table employees: {e}")

  # Step 4: Insert multiple records into the employees table
  def insertMultipleEmployees(self, employees):
    try:
      c = self.conn.cursor()
      c.executemany("INSERT INTO employees VALUES (?, ?, ?)",
        [(emp.firstName, emp.lastName, emp.email) for emp in employees])

      self.conn.commit()
      print(f"\nAdditional employee records successfully inserted.")
    except sqlite3.Error as e:
        print(f"\nError trying to insert records into table employees: {e}")

  # Step 5: Display all records of the employees table
  def displayEmployeeRecords(self):
    try:
      c = self.conn.cursor()
      c.execute("SELECT * FROM employees")

      rows = c.fetchall()
      print(f"\nHere are the current records in the employees table")
      for row in rows:
        print(f"Name: {row[0]} {row[1]}\tEmail: {row[2]}")
    except sqlite3.Error as e:
        print(f"\nError trying to display employees: {e}")

  # Step 6: Display all gmails of the employees table
  def displayGmailRecords(self):
    try:
      c = self.conn.cursor()
      gmailQuery = """
                SELECT * FROM employees
                WHERE email LIKE '%gmail.com'
      """
      c.execute(gmailQuery)

      rows = c.fetchall()
      print(f"\nHere are the current Gmail records in the employees table")
      for row in rows:
        print(f"Name: {row[0]} {row[1]}\tEmail: {row[2]}")
    except sqlite3.Error as e:
        print(f"\nError trying to display employees: {e}")

  # Step 7: Update tonyboy the "bad" way
  def updateByEmployeeName(self, email, firstName, lastName):
    try:
      c = self.conn.cursor()
      updateByNameQuery = """
          UPDATE employees
          SET email = ?
          WHERE firstName = ? AND lastName = ?
      """
      c.execute(updateByNameQuery, (email, firstName, lastName))
      self.conn.commit()

      print(f"\nUpdated email address for {firstName} {lastName} is: {email}")
    except sqlite3.Error as e:
        print(f"\nError trying to update employee email address: {e}")

  # Step 8: Update Kate Black's email the "good" way
  def updateByRowid(self, email, rowid):
    try:
      c = self.conn.cursor()
      updateByRowidQuery = """
          UPDATE employees
          SET   email = ?
          WHERE rowid = ?
      """
      c.execute(updateByRowidQuery, (email, rowid))
      self.conn.commit()

      print(f"\nUpdated email address for Employee #{rowid} is: {email}")
    except sqlite3.Error as e:
        print(f"\nError trying to update employee: {e}")

  # Step 9: Delete Jeff Scott employee record
  def deleteEmployee(self, rowid):
    try:
      c = self.conn.cursor()
      deleteQuery = """
            DELETE FROM employees
            WHERE rowid = ?
      """

      c.execute(deleteQuery, (rowid,))
      self.conn.commit()

      print(f"\nDeleted employee with rowid {rowid}")
    except sqlite3.Error as e:
        print(f"\nError trying to delete employee: {e}")

  # Step 10: Close database connection
  def closeDBConnection(self):
    if (self.conn):
      self.conn.close()
      print(f"\nDB connection closed.")

def main():
  db = Database()
  db.createTable()

  # Create all 5 current employees
  jeff = Employee('Jeff', 'Scott', 'jpscott@gmail.com')
  mary = Employee('Mary', 'Green', 'marygreen@yahoo.com')
  will = Employee('Will', 'Frank', 'willfrank@gmail.com')
  kate = Employee('Kate', 'Black', 'katieb@yahoo.com')
  tony = Employee('Tony', 'White', 'tonyboy@gmail.com')

  # Call method to insert employee 1 (Jeff Scott)
  db.insertSingleEmployee(jeff)

  # Call method to insert multiple employees
  db.insertMultipleEmployees([mary, will, kate, tony])
  db.displayEmployeeRecords()

  # Call method to display employees with Gmail addresses
  db.displayGmailRecords()

  # Call method to update tonyboy's email address
  db.updateByEmployeeName('tonywhite@yahoo.com', 'Tony', 'White')
  db.displayEmployeeRecords()

  # Call method to update Kate Black's email address
  db.updateByRowid('kateblack@yahoo.com', '4')
  db.displayEmployeeRecords()

  # Call method to delete employee Jeff Scott
  db.deleteEmployee('1')
  db.displayEmployeeRecords()

  # Call method to close DB connection (end program)
  db.closeDBConnection()

if (__name__ == "__main__"):
  main()

  '''
    This example has covered the basics of performing
    CRUD (Create/Read/Update/Delete) operations on an
    SQLite3 database using Python in an object-oriented
    manner.

    You learned the following in this program:

    1. How to connect to SQLite3
    2. How to create a cursor
    3. How to create a table
    4. How to insert a single record into a table
    5. How to insert mutiple records into a table
       4 & 5 represent the  (C or Create from CRUD)
    6. How to query data    (R or Read   from CRUD)
    7. How to update data   (U or Update from CRUD)
    8. How to delete data   (D or Delete from CRUD)

    The difference between demo03DB.py (this program)
    and demo02DB.py (the previous program) is that
    demo03DB.py used OOP with an Employee class and
    a Database class.

    Like demo02DB.py, all operations, CRUD and others
    were put into their own functions (actually methods).
    The rest of the program was basically the same as
    program demo02DB.py

    We will continue on with a new DB in the next example.
  '''