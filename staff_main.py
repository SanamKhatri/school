from staff_add import add_staff
from staff_delete import delete_staff
from staff_search import search_staff
from staff_show import show_staff
from staff_update import update_staff


def staff_menu():
    staff_menu = """
            1.Add Staff
            2.Update Staff
            3.Search Staff
            4.Delete Staff
            5.Show Staff"""
    print(staff_menu)
    staff_choice = int(input("Enter the choice:"))
    if staff_choice == 1:
        add_staff()
    elif staff_choice == 2:
        update_staff()
    elif staff_choice == 3:
        search_staff()
    elif staff_choice == 4:
        delete_staff()
    elif staff_choice == 5:
        show_staff()
    else:
        print("Invalid choice")
