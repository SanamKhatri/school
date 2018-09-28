import teacher_database
from Teacher import Teacher


def delete_teacher():
    delete_menu="""
        1.By Name
        2.By Addeess
        3.By Subject
        """
    print(delete_menu)
    delete_choice=int(input("Enter the delete choice"))
    if delete_choice==1:
        delete_name=input("Enter the name of the teacher to delete")
        t=Teacher(name=delete_name)
        is_deleted=teacher_database.delete_by_name(t)
        if is_deleted:
            print("The data is deleted")
        else:
            print("There was error in the process")
    elif delete_choice==2:
        delete_address = input("Enter the address of the teacher to delete")
        t = Teacher(address=delete_address)
        is_deleted = teacher_database.delete_by_address(t)
        if is_deleted:
            print("The data is deleted")
        else:
            print("There was error in the process")
    elif delete_choice==3:
        delete_subject = input("Enter the subject of the teacher to delete")
        t = Teacher(subject=delete_subject)
        is_deleted = teacher_database.delete_by_subject(t)
        if is_deleted:
            print("The data is deleted")
        else:
            print("There was error in the process")