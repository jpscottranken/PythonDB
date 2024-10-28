import sqlite3

# Create the eight tables & DB connection
# in the SalesOrders DB
import createDBconnection           as dbc
import createCategoriesTable        as cat
import createCustomersTable         as cus
import createEmployeesTable         as emp
import createVendorsTable           as ven
import createProductsTable          as pro
import createProductVendorsTable    as proven
import createOrdersTable            as ord
import createOrderDetailsTable      as ordet

# Fill each of the 8 tables with records
import insertCategoryRecords        as icat
import insertCustomerRecords        as icus
import insertEmployeeRecords        as iemp
import insertVendorRecords          as iven
import insertProductRecords         as ipro
import insertProductVendorRecords   as iproven
import insertOrderRecords           as iord
import insertOrderDetailsRecords    as iordet

def main():
  # Attempt to connect to database
  conn = dbc.createConnection()

  # Attempt to create categories table
  cat.createCategoriesTable(conn)

  # Attempt to create customers table
  cus.createCustomersTable(conn)

  # Attempt to create employees table
  emp.createEmployeesTable(conn)

  # Attempt to create vendors table
  ven.createVendorsTable(conn)

  # Attempt to create products table
  pro.createProductsTable(conn)

  # Attempt to create ProductVendors table
  proven.createProductVendorsTable(conn)

  # Attempt to create Orders table
  ord.createOrdersTable(conn)

  # Attempt to create OrderDetails table
  ordet.createOrderDetailsTable(conn)

  # Attempt to display all tables in SalesOrders DB
  # https://www.geeksforgeeks.org/how-to-list-tables-using-sqlite3-in-python/
  # create a SELECT query
  sqlQuery = """
      SELECT name FROM sqlite_master  
      WHERE type='table'
  """
  
  # Create a cursor object
  c = conn.cursor()

  # Execute the sqlQuery
  c.execute(sqlQuery)

  print("\nThese Were The Tables Created In The SalesOrders Database")
  # Print the results
  print(c.fetchall())

  # Attempt to insert records into the categories table
  print("\n")
  icat.insertCategoryRecords(conn)

  # Attempt to insert records into the customers table
  print("\n")
  icus.insertCustomerRecords(conn)

  # Attempt to insert records into the employees table
  print("\n")
  iemp.insertEmployeeRecords(conn)

  # Attempt to insert records into the vendors table
  print("\n")
  iven.insertVendorRecords(conn)

  # Attempt to insert records into the products table
  print("\n")
  ipro.insertProductRecords(conn)

  # Attempt to insert records into the productVendors table
  print("\n")
  iproven.insertProductVendorRecords(conn)

  # Attempt to insert records into the orders table
  print("\n")
  iord.insertOrderRecords(conn)

  # Attempt to insert records into the orderDetails table
  print("\n")
  iordet.insertOrderDetailsRecords(conn)

if (__name__ == "__main__"):
  main()
