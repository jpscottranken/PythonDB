# main.py
from classes.table                  import Table
from classes.database               import Database
from classes.tables.category        import Category
from classes.tables.customer        import Customer
from classes.tables.employee        import Employee
from classes.tables.orderDetail     import OrderDetail
from classes.tables.order           import Order
from classes.tables.product         import Product
from classes.tables.productVendor   import ProductVendor
from classes.tables.vendor          import Vendor

def displayMainMenu():
    print("\nMain Menu")
    print("1. Categories")
    print("2. Customers")
    print("3. Employees")
    print("4. OrderDetails")
    print("5. Orders")
    print("6. Products")
    print("7. ProductVendors")
    print("8. Vendors")
    print("9. Exit")
    return input("\nSelect a table (1 - 8) or 9 to Exit: ")

def displayCRUDMenu():
    print("\nCRUD Operations")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Back to Main Menu")
    return input("\nSelect an operation (1 - 5): ")

def handleTable(table):
    while True:
        operation = displayCRUDMenu()
        if operation == "1":
            if isinstance(table, Category):
                description         = input("Enter Category Description: ")
                table.create(description)
            elif isinstance(table, Customer):
                firstName           = input("Enter Customer First Name: ")
                lastName            = input("Enter Customer Last Name: ")
                street              = input("Enter Customer Street Address: ")
                city                = input("Enter Customer City: ")
                state               = input("Enter Customer State: ")
                zipCode             = input("Enter Customer Zip Code: ")
                areaCode            = input("Enter Customer Area Code: ")
                phone               = input("Enter Customer Phone Number: ")
                table.create(firstName, lastName, street, 
                             city, state, zipCode, 
                             areaCode, phone)
            elif isinstance(table, Employee):
                firstName           = input("Enter Employees First Name: ")
                lastName            = input("Enter Employees Last Name: ")
                street              = input("Enter Employees Street Address: ")
                city                = input("Enter Employees City: ")
                state               = input("Enter Employees State: ")
                zipCode             = input("Enter Employees Zip Code: ")
                areaCode            = input("Enter Employees Area Code: ")
                phone               = input("Enter Employees Phone Number: ")
                table.create(firstName, lastName, street, 
                             city, state, zipCode, areaCode, phone)
            elif isinstance(table, OrderDetail):
                orderid             = input("Enter OrderDetails OrderID: ")
                productid           = input("Enter OrderDetails ProductID: ")  
                quotedPrice         = input("Enter OrderDetails Quoted Price: ") 
                qtyOrdered          = input("Enter OrderDetails Quantity Ordered: ")            
                table.create(orderid, productid, 
                             quotedPrice, qtyOrdered)
            elif isinstance(table, Order):
                orderDate           = input("Enter Order Order Date: ")
                orderShipDate       = input("Enter Order Ship Date: ")
                customerID          = input("Enter Order CustomerID: ")
                employeeID          = input("Enter Order EmployeeID: ")
                table.create(orderDate, orderShipDate, 
                             customerID, employeeID)
            elif isinstance(table, Product):
                productName         = input("Enter Product Name: ")
                productDescShort    = input("Enter Product Description Short: ")
                productDescLong     = input("Enter Product Description Long: ")
                productImage        = input("Enter Product Image URL: ")
                productPrice        = input("Enter Product Price: ")
                productQty          = input("Enter Product Quantity: ")
                categoryID          = input("Enter CategoryID: ")
                table.create(productName,
                             productDescShort, productDescLong,
                             productImage, productPrice,
                             productQty, categoryID)
            elif isinstance(table, ProductVendor):
                productID           = input("Enter ProductVendors ProductID: ")
                vendorID            = input("Enter ProductVendors VendorID: ")
                wholesalePrice      = input("Enter ProductVendors Product Vendor Wholesale Price: ")
                daysToDeliver       = input("Enter ProductVendors Product Vendors Days To Deliver: ")
                table.create(productID, vendorID,
                             wholesalePrice, daysToDeliver)
            elif isinstance(table, Vendor):
                vendorName          = input("Enter Vendor Name: ")     
                vendorStreetAddress = input("Enter Vendor Street Address: ")
                vendorCity          = input("Enter Vendor City: ")
                vendorState         = input("Enter Vendor State: ")
                vendorZipCode       = input("Enter Vendor Zip Code: ")
                vendorPhoneNumber   = input("Enter Vendor Phone Number: ")
                vendorFaxNumber     = input("Enter Vendor Fax Number: ")
                vendorWebPage       = input("Enter Vendor Web Page: ")
                vendorEmailAddress  = input("Enter Vendor Email Address: ")
                table.create(vendorName, vendorStreetAddress,
                             vendorCity, vendorState, vendorZipCode,
                             vendorPhoneNumber, vendorFaxNumber,
                             vendorWebPage, vendorEmailAddress)
        elif operation == "2":
            rows = table.read()
            for row in rows:
                print(row)
        elif operation == "3":
            recordID = input("Enter ID to update: ")
            currentRecord = table.getRecordById(recordID)
            
            if not currentRecord:
                print("Record not found.")
                continue
            
            if isinstance(table, Category):
              newDescription        = input(f"Enter new Category Description [{currentRecord['CategoryDescription']}]: ") or currentRecord['CategoryDescription']
              table.update({"CategoryID": recordID}, {"CategoryDescription": newDescription})
            elif isinstance(table, Customer):
              newFirstName          = input(f"Enter New Customer First Name [{currentRecord['CustomerFirstName']}]: ") or currentRecord['CustomerFirstName']
              newLastName           = input(f"Enter New Customer Last Name [{currentRecord['CustomerLastName']}]: ") or currentRecord['CustomerLastName']
              newStreet             = input(f"Enter New Customer Street Address [{currentRecord['CustomerStreetAddress']}]: ") or currentRecord['CustomerStreetAddress']
              newCity               = input(f"Enter New Customer City [{currentRecord['CustomerCity']}]: ") or currentRecord['CustomerCity']
              newState              = input(f"Enter New Customer State [{currentRecord['CustomerState']}]: ") or currentRecord['CustomerState']
              newZipCode            = input(f"Enter New Customer Zip Code [{currentRecord['CustomerZipCode']}]: ") or currentRecord['CustomerZipCode']
              newAreaCode           = input(f"Enter New Customer Area Code [{currentRecord['CustomerAreaCode']}]: ") or currentRecord['CustomerAreaCode']
              newPhone              = input(f"Enter New Customer Phone Number [{currentRecord['CustomerPhoneNumber']}]: ") or currentRecord['CustomerPhoneNumber']
              table.update({"CustomerID": recordID}, 
                           {"CustomerFirstName"     : newFirstName, 
                            "CustomerLastName"      : newLastName,
                            "CustomerStreetAddress" : newStreet,
                            "CustomerCity"          : newCity,
                            "CustomerState"         : newState,
                            "CustomerZipCode"       : newZipCode,
                            "CustomerAreaCode"      : newAreaCode,
                            "CustomerPhoneNumber"   : newPhone})
            elif isinstance(table, Employee):
              newFirstName          = input(f"Enter New Employee First Name [{currentRecord['EmployeeFirstName']}]: ") or currentRecord['EmployeeFirstName']
              newLastName           = input(f"Enter New Employee Last Name [{currentRecord['EmployeeLastName']}]: ") or currentRecord['EmployeeLastName']
              newStreet             = input(f"Enter New Employee Street Address [{currentRecord['EmployeeStreetAddress']}]: ") or currentRecord['EmployeeStreetAddress']
              newCity               = input(f"Enter New Employee City [{currentRecord['EmployeeCity']}]: ") or currentRecord['EmployeeCity']
              newState              = input(f"Enter New Employee State [{currentRecord['EmployeeState']}]: ") or currentRecord['EmployeeState']
              newZipCode            = input(f"Enter New Employee Zip Code [{currentRecord['EmployeeZipCode']}]: ") or currentRecord['EmployeeZipCode']
              newAreaCode           = input(f"Enter New Employee Area Code [{currentRecord['EmployeeAreaCode']}]: ") or currentRecord['EmployeeAreaCode']
              newPhone              = input(f"Enter New Employee Phone Number [{currentRecord['EmployeePhoneNumber']}]: ") or currentRecord['EmployeePhoneNumber']
              table.update({"EmployeeID": recordID}, 
                           {"EmployeeFirstName"     : newFirstName, 
                            "EmployeeLastName"      : newLastName,
                            "EmployeeStreetAddress" : newStreet,
                            "EmployeeCity"          : newCity,
                            "EmployeeState"         : newState,
                            "EmployeeZipCode"       : newZipCode,
                            "EmployeeAreaCode"      : newAreaCode,
                            "EmployeePhoneNumber"   : newPhone})
            elif isinstance(table, OrderDetail):
              newQuotedPrice        = input(f"Enter New OrderDetail [{currentRecord['OrderDetailQuotedPrice']}]: ") or currentRecord['OrderDetailQuotedPrice']
              newQtyOrdered         = input(f"Enter New OrderDetail [{currentRecord['OrderDetailQuantityOrdered']}]: ") or currentRecord['OrderDetailQuantityOrdered']
              table.update({"OrderID": recordID, "ProductID": recordID},
                           {"OrderDetailQuotedPrice"        : newQuotedPrice,
                            "OrderDetailQuantityOrdered"    : newQtyOrdered})
            elif isinstance(table, Order):
              newOrderDate          = input(f"Enter New Order [{currentRecord['OrderDate']}]: ") or currentRecord['OrderDate']
              newOrderShipDate      = input(f"Enter New Order [{currentRecord['OrderShipDate']}]: ") or currentRecord['OrderShipDate']
              table.update({"OrderID"       : recordID},
                           {"OrderDate"     : newOrderDate, 
                            "OrderShipDate" : newOrderShipDate})
            elif isinstance(table, Product):
              newProductName        = input("Enter Product Name: [{currentRecord['ProductName']}]: ") or currentRecord['ProductName']
              newProductDescShort   = input("Enter Product Description Short: [{currentRecord['ProductDescShort']}]: ") or currentRecord['ProductDescShort']
              newProductDescLong    = input("Enter Product Description Long: [{currentRecord['ProductDescLong']}]: ") or currentRecord['ProductDescLong']
              newProductImage       = input("Enter Product Image URL: [{currentRecord['ProductImage']}]: ") or currentRecord['ProductImage']
              newProductPrice       = input("Enter Product Price: [{currentRecord['ProductPrice']}]: ") or currentRecord['ProductPrice']
              newProductQty         = input("Enter Product Quantity: [{currentRecord['ProductQty']}]: ") or currentRecord['ProductQty']
              newCategoryID         = input("Enter CategoryID: [{currentRecord['CategoryID']}]: ") or currentRecord['CategoryID']
              table.update({"ProductID"         : recordID},
                           {"ProductName"       : newProductName, 
                            "ProductDescShort"  : newProductDescShort,
                            "ProductDescShort"  : newProductDescLong,
                            "ProductImage"      : newProductImage,
                            "ProductPrice"      : newProductPrice,
                            "ProductQty"        : newProductQty,
                            "CategoryID"        : newCategoryID})
            elif isinstance(table, ProductVendor):
              newWholesalePrice     = input(f"Enter New ProductVendors [{currentRecord['ProductVendorWholesalePrice']}]: ") or currentRecord['ProductVendorWholesalePrice']
              newDaysToDeliver      = input(f"Enter New ProductVendors [{currentRecord['ProductVendorDaysToDeliver']}]: ") or currentRecord['ProductVendorDaysToDeliver']
              table.update({"ProductID": recordID, "VendorID"   : recordID},
                           {"ProductVendorWholesalePrice"       : newWholesalePrice,
                            "ProductVendorDaysToDeliver"        : newDaysToDeliver})
            elif isinstance(table, Vendor):
              newVendorName         = input("Enter Vendor Name: [{currentRecord['VendorName']}]: ") or currentRecord['VendorName']
              newVendorStreet       = input("Enter Vendor Street: [{currentRecord['VendorStreetAddress']}]: ") or currentRecord['VendorStreetAddress']
              newVendorCity         = input("Enter Vendor City: [{currentRecord['VendorCity']}]: ") or currentRecord['VendorCity']
              newVendorState        = input("Enter Vendor State: [{currentRecord['VendorState']}]: ") or currentRecord['VendorState']
              newVendorZip          = input("Enter Vendor ZipCode: [{currentRecord['VendorZipCode']}]: ") or currentRecord['VendorZipCode']
              newVendorPhone        = input("Enter Vendor Phone Number: [{currentRecord['VendorPhoneNumber']}]: ") or currentRecord['VendorPhoneNumber']
              newVendorFax          = input("Enter Vendor Fax Number: [{currentRecord['VendorFaxNumber']}]: ") or currentRecord['VendorFaxNumber']
              newVendorWeb          = input("Enter Vendor Web Address: [{currentRecord['VendorWebPage']}]: ") or currentRecord['VendorWebPage']
              newVendorEmail        = input("Enter Vendor Email Address: [{currentRecord['VendorEmailAddress']}]: ") or currentRecord['VendorEmailAddress']
              table.update({"VendorID"              : recordID},
                           {"VendorName"            : newVendorName,
                            "VendorStreetAddress"   : newVendorStreet, 
                            "VendorCity"            : newVendorCity,
                            "VendorState"           : newVendorState, 
                            "VendorZipCode"         : newVendorZip,
                            "VendorPhoneNumber"     : newVendorPhone,
                            "VendorFaxNumber"       : newVendorFax,
                            "VendorWebPage"         : newVendorWeb,
                            "VendorEmailAddress"    : newVendorEmail})
        elif operation == "4":
            recordID = input("Enter ID to delete: ")
            table.delete(recordID)
        elif operation == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    db = Database()

    while True:
        tableChoice = displayMainMenu()
        if tableChoice     == "1":
            handleTable(Category(db))
        elif tableChoice   == "2":
            handleTable(Customer(db))
        elif tableChoice   == "3":
            handleTable(Employee(db))
        elif tableChoice   == "4":
            handleTable(OrderDetail(db))
        elif tableChoice   == "5":
            handleTable(Order(db))
        elif tableChoice   == "6":
            handleTable(Product(db))
        elif tableChoice   == "7":
            handleTable(ProductVendor(db))
        elif tableChoice   == "8":
            handleTable(Vendor(db))
        elif tableChoice   == "9":
            print("Exiting the application.")
            db.close()
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()