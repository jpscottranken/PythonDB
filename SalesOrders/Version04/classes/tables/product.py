# classes/tables/product.py
import sqlite3

from classes.table import Table

class Product(Table):
    def __init__(self, db):
        super().__init__(db, "Products")

    def create(self, productName, productDescShort, productDescLong,
               productImage, productPrice, productQty, categoryID):
        fields = ["ProductName", "ProductDescShort", "ProductDescLong",
                  "ProductImage", "ProductPrice", "ProductQty", "CategoryID"]
        values = [productName, productDescShort, productDescLong,
                  productImage, productPrice, productQty, categoryID]
        super().create(fields, values)

    def delete(self, recordID):
        super().delete({"ProductID": recordID})
    
    def getRecordById(self, recordID):
        return super().getRecordById(recordID, "ProductID")

