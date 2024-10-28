# https://www.sqliz.com/sqlite-ref/
#
# https://www.sqlitetutorial.net/
#

import sqlite3
import createConnection           as dbc
import q1   # Category      table record count
import q2   # Customer      table record count
import q3   # Employee      table record count
import q4   # Orders        table record count
import q5   # OrderDetails  table record count
import q6   # Products      table record count
import q7   # ProductVendors table record count
import q8   # Vendors       table record count
import q9   # Customer first name starts with a vowel (all)
import q10  # Customer first name starts with a vowel (upper)
import q11
import q12
import q13
import q14
import q15
import q16
import q17
import q18
import q19

def main():
    # Attempt to connect to database
  conn = dbc.createConnection()

  # Run queries to show number of
  # records in each database table.
  q1.categoriesRecordCount(conn)
  q2.customersRecordCount(conn)
  q3.employeesRecordCount(conn)
  q4.orderDetailsRecordCount(conn)
  q5.ordersRecordCount(conn)
  q6.productsRecordCount(conn)
  q7.productVendorsRecordCount(conn)
  q8.vendorsRecordCount(conn)

  # Show query to show all employees with
  # whose first name starts with a vowel
  # (the "bad way").
  q9.vowelBadWay1(conn)

  # Show query to show all employees with
  # whose first name starts with a vowel
  # (the "good way").
  q10.vowelGoodWay1(conn)

  # Show query to show all employees with
  # whose last name ends with a vowel.
  q11.vowelBadWay2(conn)

  # Show query to show all employees with
  # whose last name ends with a vowel.
  q12.vowelGoodWay2(conn)

  # Show query to show all employees with
  # whose first name starts with a vowel
  # AND whose last name ends with a vowel.
  q13.vowelAND(conn)

  # Show query to show all employees with
  # whose first name starts with a vowel
  # OR whose last name ends with a vowel.
  q14.vowelOR(conn)

  # Show a query to select all category descriptions, product names,
  # and retail prices.
  #
  # Sort results by category description in ascending order, then
  # retail price in descending order.
  q15.runQ15(conn)

  # Show a query to select all category descriptions, product names,
  # and retail prices, but only for a category of "Bikes" or "Wheels".
  #
  # Sort results by category description in ascending order, then
  # retail price in descending order.
  q16.runQ16(conn)
  
  # Show a query to select all category descriptions, product names,
  # and retail prices, but only for a category NOT "Bikes" or "Wheels".
  #
  # Sort results by category description in ascending order, then
  # retail price in descending order.
  q17.runQ17(conn)

  # Show a query to select all category descriptions, product names,
  # product price, wholesale price, and vendor name. Sort results by
  # category description in ascending order, then vendor name in
  # descending order, then product price in descending order, then
  # wholesale price in descending order.
  q18.runQ18(conn)

  # Do a Union query to combine all customer first and last names
  # with all employee first and last names.
  q19.runQ19(conn)
  
if (__name__ == "__main__"):
  main()