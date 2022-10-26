


warehouse1 = ["Brand new laptop", "Exceptional monitor", "Cheap tablet", "Funny laptop", "Second hand smartphone", "Brand new smartphone", "Cheap router", "Second hand laptop", "Elegant tablet", "Funny tablet", "Second hand headphones", "Exceptional tablet", "Brand new smartphone", "Cheap mouse", "Elegant headphones", "Brand new headphones", "Second hand smartphone", "High quality smartphone", "Brand new keyboard", "Second hand headphones", "Elegant router", "Exceptional router", "Second hand smartphone", "Exceptional monitor", "Almost new tablet", "High quality monitor", "Second hand monitor", "Brand new keyboard", "Almost new keyboard", "High quality headphones", "Elegant laptop", "Elegant router", "Almost new monitor", "Almost new headphones", "Second hand keyboard", "Brand new tablet", "Elegant laptop", "Almost new keyboard", "Exceptional router", "High quality keyboard", "Exceptional router", "Elegant router", "Cheap keyboard", "High quality monitor", "High quality keyboard", "Funny keyboard", "Cheap mouse", "Cheap monitor",
              "Funny headphones", "Elegant mouse", "Cheap smartphone", "High quality mouse", "Funny keyboard", "Second hand monitor", "Almost new router", "Almost new mouse", "Elegant smartphone", "Second hand router", "Second hand mouse", "Second hand tablet", "Exceptional tablet", "High quality smartphone", "Brand new headphones", "Exceptional monitor", "Elegant mouse", "Cheap laptop", "High quality smartphone", "Cheap monitor", "Funny monitor", "Almost new mouse", "Elegant headphones", "Cheap mouse", "Exceptional smartphone", "Cheap monitor", "Exceptional tablet", "Almost new tablet", "Second hand headphones", "Cheap tablet", "Elegant mouse", "Second hand mouse", "Cheap laptop", "Cheap keyboard", "Elegant router", "Elegant headphones", "Second hand monitor", "Funny router", "Elegant mouse", "Elegant headphones", "Brand new mouse", "Exceptional tablet", "Funny router", "Second hand headphones", "Brand new laptop", "Second hand router", "Cheap mouse", "Funny keyboard", "Elegant headphones", "Brand new laptop", "Elegant laptop", "Second hand mouse"]
warehouse2 = ["High quality tablet", "Second hand headphones", "Second hand laptop", "Exceptional tablet", "Exceptional headphones", "Brand new smartphone", "Elegant laptop", "High quality tablet", "Brand new headphones", "Exceptional mouse", "Cheap mouse", "Cheap headphones", "High quality headphones", "Brand new keyboard", "Brand new smartphone", "Almost new mouse", "Second hand router", "High quality monitor", "High quality smartphone", "Second hand headphones", "Elegant monitor", "High quality mouse", "Almost new keyboard", "Exceptional headphones", "High quality smartphone", "Exceptional smartphone", "High quality tablet", "Cheap mouse", "Cheap monitor", "Funny monitor", "Elegant monitor", "Funny smartphone", "Second hand mouse", "Almost new headphones", "Cheap headphones", "High quality router", "Exceptional keyboard", "Funny keyboard", "Exceptional laptop", "Cheap keyboard", "Second hand mouse", "Elegant router", "Cheap router", "Funny mouse", "Funny laptop", "Elegant tablet", "Exceptional mouse", "Funny headphones", "Elegant tablet",
              "Second hand laptop", "Brand new headphones", "Second hand headphones", "Cheap router", "Exceptional mouse", "Elegant router", "Exceptional monitor", "Exceptional keyboard", "Funny headphones", "Second hand headphones", "Almost new router", "Brand new tablet", "Funny mouse", "Elegant mouse", "High quality router", "Second hand keyboard", "Second hand router", "Brand new monitor", "Funny mouse", "Funny tablet", "Elegant keyboard", "Cheap router", "Funny router", "Second hand monitor", "Elegant smartphone", "Brand new monitor", "Second hand monitor", "Second hand keyboard", "Cheap mouse", "Brand new keyboard", "Exceptional mouse", "Elegant router", "Brand new mouse", "Exceptional keyboard", "Elegant smartphone", "Exceptional tablet", "Second hand keyboard", "Almost new headphones", "Brand new tablet", "Brand new tablet", "Exceptional headphones", "Funny smartphone", "Funny smartphone", "Second hand tablet", "Cheap router", "Almost new keyboard", "Elegant router", "Brand new tablet", "High quality tablet", "Almost new router", "High quality monitor"]

username = input("Please enter your username: ")


print()

print("Hi", username, ".", "Please select one of the following operations: ")


print("Type 1 for LIST ITEMS BY WAREHOUSE","Type 2 for SEARCH AN ITEM AND PLACE AN ORDER", "Type 3 to terminate the program",sep='\n')
operation= input("Type desired operation")

if operation=="1":
    print()
    print("Warehouse1")
    print()
    print (*warehouse1, sep='\n')
    print()
    print("Warehouse2")
    print()
    print (*warehouse2, sep='\n')
elif operation=="2":
    item_name=input("Please input an item name: ")
    print("In warehouse 1:")
    print("item count=",warehouse1.count(item_name))
    print("In warehouse 2: ")
    print("item count=",warehouse2.count(item_name))
    if (warehouse1.count(item_name)+warehouse2.count(item_name))==0:
        print("Item not found")
        breakpoint
    else:
        print("ok you selected",item_name)
    order_decision=input("Do you want to order the item? YES or NO? ")
    
    if order_decision=="YES":
        order_amount=int(input("How many items do you want to order? "))
        if order_amount <=(warehouse1.count(item_name)+warehouse2.count(item_name)):
            print(order_amount,item_name,"ordered")
        elif order_amount >(warehouse1.count(item_name)+warehouse2.count(item_name)):    
            supplemental_order=input("Not enough items in warehouse.Do you want to order the maximum availability instead? YES or NO: ")
            if supplemental_order=="YES":
                print(warehouse1.count(item_name)+warehouse2.count(item_name),item_name,"ordered")
            else:
                print("Program terminated")
    elif order_decision=="NO":
        breakpoint
elif operation=="3":
    print("You exited the program")
else:
    print("the operator is not valid. Restart the program please")       

print()
print("Thank you for your visit",username)

