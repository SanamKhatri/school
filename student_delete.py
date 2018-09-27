import Student
import student_database


def delete_student():
    delete_menu="""
            1.By Roll
            2.By Name
            3.By Address
            4.By Contact No"""
    print(delete_menu)
    delete_choice=int(input("Enter choice"))
    if delete_choice==1:
        delete_roll=input("Enter the roll no to delete")
        d=Student(roll_no=delete_roll,name=None,address=None,contact_no=None)
        student_database.delete_by_roll_no(d)
    elif delete_choice==2:
        delete_name=input("Enter the to name delete")
        d = Student(roll_no=None, name=delete_name, address=None, contact_no=None)
        student_database.delete_by_name(d)
    elif delete_choice==3:
        delete_address=input("Enter the address to delete")
        d = Student(roll_no=None, name=None, address=delete_address, contact_no=None)
        student_database.delete_by_address(d)
    elif delete_choice==4:
        delete_contact=input("Enter the contact no to delete")
        d = Student(roll_no=None, name=None, address=None, contact_no=delete_contact)
        student_database.delete_by_contact_no(d)
    else:
        print("Invalid choice")