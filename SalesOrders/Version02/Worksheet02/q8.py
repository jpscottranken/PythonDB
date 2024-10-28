import sqlite3

def runQ8(conn):
  # Show a query that shows only the vendor name and 
  # product wholesale price, but only for those vendor 
  # names that either start with an 's' or end with an
  # 's', and have a wholesale price between 10 and 20.
  # 
  # Sort the results based on wholesale price descending 
  # then by vendor name ascending. 
  try:
    c = conn.cursor()

    q8Query = """
                  SELECT	v.VendorName,
	                        pv.ProductVendorWholesalePrice
                  FROM	vendors v
                  JOIN	productvendors pv	ON v.VendorID = pv.VendorID
                  WHERE	(v.VendorName LIKE 's%' or v.VendorName LIKE '%s')
                  AND 	(pv.ProductVendorWholesalePrice BETWEEN 10 and 20)
                  ORDER BY pv.ProductVendorWholesalePrice DESC                
              """
    c.execute(q8Query)   
    print("\nQ8. Those Vendors That Meet The Criteria:")
    print(c.fetchall())
  except sqlite3.Error as e:
    print(f"\nQ8. Problem trying to display database records: {e}")
    return None