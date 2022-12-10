from data import stock
import datetime
import collections


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
            print() # this makes a space in between items (i in set)
            print('-', item) # this is is printing every item with a "-" in front
        print(f"Total items in warehouse1: {len(warehouse1)}") # these two lines are printing the length of the original lists. Duplicates are included
        print(f"Total items in warehouse2: {len(warehouse2)}")
        print('')
        print('Thank you for your visit.')
        break # we need the break here or the loop will repeat itself (148+152) times

    if user_input == '2':
        warehouse1 = [ f"{item['state'].lower()} {item['category'].lower()}" for item in stock if item.get('warehouse') == 1]
        warehouse2 = [ f"{item['state'].lower()} {item['category'].lower()}" for item in stock if item.get('warehouse') == 2]
        item_name = input('What is the name of the item? ')
        # in wh1 and wh2 the value of key date of stock is inserted in list if the combination of values of keys state and category match the input
        # the only difference in these two lines is the value of the key warehouse
        wh1 = [item['date_of_stock'] for item in stock if item.get('warehouse') == 1 and f"{item['state']} {item['category']}".lower() == item_name.lower()]
        wh2 = [item['date_of_stock'] for item in stock if item.get('warehouse') == 2 and f"{item['state']} {item['category']}".lower() == item_name.lower()]
    # if the sum of the len of the two list is equal to 0 (meaning that the for loops in wh1 and wh2 did not find anything) it means that there is no item in warehouse
        if len(wh1 + wh2) == 0:
            print("Sorry, we do not have that item in stock.")
        else:
            today = datetime.datetime.now() # this gives today's date
            for item in wh1:
                # this is returning the name of the item and the difference between today's date and date saves in the key date of stock
                print(f"- 1 {item_name} found in warehouse1 (in stock {(today - datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')).days} days)")
            for item in wh2:
                print(f"- 1 {item_name} found in warehouse2 (in stock {(today - datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')).days} days)")
        
        if len(wh1+wh2)!=0:
            # this is calculating the sum of elements present in lists warehouse1 + warehouse2 with the same name of item name
                maximum_availability=warehouse1.count(item_name.lower())+warehouse2.count(item_name.lower())# .lower() because items in those list are inserted like "Funny Headphones"
                print (f' The maximum availability for your order is: {maximum_availability} items')
                # this needs to be an integer in order to be compared with maximum availability
                buy_decision_one=int(input("How many items would you like to order? Type here: "))
                
                if buy_decision_one <= maximum_availability and buy_decision_one >0:
                        print(f'You just ordered {buy_decision_one} {item_name}. Thank you for your purchase!')
                elif buy_decision_one==0:
                        print(f'Your order can not be processed. Thank you for your visit!')
                elif buy_decision_one>maximum_availability:
                    # buy decision two is necessary in case the user tries to request more items than maximum availability
                        buy_decision_two=input("Not enough items in warehouse. Would you like to order the maximum availability instead? Type yes or no please. ")
                        if buy_decision_two=="yes":
                            print (f'you just ordered {maximum_availability} {item_name}. Thank you for your visit')
                        elif buy_decision_two=="no":
                            print(f'Thank you for your visit')
                break

    if user_input=='3':
        # this is a comprehensive list of all the categories in warehouse 1 and 2 combined
        warehouse=[item["category"] for item in stock if item.get('warehouse') == 1 or 2]
        # this list is used to append the unique categories (keys) collected by the for loop two lines below
        category_list=[]
        # this creates a dictionary with categories as keys and quantities as values. Warehouse 1 and 2 are merged
        dictionary_group_category=dict(collections.Counter(warehouse))
        # this for loop is generating an ordinated list of categories with quantities. Since enumerate needs two elements (k,v) are grouped into 1
        for i,(k,v) in enumerate(dictionary_group_category.items()):
            print(f'{i} {k} ({v})')
            category_list.append(k)
        # this generate the index number we will use as filter to browse through the catergories in category list    
        browse_choice=int(input("Please type the number in front of the category to browse the available items: "))
        # this is the search filter
        category_search_filter=category_list[browse_choice]
        # the set converts the list to show one item only once per warehouse
        filtered_items=set([f'{item["state"]} {item["category"]}, warehouse: {item["warehouse"]}' for item in stock if item.get('category')==category_search_filter])
        print(*filtered_items,sep="\n")
        print("Thank you for your visit!")
        break
    # write condition 4           

        
        