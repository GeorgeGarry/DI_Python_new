import menu_item
import menu_manager


def show_user_menu():
    user_finished = False
    while not user_finished:
        input_valid = False
        options = ["v", "a", "d", "u", "s"]
        while not input_valid:
            user_choice = input("""
                Please select:
                
                View an Item (V)
                Add an Item (A)
                Delete an Item (D)
                Update an Item (U)
                Show the Menu (S)
            """)
            if user_choice.lower() in options:
                print("Correct choice")
                input_valid = True
            else:
                print("Please choose from V A D U S:")

        switch_dict = {
            'v': view_one_item,
            'a': add_item_to_menu,
            'd': remove_item_from_menu,
            'u': update_item_from_menu,
            's': show_restaurant_menu,
        }
        selected_function = switch_dict[user_choice.lower()]
        selected_function()
        quit_menu = input("Do you want to quit? Y/N\n")
        if quit_menu.lower() == 'y':
            print("Ok! Goodbye!")
            show_restaurant_menu()
            user_finished = True


def add_item_to_menu():
    try:
        user_item_name = input("Please choose a new name:\n")
        user_item_price = input("Please choose a new price:\n")
        user_item = menu_item.MenuItem(user_item_name, user_item_price)
        user_item.save()
        print("Item added successfully")
    except:
        print("Something went wrong")


def remove_item_from_menu():
    try:
        user_item_name = input("What item do you want to delete?\n")
        user_item = menu_item.MenuItem(user_item_name)
        user_item.delete()
        print("Item was deleted")
    except:
        print("Something went wrong")


def update_item_from_menu():
    try:
        user_item_name = input("What item do you want to update?\n")
        user_item = menu_item.MenuItem(user_item_name)
        new_name = input("Please choose a new name for the item: \n")
        new_price = input("Please enter a new price: \n")
        user_item.update(new_name, new_price)
        print("Item was updated")
    except:
        print("Something went wrong")


def show_restaurant_menu():
    try:
        manager_tmp = menu_manager.MenuManager()
        all_items = manager_tmp.all_items()
        print("Here's our menu:")
        for item in all_items:
            print(item)
    except:
        print("Something went wrong")


def view_one_item():
    try:
        item_searched_name = input("Please input the name you're looking for:\n")
        manager_tmp = menu_manager.MenuManager()
        item_search = manager_tmp.get_by_name(item_searched_name)
        print("Here's the item:\n", item_search)

    except:
        print("Something went wrong")


show_user_menu()
