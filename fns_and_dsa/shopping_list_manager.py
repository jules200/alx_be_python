shopping_list = []
print(shopping_list)
def shopping(option):
    if option == "1":
        item = input("Enter new item: ")
        shopping_list.append(item)
        return theoptions()
    elif option == "2":
        item = input("Enter item to remove: ")
        shopping_list.remove(item)
        return theoptions()
    elif option == "3":        
        print(f"This is your shopping list: \n {shopping_list}")
        return theoptions()
    elif option == "4":
        return none
    else:
        print("Enter the valid Option")
        return theoptions()

def display_menu():
    print("Choose the option")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    option = int(input("Your choice: "))
    return shopping(option)

display_menu()

