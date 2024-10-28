import sqlite3
# https://www.slingacademy.com/article/python-sqlite3-define-a-table-with-auto-incrementing-primary-key/
def insertProductRecords(conn):
  try:
    c = conn.cursor()
      
    # Insert data
    products = [
            ('AeroFlo ATB Wheels', '',  '', '~/content/images/01-AeroFlo-ATB-Wheels.jpg', 189, 40, 4),
            ('Clear Shade 85-T Glasses', '', '', '~/content/images/02-Clear-Shade-85-T-Glasses.jpg', 45, 14, 1),
            ('Cosmic Elite Road Warrior Wheels', '', '', '~/content/images/03-Cosmic-Elite-Road-Warrior-Wheels.jpg', 165, 22, 4),
            ('Cycle-Doc Pro Repair Stand', '', '', '~/content/images/04-Cycle-Doc-Pro-Repair-Stand.jpg', 166, 12, 1),
            ('Dog Ear Aero-Flow Floor Pump', '', '', '~/content/images/05-Dog-Ear-Aero-Flow-Floor-Pump.jpg', 55, 25, 1),
            ('Dog Ear Cycle Computer', '', '', '~/content/images/06-Dog-Ear-Cycle-Computer.jpg', 75, 20, 1),
            ('Dog Ear Helmet Mount Mirrors', '', '', '~/content/images/07-Dog-Ear-Helmet-Mount-Mirror.jpg', 7.45, 12, 1),
            ('Dog Ear Monster Grip Gloves', '', '', '~/content/images/08-Dog-Ear-Monster-Grip-Gloves.jpg', 15, 30, 1),
            ('Eagle FS-3 Mountain Bike', '', '', '~/content/images/09-Eagle-FS-3-Mountain-Bike.jpg', 1800, 8, 2),
            ('Eagle SA-120 Clipless Pedals', '', '', '~/content/images/10-Eagle-SA-120-Clipless-Pedals.jpg', 139.95, 20, 4), 
            ('Glide-O-Matic Cycling Helmet', '', '', '~/content/images/11-Glide-O-Matic-Cycling-Helmet.jpg', 125, 24, 1), 
            ('GT RTS-2 Mountain Bike', '', '', '~/content/images/12-GT-RTS-2-Mountain-Bike.jpg', 1650, 5, 2),
            ('HP Deluxe Panniers', '', '', '~/content/images/13-HP-Deluxe-Panniers.jpg', 39, 10, 1),
            ('King Cobra Helmet', '', '', '~/content/images/14-King-Cobra-Helmet.jpg', 139, 30, 1),
            ('Kool Breeze Rocket Top Jersey', '', '', '~/content/images/15-Kool-Breeze-Rocket-Top-Jersey.jpg', 4.99, 40, 4),
            ('Kryptonite Advanced 2000 U-Lock', '', '', '~/content/images/16-Kryptonite-Advanced-2000-U-Lock.jpg', 50, 20, 1),
            ('Nikoma Lok-Tight U-Lock', '', '', '~/content/images/17-Nikoma-Lok-Tight-U-Lock.jpg', 33, 12, 1),
            ('ProFormance ATB All-Terrain Pedal', '', '', '~/content/images/18-ProFormance-ATB-All-Terrain-Pedal.jpg', 28, 40, 4),
            ('ProFormance Toe Klips 2G', '', '', '~/content/images/19-ProFormance-Toe-Klips-2G.jpg', 28, 40, 4),
            ('Pro-Sport Dillo Shades', '', '', '~/content/images/20-Pro-Sport-Dillo-Shades.jpg', 82, 18, 1), 
            ('Road Warrior Hitch Pack', '',  '', '~/content/images/21-Road-Warrior-Hitch-Pack.jpg', 175, 6, 5), 
            ('Shinoman 105 SC Brakes', '', '', '~/content/images/22-Shinoman-105-SC-Brakes.jpg', 23.5, 16, 4),
            ('Shinoman Deluxe TX-30 Pedal', '', '', '~/content/images/23-Shinoman-Deluxe-TX-30-Pedal.jpg', 45, 60, 4),
            ('Shinoman Dura-Ace Headset', '', '', '~/content/images/24-Shinoman-Dura-Ace-Headset.jpg', 67.5, 20, 4), 
            ('StaDry Cycling Pants', '', '', '~/content/images/25-StaDry-Cycling-Pants.jpg', 69, 22, 3),
            ('TransPort Bicycle Rack', '', '', '~/content/images/26-TransPort-Bicycle-Rack.jpg', 27, 14, 1),
            ('Trek 9000 Mountain Bike', '', '', '~/content/images/27-Trek-9000-Mountain-Bike.jpg', 1200, 6, 2), 
            ('True Grip Competition Gloves', '', '', '~/content/images/28-True-Grip-Competition-Gloves.jpg', 22, 20, 1), 
            ('Turbo Twin Tires', '', '', '~/content/images/29-Turbo-Twin-Tires.jpg', 29, 18, 6),
            ('Ultimate Export 2G Car Rack', '',  '', '~/content/images/30-Ultimate-Export-2G-Car-Rack.jpg', 180, 8, 5),
            ('Ultra-2K Competition Tire', '', '', '~/content/images/31-Ultra-2K-Competition-Tire.jpg', 34, 22, 6),
            ('Ultra-Pro Rain Jacket', '', '', '~/content/images/32-Ultra-Pro-Rain-Jacket.jpg', 85, 30, 3), 
            ('Victoria Pro All Weather Tires', '', '', '~/content/images/33-Victoria-Pro-All-Weather-Tires.jpg', 54.95, 20, 4), 
            ('Viscount C-500 Wireless Bike Computer', '', '', '~/content/images/34-Viscount-C-500-Wireless-Bike-Computer.jpg', 49, 30, 1),
            ('Viscount CardioSport Sport Watch', '', '', '~/content/images/35-Viscount-CardioSport-Sport-Watch.jpg', 179, 12, 1), 
            ('Viscount Microshell Helmet', '', '', '~/content/images/36-Viscount-Microshell-Helmet.jpg', 36, 20, 1),
            ('Viscount Mountain Bike', '', '', '~/content/images/37-Viscount-Mountain-Bikes.jpg', 635, 5, 2),
            ('Viscount Tru-Beat Heart Transmitter', '', '', '~/content/images/38-Viscount-Tru-Beat-Heart-Transmitter.jpg', 47, 20, 1),
            ('Wonder Wool Cycle Socks', '', '', '~/content/images/39-Wonder-Wood-Cycle-Socks.jpg', 19, 30, 3),
            ('X-Pro All Weather Tires', '', '', '~/content/images/40-X-Pro-All-Weather-Tires.jpg', 24, 20, 6)
    ]
      
    # Insert each product record
    for product in products:
        c.execute("""
            INSERT INTO products 
            (ProductName, ProductDescShort, ProductDescLong, ProductImage, ProductPrice, ProductQty, CategoryID) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, product)

    conn.commit()
    print(f"\nMultiple products successfully inserted into the table.")

    # Fetch and display all records in the products table
    productsQuery = "SELECT * FROM products"
    c.execute(productsQuery)
    print("\nThese are the products in the products table via fetchall:")
    print(c.fetchall())

    c.execute(productsQuery)
    print("\nThese are the products in the products table via for loop:")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]} Name: {row[1]} Short Desc: {row[2]} Long Desc: {row[3]} Image: {row[4]} Price ${row[5]} Qty: {row[6]} CategoryID: {row[7]}")
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
