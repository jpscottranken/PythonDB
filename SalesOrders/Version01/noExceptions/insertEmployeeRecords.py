import sqlite3
# https://www.slingacademy.com/article/python-sqlite3-define-a-table-with-auto-incrementing-primary-key/
def insertEmployeeRecords(conn):
  try:
    c = conn.cursor()
      
    # Insert data
    employees = [
        ('Ann',      'Patterson',  '16 Maple Lane',           'Auburn',      'WA', '98002', '253', '555-2591'),
        ('Mary',     'Thompson',   '122 Spring River Drive',  'Duvall',      'WA', '98019', '425', '555-2516'),
        ('Matt',     'Bergstrom',  '908 W. Capital Way',      'Tacoma',      'WA', '98413', '253', '555-2581'),
        ('Carol',    'Viescas',    '722 Moss Bay Blvd.',      'Kirkland',    'WA', '98033', '425', '555-2576'),
        ('Kirk',     'DeGrasse',   '455 West Palm Ave',       'San Antonio', 'TX', '78284', '210', '5552311'),
        ('David',    'Viescas',    '16679 NE 42nd Court',     'Redmond',     'WA', '98052', '425', '555-2661'),
        ('Kathryn',  'Patterson',  '554 E. Wilshire Apt. 2A', 'Seattle',     'WA', '98105', '206', '555-2697'),
        ('Susan',    'McLain',     '511 Lenora Ave',          'Bellevue',    'WA', '98006', '425', '555-2301')
    ]
      
    # Insert each employee record
    for employee in employees:
        c.execute("""
            INSERT INTO employees 
            (EmployeeFirstName, EmployeeLastName, EmployeeStreetAddress, EmployeeCity, EmployeeState, EmployeeZipCode, EmployeeAreaCode, EmployeePhoneNumber) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, employee)

    conn.commit()
    print(f"\nMultiple employees successfully inserted into the table.")

    # Fetch and display all records in the employees table
    employeesQuery = "SELECT * FROM employees"
    c.execute(employeesQuery)
    print("\nThese are the employees in the employees table via fetchall:")
    print(c.fetchall())

    c.execute(employeesQuery)
    print("\nThese are the employees in the employees table via for loop:")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]} Name: {row[1]} {row[2]} Address: {row[3]} CSZ: {row[4]} {row[5]} {row[6]} Phone: {row[7]} {row[8]}")
  except sqlite3.Error as e:
      print(f"\nProblem trying to insert database records: {e}")