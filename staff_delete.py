import staff_database
from Staff import Staff


def delete_staff():
    delete_menu="""
        1.By Name
        2.By Addeess
        3.By Post
        """
    print(delete_menu)
    delete_choice=int(input("Enter the delete choice"))
    if delete_choice==1:
        delete_name=input("Enter the name of the staff to elete")
        s=Staff(name=delete_name)
        is_deleted=staff_database.delete_by_name(s)
        if is_deleted:
            print("The data is deleted")
        else:
            print("There was error in the process")
    elif delete_choice==2:
        delete_address = input("Enter the address of the staff to delete")
        s = Staff(address=delete_address)
        is_deleted = staff_database.delete_by_address(s)
        if is_deleted:
            print("The data is deleted")
        else:
            print("There was error in the process")
    elif delete_choice==3:
        delete_post = input("Enter the subject of the staff to delete")
        s = Staff(post=delete_post)
        is_deleted = staff_database.delete_by_subject(s)
        if is_deleted:
            print("The data is deleted")
        else:
            print("There was error in the process")