import Student
import student_database


def delete_student():
    delete_menu = """
            1.By Name
            2.By Address
            3.By Contact No"""
    print(delete_menu)
    delete_choice = int(input("Enter choice"))
    if delete_choice == 1:
        delete_name = input("Enter the to name delete")
        d = Student(name=delete_name)
        is_deleted = student_database.delete_by_name(d)
        if is_deleted:
            print("The data is deleted")
        else:
            print("The data is not deleted")
    elif delete_choice == 2:
        delete_address = input("Enter the address to delete")
        d = Student(name=None, address=delete_address, contact_no=None)
        is_deleted = student_database.delete_by_address(d)
        if is_deleted:
            print("The data is deleted")
        else:
            print("The data is not deleted")
    elif delete_choice == 3:
        delete_contact = input("Enter the contact no to delete")
        d = Student(name=None, address=None, contact_no=delete_contact)
        is_deleted = student_database.delete_by_contact_no(d)
        if is_deleted:
            print("The data is deleted")
        else:
            print("The data is not deleted")
    else:
        print("Invalid choice")
