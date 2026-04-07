# cart system:-
import sqlite3
import sys

con = sqlite3.connect("store.db")
cursor = con.cursor()

# chich phele choice price hum de!
snack = [
    "Kurkure Masala Munch" ,
"Kurkure Chilli Chatka",
"Kurkure Puffcorn Cheese",
"Lay’s Classic Salted",
"Lay’s Magic Masala",
"Lay’s Cream & Onion",
"Lay’s American Style Cream & Onion",
"Bingo Mad Angles",
"Bingo Tedhe Medhe",
"Doritos Nacho Cheese",
"Doritos Sweet Chilli",
"Haldiram’s Aloo Bhujia",
"Haldiram’s Moong Dal",
"Haldiram’s Navratan Mixture",
"Haldiram’s Khatta Meetha",
"Bikaji Bhujia",
"Bikaji Aloo Bhujia",
"Too Yumm! Veggie Chips",
"Balaji Wafers Chips",
"Uncle Chipps Spicy Treat"
]
price ="₹",  20
def add_item():
    choice = input("enter your snack from above list: ")
    if(choice != snack):
        print("so sorry we have not this item😔")
        sys.exit()
    elif(choice == snack):
        print(choice ,"✅ item added to your cart sucessfully ")
        cursor.execute("INSERT INTO cart (item_name, price) VALUES (?, ?)", (choice, price))
    else:
        sys.exit()

    pay = input("enter 'pay' to pay on COD , OR , 'con' to continue shoping: ")
    if pay == "con":
        return
# veiw = input("if you wanted to view cart enter 'view' else enter 'no' for continue shoping : ")
# if (veiw == "view"):
#     def view_cart():
#         cursor.execute("SELECT * FROM cart")
#         items = cursor.fetchall()
#         if not items:
#             print("🛒 Cart is empty!")
#         return
# else:
#     def add_item():
#         Choice = input("enter your snack from above list: ")
