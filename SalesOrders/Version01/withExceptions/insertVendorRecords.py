import sqlite3
# https://www.slingacademy.com/article/python-sqlite3-define-a-table-with-auto-incrementing-primary-key/
def insertVendorRecords(conn):
  try:
    c = conn.cursor()
      
    # Insert data
    vendors = [
        ('Shinoman, Incorporated',      '3042 19th Avenue South',   'Bellevue',     'WA', '98001', '(425) 888-1234', '(425) 888-1235', '#http://www.shinoman.com/#',        'Sales@Shiniman.com'),
        ('Viscount',                    '1911 Commerce Way',        'St. Louis',    'MO', '63127', '(314) 777-1234', '(314) 777-1235', '#http://www.viscountbikes.com/#',   'Orders@ViscountBikes.com'),
        ('Nikoma of America',           '88 Old North Road Ave',    'Ballard',      'WA', '91324', '(206) 666-1234', '(314) 666-1235', '#http://www.nikomabikes.com/#',     'BuyBikes@NikomaBikes.com'),
        ('ProFormance',                 '29 N. Quail St.',          'Albany',       'NY', '12012', '(518) 444-1234', '(518) 444-1235', '#http://www.ProFormBikes.com/#',    'Sales@ProFormBikes.com'),
        ('Kona, Incorporated',          'PO Box 10429',             'Redmond',      'WA', '98052', '(425) 333-1234', '(425) 333-1235', '#http://www.konabikes.com/#',       'Sales@KonaBikes.com'),
        ('Big Sky Mountain Bikes',      'Glacier Bay South',        'Anchorage',    'AK', '99209', '(907) 222-1234', '(907) 222-1235', '',                                   ''),
        ('Dog Ear',                     '575 Madison Ave.',         'New York',     'NY', '10003', '(212) 888-9876', '(212) 888-9877', '',                                  ''),
        ('Sun Sports Suppliers',        'PO Box 8082',              'Santa Monica', 'CA', '91003', '(310) 777-9876', '(310) 777-9877', '',                                  ''),
        ('Lone Star Bike Supply',       '7402 Kingman Drive',       'El Paso',      'TX', '79915', '(915) 666-9876', '(915) 666-9877', '',                                  ''),
        ('Armadillo Brand',             '12330 Side Road Lane',     'Dallas',       'TX', '75137', '(214) 444-9876', '(214) 444-9877', '#http://www.DilloBikes.com/#',      'BikeProducts@DilloBikes.com')
    ]
      
    # Insert each vendor record
    for vendor in vendors:
        c.execute("""
            INSERT INTO vendors 
            (VendorName, VendorStreetAddress, VendorCity, VendorState, VendorZipCode, VendorPhoneNumber, VendorFaxNumber, VendorWebPage, VendorEmailAddress) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, vendor)

    conn.commit()
    print(f"\nMultiple vendors successfully inserted into the table.")

    # Fetch and display all records in the vendors table
    vendorsQuery = "SELECT * FROM vendors"
    c.execute(vendorsQuery)
    print("\nThese are the vendors in the vendors table via fetchall:")
    print(c.fetchall())

    c.execute(vendorsQuery)
    print("\nThese are the vendors in the vendors table via for loop:")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]} Name: {row[1]} Address: {row[2]} CSZ: {row[3]} {row[4]} {row[5]} Phone: {row[6]} Fax: {row[7]} Web Page: {row[8]} Email: {row[9]} ")
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
