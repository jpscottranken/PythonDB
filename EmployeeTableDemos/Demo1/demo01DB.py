'''
  The Python standard library includes a module called sqlite3.
  This module contains the interface to work with SQLite databases.

  There is no need to install DBLite on your machine. Rather, just
  import the sqlite3 module to work with it "right out of the box".
'''

import sqlite3

def main():
  '''
      Step 1: Create a database connection.
      =====================================
      Create a connection object to represent a database.
      In this case, the database will be called test1.db

      sqlite3 has a method named connect(). Within this
      connect() method, the programmer can either pass
      in a file (as we do in line 30) or make an in-memory
      database (shown in line 31 but commented out).

      Executing this code will create the test1.db file
      in the current directory. Even if the file has
      already existed, we will not get an error if the
      code is run again.

      Typically, the object is called conn, con, or connection.
      We will name our connection con.
  '''
  conn = sqlite3.connect("test1.db")
  #conn = sqlite3.connect(":memory:")

  '''
      Step 2: Create a database cursor.
      =================================
      A cursor lets the programmer execute SQL commands. The
      programmer creates a cursor by execution the cursor()
      method of the connection object.

      The execute() method of the cursor object is used to
      run SQL commands, as will be seen below.

       Typically, the object is called cursor, cur, or c.
       We will name our cursor c.   
  '''
  c = conn.cursor()

  print ("\nAble to connect to SQLite and create new database.")

  '''
      SQLite 3 Data Types:
      ====================
      NULL              (unknown)
      INTEGER           (whole numbers)
      REAL              (numbers with a decimal portion)
      TEXT              (strings)
      BLOB              (binary large object, e.g. images)
  '''
  
  '''
      Step 3: Create a database table.
      ================================
      Using the cursor object, we will now create an
      employees table. In this initial example, the
      employees table will have only the following
      3 fields (a.k.a. columns or attibutes):

      1.  firstName
      2.  lastName
      3.  email

      Please note that below, I am using triple double
      quotes("""""") for wrapping many of the SQL commands.
      This is also known as a "docstring". Again, the
      benefit is that it allows the programmer to write
      string values over multiple lines.
  '''
  createEmployeesTableQuery = """
      CREATE TABLE IF NOT EXISTS employees
      (
          firstName   TEXT  NOT NULL,
          lastName    TEXT  NOT NULL,
          email       TEXT      NULL
      )
  """

  '''
      The SQL command to run will go into the execute()
      method of the cursor object. This execute() method
      is used to help run SQL commands.
  '''
  c.execute(createEmployeesTableQuery)
  print("\nEmployees Table Was Successfully Created.")

  '''
      STEP 4: Insert New Record Into Employees Table
      ==============================================
      To insert a new employee records, we use the
      INSERT INTO <tableName> VALUES() command.

      In the example below, the "?" are used as
      placeholders for the query.
  '''
  insertEmployeeQuery = """
      INSERT INTO employees(firstName, lastName, email) VALUES (?, ?, ?)
  """

  '''
      Actually insert the data into the employees table.
      employee1 is the record #1 we are inputting into
      said table.
  '''
  employee1 = ("Janet", "Dawson", "janetd@gmail.com")
  c.execute(insertEmployeeQuery, employee1)
  print("\nRecord employee1 inputted into employees table.")

  '''
      After creating table employees and adding record
      employee1 to this table, we must commit the changes
      to the database. For that, we use the commit()
      method of the connection object.
  '''
  conn.commit()

  '''
      Query the database to verify that record employee1
      indeed does exist in the employees table.
  '''
  c.execute("SELECT * FROM employees")
  print("\nThe results are: ")

  '''
      There are three different fetch() methods that can
      be used to get database records. One of those methods
      is fetchone(), which gets the next row in the result
      set.
  '''
  print(c.fetchone())

  '''
      STEP 5: Insert 4 More Records Into Employees Table
      ==================================================
      Insert multiple records into the employees table,
      all at the same time.

      Create a list called 4MoreRecords
  '''
  fourMoreRecords = [
                      ('Robert', 'Smith', 'rsmith@yahoo.com'),
                      ('Karen',  'Jones', 'kjones@gmail.com'),
                      ('Mark',   'Black', 'mblack@yahoo.com'),
                      ('Mary',   'Brown', 'mbrown@gmail.com'),
                    ]

  '''
      Insert the four records above into the employees table.
      Rather than executing the INSERT INTO query above once for
      each new record (i.e. 4 different INSERT INTO statements),
      we will perform a "bulk insert" operation in a single
      query using a cursor's executemany() function.

      The executemany() method of the cursor() object takes
      2 arguments:

      1.  An SQL query
      2.  The records to update
  '''
  c.executemany("INSERT INTO employees VALUES (?, ?, ?)", fourMoreRecords)
  
  # Commit the change
  conn.commit()
  print("\n4 records succesfully inserted. See below:")

  '''
      Fetch Method                Functionality
      ==============================================================
      fetchone()        This method will get the next row in the
                        result set. It returns one record if it
                        exists. Otherwise it returns none.

      fetchmany(n)      This method will return a specified number
                        of rows (records), i.e. the "n" in the ()
                        as a list. If there no records, it returns
                        an empty list.

      fetchall()        This method returns all rows as a list.
                        If there no rows, it returns an empty list.
  '''
  # First, get all employee records
  c.execute("SELECT * FROM employees")

  print("\nUsing a fetchall() to print all 5 employee records.")
  rows = c.fetchall()
  for row in rows:
    print(f"Name: {row[0]} {row[1]}\tEmail: {row[2]}")

  '''
      STEP 6: Get some of the employee records.
      =========================================
      Retrieve only those employees that have a gmail
      email address.
  '''
  selectGmailQuery = """
      SELECT * FROM employees
      WHERE email LIKE '%gmail.com'
  """

  # Execute the query
  c.execute(selectGmailQuery)

  print("\nShowing only those employees with a gmail email address.")
  for row in c.fetchall():
    print(f"Name: {row[0]} {row[1]}\tEmail: {row[2]}")

  """
      STEP 7: Updating data (the "hard" way).
      =======================================
      In this example, we will use an update query
      to update Mary Brown's email in the employees table
  """
  updateMBQuery = """
            UPDATE employees SET email = ? WHERE firstName = ? AND lastName = ?
    """

  '''
        This query needs 2 parameters:

        1.  The updated data.
        2.  Whose data to update.
  '''
  updateData = ("mbrown@bing.com", "Mary", "Brown")
  
  # Run and commit the query
  c.execute(updateMBQuery, updateData)
  conn.commit()

  print("\nMary Brown email address update succesfully. See below.")

  c.execute("SELECT rowid, * FROM employees")

  print("\nUsing a fetchall() to print all 5 employee records.")
  rows = c.fetchall()
  for row in rows:
    print(f"Record #: {row[0]} Name: {row[1]} {row[2]}\tEmail: {row[3]}")

  '''
      STEP 8: Updating data (the "easy" way).
      =======================================
      In this example, we will use an update query
      to update Mary Brown's email in the employees table.
      However, we will base it on the row number (rowid),
      and not on firstName and lastName.
  '''
  updateMB2Query = """
            UPDATE employees SET email = ? WHERE rowid = ?
    """

  '''
        This query needs 2 parameters:

        1.  The updated data.
        2.  Whose data to update.
  '''
  update2Data = ("mbrown@marybrown.com", "5")
  
  # Run and commit the query
  c.execute(updateMB2Query, update2Data)
  conn.commit()

  print("\nMary Brown email address update succesfully. See below.")

  c.execute("SELECT rowid, * FROM employees")

  print("\nUsing a fetchall() to print all 5 employee records.")
  rows = c.fetchall()
  for row in rows:
    print(f"Record #: {row[0]} Name: {row[1]} {row[2]}\tEmail: {row[3]}")

  '''
      STEP 9: Deleting a record.
      =========================
      In this example, we will use delete query
      to delete a record from the employees table.
  '''
  deleteQuery = """
        DELETE FROM employees WHERE rowid = ?
  """

  '''
    We must provide the rowid as a parameter.

    Two minor "quirks" here:

    1.  Even though rowid is an integer, sqlite3
        expects you to pass it in as a text field.
    2.  This "works better" if you add the ending
        comma as shown. I read this in an article
        that I forgot to bookmark.
  '''
  userData = "4"

  # Execute the query and do a commit.
  c.execute(deleteQuery, userData)
  conn.commit()

  print("\nEmployee Mark Black successfully deleted. See below.")
  c.execute("SELECT rowid, * FROM employees")

  print("\nUsing a fetchall() to print all 4 employee records.")
  rows = c.fetchall()
  for row in rows:
    print(f"Record #: {row[0]} Name: {row[1]} {row[2]}\tEmail: {row[3]}")

  '''
      STEP 10: Error Handling And Cleanup.
      ====================================
      Proper error handling is crucial when working with
      a database. Especially if the database is being
      shared by more than one person.

      You should always close the SQLite3 connection 
      when you're done.

      However, even if you do not, the connection will
      automatically close when the program terminates.
  '''
  if 'c' in locals():
    c.close()
    conn.close()
    print("\nConnection closed.")
  
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
  '''
  
main()