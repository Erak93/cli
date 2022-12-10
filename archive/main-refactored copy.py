from archive.data import warehouse1
from archive.data import warehouse2
from archive.new_data import stock
import archive.refactory_support as refactory_support


username = input("Please enter your username: ")


print()

print("Hi", username,",", "please select one of the following operations: ")


print("Type 1 for LIST ITEMS BY WAREHOUSE","Type 2 for SEARCH AN ITEM AND PLACE AN ORDER", "Type 4 to TERMINATE THE PROGRAM",sep='\n')
operation= input("Type desired operation: ")

if operation=="1":
    refactory_support.option_1()
    
elif operation=="2":
    refactory_support.option_2()       
        
elif operation=="4":
    print("You exited the program")
else:
    print("the operator is not valid. Restart the program please")       

print()
print("Thank you for your visit",username)

