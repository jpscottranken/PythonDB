import sqlite3

# https://www.slingacademy.com/article/python-sqlite3-define-a-table-with-auto-incrementing-primary-key/
def insertCustomerRecords(conn):
  try:
    c = conn.cursor()
      
    # Insert data
    customers = [
    ('Suzanne', 'Viescas',   '15127 NE 24th, #383',     'Redmond',      'WA', '98052', '425', '555-2686'),
    ('William', 'Thompson',  '122 Spring River Drive',  'Duvall',       'WA', '98019', '425', '555-2681'),
    ('Gary',    'Hallmark',  'Route 2, Box 203B',       'Auburn',       'WA', '98002', '253', '555-2676'),
    ('Robert',  'Brown',     '672 Lamont Ave',          'Houston',      'TX', '77201', '713', '555-2491'),
    ('Dean',    'McCrae',    '4110 Old Redmond Rd.',    'Redmond',      'WA', '98052', '425', '555-2506'),
    ('John',    'Viescas',   '15127 NE 24th, #383',     'Redmond',      'WA', '98052', '425', '555-2511'),
    ('Mariya',  'Sergienko', '901 Pine Avenue',         'Portland',     'OR', '97208', '503', '555-2526'),
    ('Neil',    'Patterson', '233 West Valley Hwy',     'San Diego',    'CA', '92199', '619', '555-2541'),
    ('Andrew',  'Cencini',   '507 - 20th Ave. Apt. 2',  'Seattle',      'WA', '98105', '206', '555-2601'),
    ('Angel',   'Kennedy',   '667 Red River Road',      'Austin',       'TX', '78710', '512', '555-2571'),
    ('Alaina',  'Hallmark',  'Route 2, Box 203B',       'Woodinville',  'WA', '98072', '425', '555-2631'),
    ('Liz',     'Keyser',    '13920 S.E. 40th Street',  'Bellevue',     'WA', '98006', '425', '555-2556'),
    ('Rachel',  'Patterson', '2114 Longview Lane',      'San Diego',    'CA', '92199', '619', '555-2546'),
    ('Sam',     'Abolrous',  '611 Alpine Drive',        'Palm Springs', 'CA', '92263', '760', '555-2611'),
    ('Darren',  'Gehring',   '2601 Seaview Lane',       'Chico',        'CA', '95926', '530', '555-2616'),
    ('Jim',     'Wilson',    '101 NE 88th',             'Salem',        'OR', '97301', '503', '555-2636'),
    ('Manuela', 'Seidel',    '66 Spring Valley Drive',  'Medford',      'OR', '97501', '541', '555-2641'),
    ('David',   'Smith',     '311 20th Ave. N.E.',      'Fremont',      'CA', '94538', '510', '555-2646'),
    ('Zachary', 'Ehrlich',   '12330 Kingman Drive',     'Glendale',     'CA', '91209', '818', '555-2721'),
    ('Joyce',   'Bonnicks',  '2424 Thames Drive',       'Bellevue',     'WA', '98006', '425', '555-2726'),
    ('Estella', 'Pundt',     '2500 Rosales Lane',       'Dallas',       'TX', '75260', '972', '555-9938'),
    ('Caleb',   'Viescas',   '4501 Wetland Road',       'Long Beach',   'CA', '90809', '562', '555-0037'),
    ('Julia',   'Schnebly',  '2343 Harmony Lane',       'Seattle',      'WA', '99837', '206', '555-9936'),
    ('Mark',    'Rosales',   '323 Advocate Lane',       'El Paso',      'TX', '79915', '915', '555-2286'),
    ('Maria',   'Patterson', '3445 Cheyenne Road',      'El Paso',      'TX', '79915', '915', '555-2291'),
    ('Kirk',    'DeGrasse',  '455 West Palm Ave',       'San Antonio',  'TX', '78284', '210', '555-2311'),
    ('Luke',    'Patterson', '877 145th Ave SE',        'Portland',     'OR', '97208', '503', '555-2316') 
    ]
    
    # Insert each customer record
    for customer in customers:
        c.execute("""
            INSERT INTO customers 
            (CustomerFirstName, CustomerLastName, CustomerStreetAddress, CustomerCity, CustomerState, CustomerZipCode, CustomerAreaCode, CustomerPhoneNumber) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, customer)

    conn.commit()
    print(f"\nMultiple customers successfully inserted into the table.")

    # Fetch and display all records in the customers table
    customersQuery = "SELECT * FROM customers"
    c.execute(customersQuery)
    print("\nThese are the customers in the customers table via fetchall:")
    print(c.fetchall())

    c.execute(customersQuery)
    print("\nThese are the customers in the customers table via for loop:")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]} Name: {row[1]} {row[2]}  Address: {row[3]}  CSZ: {row[4]} {row[5]} {row[6]}  Phone: {row[7]} {row[8]}")
  except sqlite3.IntegrityError as e:
    print(f"\nIntegrity Error: {e}")
    return None
  except sqlite3.DataError as e:
    print(f"\nData Error: {e}")
    return None
  except sqlite3.DatabaseError as e:
    print(f"\nDatabase Error: {e}")
    return None
  except sqlite3.OperationalError as e:
    print(f"\nOperational Error: {e}")
    return None
  except sqlite3.ProgrammingError as e:
    print(f"\nProgramming Error: {e}")
    return None
  except sqlite3.Error as e:
    print(f"\nGeneric Database Error: {e}")
    return None
