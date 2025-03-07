import sqlite3
# https://www.slingacademy.com/article/python-sqlite3-define-a-table-with-auto-incrementing-primary-key/
def insertProductVendorRecords(conn):
  try:
    c = conn.cursor()
      
    # Insert data
    productVendors = [
        (1, 4, 804, 6),
        (1, 9, 854.22, 7),						 
        (2, 6, 1269, 9),						 
        (2, 9, 1477.81, 7),						 
        (3, 7, 54.19, 10),
        (3, 9, 57.27, 6),
        (4, 6, 44.22, 10),
        (4, 9, 41.62, 14),
        (5, 7, 5.38, 10),
        (5, 9, 5.87, 9),
        (6, 2, 403.22, 3),
        (6, 9, 448.73, 7),
        (7, 2, 31.12, 3),
        (8, 8, 39.32, 10),
        (8, 9, 37.88, 14),
        (9, 3, 21.53, 4),
        (10, 2, 22.86, 3),
        (11, 3, 1076.62, 4),
        (11, 9, 1178.65, 7),
        (12, 1, 14.51, 2),
        (12, 6, 15.44, 10),
        (12, 9, 15.02, 14),
        (13, 1, 41.68, 2),
        (13, 6, 43.99, 10),
        (13, 9, 43.77, 14),
        (14, 6, 98.66, 9),
        (14, 9, 101.22, 14),
        (15, 4, 3.34, 6),
        (15, 6, 3.79, 10),
        (15, 9, 3.88, 14),
        (16, 4, 18.76, 6),
        (16, 6, 19.33, 10),
        (16, 9, 19.33, 14),
        (17, 1, 27.79, 2),
        (17, 6, 28.55, 10),
        (17, 9, 28.55, 14),
        (18, 2, 113.66, 3),
        (19, 2, 29.84, 3),
        (20, 7, 10.84, 10),
        (20, 9, 11.54, 6),
        (21, 7, 39.74, 10),
        (21, 9, 41.5, 9),
        (22, 10, 63.55, 15),
        (23, 6, 69.54, 15),
        (23, 9, 64.39, 14),
        (24, 6, 55.91, 15),
        (24, 7, 53.88, 10),
        (24, 9, 52.27, 14),
        (25, 9, 105.29, 14),
        (25, 10, 101.58, 15),
        (26, 3, 81.56, 4),
        (26, 6, 79.88, 15),
        (27, 3, 15.66, 4),
        (27, 6, 16.88, 10),
        (27, 9, 15.88, 14),
        (28, 3, 18.92, 4),
        (28, 6, 20.56, 10),
        (28, 9, 19.04, 14),
        (29, 5, 23.38, 8),
        (29, 6, 24.44, 10),
        (29, 9, 23.99, 14),
        (30, 8, 33.3, 12),
        (30, 9, 35.32, 8),
        (30, 10, 32.87, 15),
        (31, 7, 15.85, 15),
        (31, 8, 16.28, 12),
        (31, 9, 16.93, 7),
        (31, 10, 16.9, 9),
        (32, 6, 24.77, 15),
        (32, 7, 24.12, 10),
        (32, 8, 23.68, 12),
        (33, 6, 15.23, 15),
        (33, 8, 14.06, 12),
        (34, 6, 19.04, 9),
        (34, 9, 23.86, 3),
        (34, 10, 19.32, 10),
        (35, 6, 27.49, 9),
        (35, 9, 28.22, 6),
        (36, 6, 122.88, 10),
        (36, 7, 119.21, 10),
        (36, 9, 122.78, 14),
        (37, 2, 120.02, 3),
        (37, 6, 125.99, 10),
        (37, 9, 124.89, 14),
        (38, 9, 136.98, 6),
        (38, 10, 128.65, 15),
        (39, 6, 137.55, 7),
        (39, 7, 126.44, 10),
        (40, 6, 154.87, 10),
        (40, 9, 136.35, 14)
    ]
      
    # Insert each productVendor record
    for pv in productVendors:
        c.execute("""
            INSERT INTO ProductVendors 
            (ProductID, VendorID, ProductVendorWholesalePrice, ProductVendorDaysToDeliver) 
            VALUES (?, ?, ?, ?)
        """, pv)

    conn.commit()
    print(f"\nMultiple product vendors successfully inserted into the table.")

    # Fetch and display all records in the product vendors table
    pvQuery = "SELECT * FROM productVendors"
    c.execute(pvQuery)
    print("\nThese are the product vendors in the product vendors table via fetchall:")
    print(c.fetchall())

    c.execute(pvQuery)
    print("\nThese are the product vendors in the product vendors table via for loop:")
    rows = c.fetchall()
    for row in rows:
        print(f"Product ID: {row[0]} Vendor ID: {row[1]} Wholesale Price: ${row[2]} Days To Deliver: {row[3]}")
  except sqlite3.Error as e:
      print(f"\nProblem trying to insert database records: {e}")