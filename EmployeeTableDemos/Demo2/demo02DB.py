'''
    In this non-Object Oriented program, we put each
    of the CRUD operations (Create/Insert, Read/Select,
    Update, and Delete) in its own function.
'''

'''
    Changes made from demo01db.py:

    1.  Separation of CRUD operations:

        Each CRUD operation has been put into its
        own function.
    
    2.  Exception handling:

        Each database operation has been wrapped
        within a try/except block to handle any
        exceptions.
    
    3.  Function Parameters:

        Adjusted the function to accept necessary
        parameters such as conn (database connection)
        and the appropriate employee table details.
'''

import sqlite3

# Step 1.  Function createDatabaseConnection()
#
# This function will attempt to create
# and return a database connection.
def createConnection():
  try:
    conn = sqlite3.connect("test2.db")
    print(f"\nDatabase connection established.")
    return conn
  except sqlite3.Error as e:
    print(f"\nProblem trying to create database connection: {e}")
    return None
  
# Step 2.  Function createDatabaseTable()
#
# This function will attempt to create
# a database table.
def createDatabaseTable(conn):
  try:
    c = conn.cursor()
    createEmployeeTableQuery = """
        CREATE TABLE IF NOT EXISTS employees
        (
            firstName   TEXT    NOT NULL,
            lastName    TEXT    NOT NULL,
            email       TEXT        NULL
        )
    """

    c.execute(createEmployeeTableQuery)
    conn.commit()
    print(f"\nEmployees table successfully created.")
  except sqlite3.Error as e:
    print(f"\nProblem trying to create database table: {e}")
    return None

# Step 3.  Function insertOneEmployee(conn, emp)
#
# This function will attempt to insert
# a single employee into the employees table.
def insertOneEmployee(conn, emp):
  try:
    c = conn.cursor()
    insertOneEmployee = """
        INSERT INTO employees(
        firstName, lastName, email) 
        VALUES (?, ?, ?)
    """

    c.execute(insertOneEmployee, emp)
    conn.commit()

    print(f"\nEmployee {emp[0]} {emp[1]} successfully inserted into table.")
  except sqlite3.Error as e:
    print(f"\nProblem trying to insert database record: {e}")
    return None
  
# Step 4.  Function insertMultipleEmployees(conn, emps)
#
# This function will attempt to insert
# multiple employees into the employees table.
def insertMultipleEmployees(conn, emps):
  try:
    c = conn.cursor()
    c.executemany("INSERT INTO employees VALUES (?, ?, ?)", emps)

    conn.commit()
    print(f"\nMultiple employees successfully inserted into table.")
  except sqlite3.Error as e:
    print(f"\nProblem trying to insert database records: {e}")
    return None

# Step 5.  Function readEmployees(conn)
#
# This function will attempt to read
# all records in the employees table.
def readEmployees(conn):
  try:
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    rows = c.fetchall()
    for row in rows:
      print(f"Name: {row[0]} {row[1]}\tEmail: {row[2]}")
  except sqlite3.Error as e:
    print(f"\nProblem trying to read database records: {e}")
    return None

# Step 6.  Function readGmailers(conn)
#
# This function will attempt to read
# all employees with a Gmail email
# address in the employees table.
def readGmailers(conn):
  try:
    c = conn.cursor()
    selectGmailerQuery = """
        SELECT * FROM employees
        WHERE email LIKE '%gmail.com'
    """

    c.execute(selectGmailerQuery)
    rows = c.fetchall()
    print(f"\nEmployees with a gmail email address:")
    for row in rows:
      print(f"Name: {row[0]} {row[1]}\tEmail: {row[2]}")
  except sqlite3.Error as e:
    print(f"\nProblem trying to read database records: {e}")
    return None

# Step 7.  Function updateEmailBadWay
#
# This function will attempt to read
# all employees with a Gmail email
# address in the employees table.
def updateEmailBadWay(conn, email, firstName, lastName):
  try:
    c = conn.cursor()
    emailBadWayQuery = """
        UPDATE employees
        SET   email     = ?
        WHERE firstName = ?
        AND   lastName  = ?
    """

    c.execute(emailBadWayQuery, (email, firstName, lastName))
    conn.commit()

    print(f"\nUpdated email address for {firstName} {lastName}")
  except sqlite3.Error as e:
    print(f"\nProblem trying to update email address: {e}")
    return None

# Step 8.  Function updateEmailGoodWay
#
# This function will attempt to read
# all employees with a Gmail email
# address in the employees table.
def updateEmailGoodWay(conn, email, rowid):
  try:
    c = conn.cursor()
    emailGoodQuery = """
        UPDATE employees
        SET   email = ?
        WHERE rowid = ?
    """
    c.execute(emailGoodQuery, (email, rowid,))
    conn.commit()

    print(f"\nUpdated email address for employee #{rowid}")
  except sqlite3.Error as e:
    print(f"\nProblem trying to update email address: {e}")
    return None

# Step 9.  Function deleteEmployee(conn, rowid)
#
# This function will attempt to delete
# the employes with the rowid passed into it.
def deleteEmployee(conn, rowid):
  try:
    c = conn.cursor()
    deleteQuery = """
        DELETE FROM employees
        WHERE rowid = ?
    """
    c.execute(deleteQuery, (rowid,))
    conn.commit()

    print(f"\nDeleted employee #{rowid}")
  except sqlite3.Error as e:
    print(f"\nProblem trying to delete employee: {e}")
    return None

def main():
  conn = createConnection()
  if (conn):
    createDatabaseTable(conn)
    insertOneEmployee(conn, ("Ryan", "Peters", "rpeters@gmail.com"))
    insertMultipleEmployees(conn, [
      ('Fred',   'Flintstone', 'fredf@yahoo.com'),
      ('Wilma',  'Flintstone', 'wilmaf@yahoo.com'),
      ('Barney', 'Rubble',     'barneyr@gmail.com'),
      ('Betty',  'Rubble',     'bettyr@gmail.com'),
    ])
    readEmployees(conn)
    readGmailers(conn)
    updateEmailBadWay(conn, 'bettyr@bing.com', 'Betty', 'Rubble')
    readEmployees(conn)
    updateEmailGoodWay(conn, 'bettyr@edge.com', '5')
    readEmployees(conn)
    deleteEmployee(conn, "1")
    readEmployees(conn)
    conn.close()
    print(f"\nConnection closed. Program completed.")

if (__name__ == "__main__"):
  main()

  
  '''
    This example has covered the basics of performing
    CRUD (Create/Read/Update/Delete) operations on an
    SQLite3 database using Python.

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

    The difference between demo02DB.py (this program)
    and demo01DB.py (the previous program) is that
    demo01DB.py had only a main() function and this
    function included all operations, CRUD and others.

    In demo02DB.py, all operations, CRUD and others
    were put into their own functions. The rest of
    the program was basically the same as program
    demo01DB.py

    The last example of this, which will be program
    demo03DB.py will be object-oriented. The previous
    two programs were NOT object-oriented.

    In demo03DB.py, we will create a Database.py class
    and an Employee.py class to add the object orientation.
  '''