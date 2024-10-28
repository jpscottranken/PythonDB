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

def updateRecord(cursor, tableName, primaryKeys, updateFields):
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
  
  # Print the update message
  print(f"{tableName} Record Updated.")