# classes/tables/vendor.py
import sqlite3

from classes.table import Table

class Vendor(Table):
    def __init__(self, db):
        super().__init__(db, "Vendors")

    def create(self, vendorName, vendorStreetAddress,
               vendorCity, vendorState, vendorZipCode,
               vendorPhoneNumber, vendorFaxNumber,
               vendorWebPage, vendorEmailAddress):
        fields = ["VendorName", "VendorStreetAddress",
                  "VendorCity", "VendorState", "VendorZipCode",
                  "VendorPhoneNumber", "VendorFaxNumber",
                  "VendorWebPage", "VendorEmailAddress"]
        values = [vendorName, vendorStreetAddress,
                  vendorCity, vendorState, vendorZipCode,
                  vendorPhoneNumber, vendorFaxNumber,
                  vendorWebPage, vendorEmailAddress]
        super().create(fields, values)

    def delete(self, recordID):
        super().delete({"VendorID": recordID})
    
    def getRecordById(self, recordID):
        return super().getRecordById(recordID, "VendorID")
