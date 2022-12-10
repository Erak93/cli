from data import stock
import datetime


print('1: List all items')
print('2: Search and replace order')
print('3: Browse by category')
print('4: Quit')

user_input = input("Choose between options 1,2,3,4 please: ")
# {"state": "Almost new", "category": "Keyboard", "warehouse": 1, 
#  "date_of_stock": "2020-05-06 08:28:12"}
while True:
    if user_input == '1':
        # This means if the value of the key warehouse is equal to 1. Loop through the item in the list stock and insert  in the list the values of key state and category
        warehouse1 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 1]
        warehouse2 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 2]

        # Here we are using sets in order to avoid duplicates in the lists. After that we are using "|" to make set1 union set2
        for item in set(warehouse1) | set(warehouse2):
            print('')
            print('-', item)
        print(f"Total items in warehouse1: {len(warehouse1)}")
        print(f"Total items in warehouse2: {len(warehouse2)}")
        print('')
        print('Thank you for your visit.')
        break
# {"state": "Almost new", "category": "Keyboard", "warehouse": 1, 
#  "date_of_stock": "2020-05-06 08:28:12"}
    if user_input == '2':
        item_name = input('What is the name of the item? ')
        wh1 = [item['date_of_stock'] for item in stock if item.get('warehouse') == 1 and f"{item['state']} {item['category']}".lower() == item_name.lower()]
        wh2 = [item['date_of_stock'] for item in stock if item.get('warehouse') == 2 and f"{item['state']} {item['category']}".lower() == item_name.lower()]
    if len(wh1 + wh2) == 0:
        print("Sorry, we do not have that item in stock.")
    else:
        today = datetime.datetime.now()
        for item in wh1:
            print(f"- Warehouse1 (in stock {(today - datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')).days} days)")
        for item in wh2:
            print(f"- Warehouse2 (in stock {(today - datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')).days} days)")

        break