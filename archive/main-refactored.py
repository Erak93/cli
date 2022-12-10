from archive.data import warehouse1
from archive.data import warehouse2
from archive.new_data import stock


username = input("Please enter your username: ")


print()

print("Hi", username,",", "please select one of the following operations: ")


print("Type 1 for LIST ITEMS BY WAREHOUSE","Type 2 for SEARCH AN ITEM AND PLACE AN ORDER", "Type 3 to TERMINATE THE PROGRAM",sep='\n')
operation= input("Type desired operation: ")

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
    subs=input("What are you looking for?")
    res = [i for i in warehouse1 if subs in i]
    res2=[i for i in warehouse2 if subs in i]
    if res or res2:
        print ("Here is your search match",*res , sep="\n")
        print (*res2, sep="\n")
       
        item_name=str.capitalize(input("Please pick an item: "))
        print("In warehouse 1:")       
        print("item count=",warehouse1.count(item_name))
        print("In warehouse 2: ")
        print("item count=",warehouse2.count(item_name))
        if (warehouse1.count(item_name)+warehouse2.count(item_name))>=1:
            print("Okay, you selected: ",item_name)
            
            order_decision=input("Do you want to order the item? YES or NO? ")
        
            if order_decision=="YES":
                order_amount=int(input("How many items do you want to order? "))
                if order_amount <=(warehouse1.count(item_name)+warehouse2.count(item_name)):
                    print(order_amount,item_name,"ordered")
                elif order_amount >(warehouse1.count(item_name)+warehouse2.count(item_name)):    
                    supplemental_order=input("Not enough items in warehouse. Do you want to order the maximum availability instead? YES or NO: ")
                    if supplemental_order=="YES":
                                print(warehouse1.count(item_name)+warehouse2.count(item_name),item_name,"ordered.")
                else:
                    print("Program terminated")
            elif order_decision=="NO":
                breakpoint
            else:
                print("Items not found.")
    else:
        print("Items not found")        
        
elif operation=="3":
    print("You exited the program")
else:
    print("the operator is not valid. Restart the program please")       

print()
print("Thank you for your visit",username)

