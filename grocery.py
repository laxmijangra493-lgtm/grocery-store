import sqlite3
import sys

# Connect to database
conn = sqlite3.connect("cart.db")
cursor = conn.cursor()

print("\nhi  there 😊 , just you need a break \n , heres the break looks like👀\n welcome to OURCART🔥\n")
print("MENU 🍽")
print("🍟 Packaged Snacks ➡")
snack =["0. Potato Chips = ₹ 20" ,
 "1. Nachos =  ₹ 32" ,
 "2. Kurkure =  ₹ 30 " ,
 "3. Namkeen Mix =  ₹ 56" ,
 "4. Popcorn = ₹ 60",
 "5. Biscuits = ₹ 30 \n"]
for i in snack:
    print(i)
print(".................\n")

print("🍫 Sweet Snacks ➡")
sweet_snack =[
    "0. Chocolate Bars =  ₹ 45" ,
    "1. Wafer Rolls =  ₹ 30" ,
    "2. Candy / Toffees =  ₹ 200 , full satck" ,
    "3. Energy Bars =  ₹ 45"
    ]
sweet_snack_price =  [45 , 30 , 200 , 45]
for I in sweet_snack:
    print(I)

print(".................\n")

print("🥜 Healthy / Light Snacks ➡")
light_snack = [
        "0. Roasted Peanuts =  ₹ 50" ,
        "1. Almonds =  ₹ 300 per 250gm" ,  
        "2. Cashews =  ₹ 350 per 250gm" ,
        "3. Trail Mix =  ₹250" ,
        "4. Dry Fruits Pack =  ₹ 560" ,
        "5. Makhana (Fox Nuts) =  ₹ 260\n" ,
        ]
for x in light_snack:
    print(x)

print(".................\n")
        
print("🧃 Drinks ➡")
drinks = [
        "0. Soft Drinks = ₹ 100",
        "1. Fruit Juice = ₹ 70",
        "2. Flavoured Milk = ₹ 30",
        "3. Water Bottles = ₹ 20\n"
        ]
for h in drinks:
    print(h)
print("-----------------------")


# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT,
    price INTEGER
)
""")

# Function to add item
def add_item():
    name = input("Enter item name from above: ")  
    price = int(input("enter price mentioned above :"))  
    cursor.execute("INSERT INTO cart (item_name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    print(name , "✅ Item added to cart!")

# Function to view cart
def view_cart():

    cursor.execute("SELECT * FROM cart")
    items = cursor.fetchall()
    
    if not items:
        print("🛒 Cart is empty!")
        return
    print("\n🧾 Your Cart:")
    for item in items:
        print(f"ID: {item[0]} | {item[1]} - ₹{item[2]}")
    pay = input("enter 'pay' to pay your bill & '2' for continue: ")
    if pay == "pay":
            total =0 
            for item in items:
                total += item[2]
            print("please pay ₹" ,total)
            cursor.execute("DELETE FROM cart")
            conn.commit()
            sys.exit

    
# Function to remove item
def remove_item():
    view_cart()
    item_id = int(input("Enter ID to remove: "))
    
    cursor.execute("DELETE FROM cart WHERE id = ?", (item_id,))
    conn.commit()
    print("❌ Item removed!")

# Main menu
while True:
    print("\n==== 🛒 CART MENU ====")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        view_cart()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        print("👋 Exiting...")
        break
    else:
        print("❗ Invalid choice")


# Close connection
conn.close()
