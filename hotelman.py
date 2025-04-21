

# menu={
#     'fast_food':{
#     'Pizza':40,
#     'Pasta':50,
#     'Burger':60,
#     'Salad':70,
#     'Coffee':80,
#     'Vada Pav':20,
#     'Dabeli':25,
#     'Pav Bhaji':70
#     },
#     'drinks':{
#     'Masala Soda':30,
#     'Lassi (Sweet/Salted)' :60,
#     'Cold Coffee (with ice cream)' :100,
#     'Falooda' :80
#     }
# }
# print("WELCOME TO JK HOTEL...!!! jay shree ram")
# for category, items in menu.items():
#     print(f"--- {category.upper()} ---")
#     for item, price in items.items():
#         print(f"{item} - ₹{price}")
#     print()  # Add a blank line after each category

# all_items = {**menu['fast_food'], **menu['drinks']}

# order_total=0

# item1 = input("Enter the name of item you want to order: ")
# if item1 in all_items :
#     order_total +=all_items[item1]
#     print(f"Your item1 {item1} has been added to your order")

# else:
#     print(f"Ordered item{item1} isn't available ")

# another_order = input("Do you want to add anything else? (yes/no) ")
# if another_order =="yes":
#     item2 = input("Enter the name of 2nd item: ")
#     if item2 in all_items:
#         order_total += all_items[item2]
#         print(f"Your item2 {item2} has been added to your order")
#     else:
#      print(f"Ordered item {item2} isn't available ")

# print(f"Your bill is {order_total} is to pay")








