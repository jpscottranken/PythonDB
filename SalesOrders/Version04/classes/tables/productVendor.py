# classes/tables/productVendors.py
import sqlite3

from classes.table import Table

class ProductVendor(Table):
    def __init__(self, db):
        super().__init__(db, "ProductVendors")

    def create(self, productID, vendorID,
               productVendorWholesalePrice,
               productVendorDaysToDeliver):
        fields = ["ProductID", "VendorID",
                  "ProductVendorWholesalePrice",
                  "ProductVendorDaysToDeliver"]
        values = [productID, vendorID,
                  productVendorWholesalePrice,
                  productVendorDaysToDeliver]
        super().create(fields, values)

    def delete(self, recordID):
        super().delete({"ProductID" : recordID,
                        "VendorID"  : recordID})
    
    def getRecordById(self, recordID):
        return super().getRecordById(recordID, ("ProductID", "VendorID"))
