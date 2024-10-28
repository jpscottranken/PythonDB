# classes/tables/orderDetails.py
import sqlite3

from classes.table import Table

class OrderDetail(Table):
    def __init__(self, db):
        super().__init__(db, "OrderDetails")

    def create(self, orderID, productID,
               orderDetailQuotedPrice,
               orderDetailQuantityOrdered):
        fields = ["OrderID", "ProductID",
                  "OrderDetailQuotedPrice",
                  "OrderDetailQuantityOrdered"]
        values = [orderID, productID,
                  orderDetailQuotedPrice,
                  orderDetailQuantityOrdered]
        super().create(fields, values)

    def delete(self, recordID):
        super().delete({"OrderID"   : recordID,
                        "ProductID" : recordID})
    
    def getRecordById(self, recordID):
        return super().getRecordById(recordID, ("OrderID", "ProductID"))
