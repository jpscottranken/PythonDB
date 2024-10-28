import sqlite3

"""
    NOTES:
    ======
    1.  The generic updateRecord() function must handle
        having a PK of one field or a PK of multiple fields.
    
    2.  The user should be able to either:
    
        a) Enter in a new value for the field in question.

        OR:

        b) Hit the <enter> key to keep the current DB value
           in the database without changing it.
    
    3.  Why are we doing this anyway?
    
        Writing a generic function such as this will
        eliminate the need for writing separate update
        functions for each of the 8 different tables in
        the SalesOrders database.
    
    HOW TO DO THIS:
    ===============
    1.  Identify the table to be updated and its PK(s).

        So the updateRecord() function must take in both
        the table name and the primary key(s) as parameters.

    2.  Fetch the current record.

        Before possibly updating this record, we need to
        fetch it so we have that record's current values.

    3.  Dynamically update the record.

        Allow the user to update 1...all fields they
        wish to update.

    4.  Must support both single PK and a concatenated PK.

    5.  Build the update statement dynamically.

        This will be based on the table name, the
        primary key(s), and the field(s) to be updated.
"""

##########################################################
#   Generic Create Function (Written But NOT EVER CALLED!)
def insertRecord(conn, cursor, tableName, data):
  """
  The insertRecord() function will let a user
  insert a new record into table tableName.

  :param cursor:        The necessary database cursor
  :param tableName:     The table containing the record to delete
  :param data:          These are the fields to insert
  :return:              none 
  """
  try:
    #   Prepare column names and values for SQL Insert query
    columnNames  = ', '.join(data.keys())
    columnValues = ', '.join(['?' for _ in data])
    values       = tuple(data.values())

    #   Construct SQL Insert query
    insertQuery = (f"""
                        INSERT INTO {tableName}
                                    ({columnNames})
                        VALUES      ({columnValues})
                    """)

    #   Execute the SQL Insert query
    cursor.execute(insertQuery, values)
    # Print insert success message
    print(f"\n{tableName} Record Inserted.")

    #   Commit changes to SalesOrders DB
    conn.commit()
  # Exception Handlers
  except sqlite3.DatabaseError as e:
    print(f"Database Error: {e}")
  except sqlite3.IntegrityError as e:
    print(f"Integrity Error: {e}")
  except sqlite3.ProgrammingError as e:
    print(f"Programming Error: {e}")
  except sqlite3.DataError as e:
    print(f"Data Error: {e}")
  except sqlite3.NotSupportedError as e:
    print(f"Not Supported Error: {e}")
  except sqlite3.Error as e:
    print(f"Generic Database Error: {e}")

##########################################################
#   Generic Read Function
def readRecords(cursor, tableName):
  """
  The readRecords() function will let a user
  view all records from table tableName.

  :param cursor:        The necessary database cursor
  :param tableName:     The table containing the record to delete
  :return:              none 
  """ 
  try:
    print(f"Here Are The Records In The {tableName} Table: ")

    # Run the select query
    cursor.execute(f"SELECT * FROM {tableName}")

    # Fetch all of the records found
    rows = cursor.fetchall()
    for row in rows:
        # Print all of the records found
        print(row)

    # Print read message
    print(f"\nAll {tableName} Records Read.")
  # Exception Handlers
  except sqlite3.DatabaseError as e:
    print(f"Database Error: {e}")
  except sqlite3.IntegrityError as e:
    print(f"Integrity Error: {e}")
  except sqlite3.ProgrammingError as e:
    print(f"Programming Error: {e}")
  except sqlite3.DataError as e:
    print(f"Data Error: {e}")
  except sqlite3.NotSupportedError as e:
    print(f"Not Supported Error: {e}")
  except sqlite3.Error as e:
    print(f"Generic Database Error: {e}")

##########################################################
#   Generic Update Function
def updateRecord(conn, cursor, tableName, primaryKeys, updateFields):
  """
  The updateRecord() function will let a user
  update a record from table tableName given
  primary key(s) primaryKeys. This allows for
  a "selective" update, where the user can
  update any field(s) desired or just hit the
  <enter> key to keep the current DB value.

  :param conn:          The database connection
  :param cursor:        The necessary database cursor
  :param tableName:     The table containing the record to delete
  :param primaryKeys:   The primary key(s) of tableName
  :param updateFields:  All fields in tableName
  :return:              none 
  """ 
  try:
    # Fetch the current record to allow the user
    # to keep any current record field values they want to
    # enter in new values for any field desired.
    whereClause       = " AND ".join([f"{key} = ?" for key in primaryKeys])
    primaryKeyValues  = [input(f"Enter {key} of record to update: ") for key in primaryKeys]

    # Fetch current value for all fields
    # of the current record.
    cursor.execute(f"""
                        SELECT {', '.join(updateFields)}
                        FROM   {tableName}
                        WHERE  {whereClause}""",
                            primaryKeyValues )
    currentRecord = cursor.fetchone()

    # This SHOULD NEVER happen. But,
    # if the currentRecord is empty, 
    # print error message and return
    if (not currentRecord):
        print(f"No record found with the primary key(s) given in table {tableName}")
        return
    
    # Let the user update field(s), or keep the current
    # DB value if the <enter> key is pressed instead.
    updateValues = []
    for i, field in enumerate(updateFields):
        newValue = input(f"Enter Updated {field} value OR Press <enter> to keep current DB value of {currentRecord[i]}: ")
        updateValues.append(newValue if newValue != "" else currentRecord[i])

    # Build our UPDATE SQL statement dynamically
    setClause = ", ".join([f"{field} = ?" for field in updateFields])

    # Execute the update statement
    cursor.execute(f"""
                            UPDATE {tableName}
                            SET    {setClause}
                            WHERE  {whereClause}
                    """,
                    updateValues + primaryKeyValues)
    
    # Print update success message
    print(f"\n{tableName} Record Updated.")

    #   Commit changes to SalesOrders DB
    conn.commit()
  # Exception Handlers
  except sqlite3.DatabaseError as e:
    print(f"Database Error: {e}")
  except sqlite3.IntegrityError as e:
    print(f"Integrity Error: {e}")
  except sqlite3.ProgrammingError as e:
    print(f"Programming Error: {e}")
  except sqlite3.DataError as e:
    print(f"Data Error: {e}")
  except sqlite3.NotSupportedError as e:
    print(f"Not Supported Error: {e}")
  except sqlite3.Error as e:
    print(f"Generic Database Error: {e}")

##########################################################
#   Generic Delete Function
def deleteRecord(conn, cursor, tableName, primaryKeys):
  """
  The deleteRecord() function will let a user
  delete a record from table tableName given
  primary key(s) primaryKeys.

  :param conn:        The database connection
  :param cursor:      The necessary database cursor
  :param tableName:   The table containing the record to delete
  :param primaryKeys: The primary key(s) of tableName
  :return:            none
  """
  try:
    #   Set WHERE clause based on the primary key(s)
    whereClause = ' AND '.join([f"{col} = ?" for col in primaryKeys])
    values      = tuple(primaryKeys.values())

    #   Construct the SQL delete query
    deleteQuery = (f"""
                        DELETE FROM {tableName}
                        WHERE  {whereClause}
                    """)

    #   Execute the SQL delete query
    cursor.execute(deleteQuery, values)    

    # Print delete success message
    print(f"\n{tableName} Record Deleted.")

    #   Commit changes to SalesOrders DB
    conn.commit()
  # Exception Handlers
  except sqlite3.DatabaseError as e:
    print(f"Database Error: {e}")
  except sqlite3.IntegrityError as e:
    print(f"Integrity Error: {e}")
  except sqlite3.ProgrammingError as e:
    print(f"Programming Error: {e}")
  except sqlite3.DataError as e:
    print(f"Data Error: {e}")
  except sqlite3.NotSupportedError as e:
    print(f"Not Supported Error: {e}")
  except sqlite3.Error as e:
    print(f"Generic Database Error: {e}")
