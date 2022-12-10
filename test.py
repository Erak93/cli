list=["old laptop","phone", "laptop red"]
#subs=input("What do you want?")
#res = [i for i in list if subs in i]
#print (res)



############

def count_category(keyword,destination_list):
    for dictionary in archive.new_data.stock:
        if keyword==dictionary["category"]:
            destination_list.append(dictionary["category"])
    return f'{keyword} added'        

import archive.new_data as new_data
temp_category=[]
temp_items=[]
keyboard_list=[]
smartphone_list=[]
mouse_list=[]
laptop_list=[]
headphones_list=[]
monitor_list=[]
router_list=[]
tablet_list=[]
complete_item_count_list=[]
indexed_category_list=[]

count_category("Keyboard",keyboard_list)
count_category("Smartphone",smartphone_list)
count_category("Mouse",mouse_list)
count_category("Laptop",laptop_list)
count_category("Headphones",headphones_list)
count_category("Monitor",monitor_list)
count_category("Router",router_list)
count_category("Tablet",tablet_list)

print()


Keyboard_count=f'({len(keyboard_list)})'
#print(Keyboard_count)
Smartphone_count=f'({len(smartphone_list)})'
#print(Smartphone_count)
Mouse_count=f'({len(mouse_list)}) '
#print(Mouse_count)
Laptop_count=f'({len(laptop_list)}) '
#print(Laptop_count)
Headphones_count=f'({len(headphones_list)}) '
#print(Headphones_count)
Monitor_count=f'({len(monitor_list)}) '
#print(Monitor_count)
Router_count=f'({len(router_list)}) '
#print(Router_count)
Tablet_count=f'({len(tablet_list)}) '
#print(Tablet_count)

complete_item_count_list.append(Keyboard_count)
complete_item_count_list.append(Smartphone_count)
complete_item_count_list.append(Mouse_count)
complete_item_count_list.append(Laptop_count)
complete_item_count_list.append(Headphones_count)
complete_item_count_list.append(Monitor_count)
complete_item_count_list.append(Router_count)
complete_item_count_list.append(Tablet_count)


for dictionary in  new_data.stock:
    if dictionary["category"] not in temp_category:
        temp_category.append (dictionary["category"])
  
    
for i in temp_category:
    index_item=temp_category.index(i)
    indexed_item=f'{index_item}.{"".join(i)}'
    indexed_category_list.append(indexed_item) 
    
#print(*indexed_category_list, sep="\n")


#print(*complete_item_count_list,sep="\n")

for item_a, item_b in zip(indexed_category_list,complete_item_count_list):
    print(item_a, item_b)

print()




category_ask=input("Which category do you want to browse? Use numeric code please ")
if category_ask=="0":
    category_ask="Keyboard"
elif category_ask=="1":
    category_ask="Smartphone"
elif category_ask=="2":
    category_ask="Laptop"
elif category_ask=="3":
    category_ask="Mouse"
elif category_ask=="4":
    category_ask="Headphones"
elif category_ask=="5":
    category_ask="Monitor"
elif category_ask=="6":
    category_ask="Router"
elif category_ask=="7":
    category_ask="Tablet"
else:
    print("Invalid code. Please start over")
print()
print("List of selected item available")
print()

for dictionary in new_data.stock:
    
    if category_ask in temp_category:

        if category_ask in dictionary["category"]:
      
            item=f'{dictionary["state"]} {dictionary["category"]}, warehouse{dictionary["warehouse"]}'
            if item not in temp_items:
                temp_items.append(item)
print(*temp_items,sep='\n')

print()
print("Thank you for your visit")



