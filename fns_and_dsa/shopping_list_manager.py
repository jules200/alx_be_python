

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        option = input("Your choice: ")
        if option == "1":
            item = input("Enter new item: ")
            shopping_list.append(item)
            pass
        elif option == "2":
            item = input("Enter item to remove: ")
            shopping_list.remove(item)
            pass
        elif option == "3":        
            print(f"This is your shopping list: \n {shopping_list}")
            pass
        elif option == "4":
            break
        else:
            print("Enter the valid Option")
main()
