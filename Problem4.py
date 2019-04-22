#Maylene Garcia
#4/16/19
#This program add fruit to an inventory.

def add_fruit(inventory, fruit, quantity=0):
    if 'strawberries' not in new_inventory:
       inventory [fruit] = quantity
    else:
       inventory [fruit] += quantity 
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
if 'strawberries' in new_inventory:
    print("Yes. 'Strawberries' is a key")
print(new_inventory)
add_fruit(new_inventory,'strawberries',25)
print(new_inventory)


