import student_database
from Student import Student


def update_student():
    roll_no = int(input("Enter the roll no:"))
    is_inserted = student_database.getStudentDetails(roll_no)
    if is_inserted:
        student_deatail = student_database.getStudentDetails(roll_no)
        print(student_deatail)
        print("The detail are")
        print("Name= " + student_deatail[1])
        print("Address= " + student_deatail[2])
        #print("Contact No= " + student_deatail[3])
        update_menu = """
                        1.Only Name
                        2.Only Address
                        3.Only Contact No
                        4.Name and Address
                        5.Name and Contact
                        6.Address and Contact
                        7.Name, Address and Contact"""
        print(update_menu)
        update_choice = int(input("Enter the update you want to do"))
        if update_choice == 1:
            update_name = input("Enter the name to update:")
            student_object = Student(name=update_name, address=None, contact_no=None)
            student_object.setRollNo(student_deatail[0])
            is_updated = student_database.update_by_name(student_object)
            if is_updated:
                print("The data is updated")
            else:
                print("The data is not updated")
        elif update_choice == 2:
            update_address = input("Enter the address to update:")
            student_object = Student(name=None, address=update_address, contact_no=None)
            student_object.setRollNo(student_deatail[0])
            is_updated = student_database.update_by_name(student_object)
            if is_updated:
                print("The data is updated")
            else:
                print("The data is not updated")
        elif update_choice == 3:
            update_contact_no = input("Enter the Contact No to update:")
            student_object = Student(name=None, address=None, contact_no=update_contact_no)
            student_object.setRollNo(student_deatail[0])
            is_updated = student_database.update_by_name(student_object)
            if is_updated:
                print("The data is updated")
            else:
                print("The data is not updated")
        elif update_choice == 4:
            update_name = input("Enter the name to update:")
            update_address = input("Enter the address to update:")
            student_object = Student(name=update_name, address=update_address, contact_no=None)
            student_object.setRollNo(student_deatail[0])
            is_updated = student_database.update_by_name(student_object)
            if is_updated:
                print("The data is updated")
            else:
                print("The data is not updated")
        elif update_choice == 5:
            update_name = input("Enter the name to update:")
            update_contact_no = input("Enter the contact no to update:")
            student_object = Student(name=update_name, address=None, contact_no=update_contact_no)
            student_object.setRollNo(student_deatail[0])
            is_updated = student_database.update_by_name(student_object)
            if is_updated:
                print("The data is updated")
            else:
                print("The data is not updated")
        elif update_choice == 6:
            update_address = input("Enter the address to update:")
            update_contact_no = input("Enter the contact no to update:")
            student_object = Student(name=None, address=update_address, contact_no=update_contact_no)
            student_object.setRollNo(student_deatail[0])
            is_updated = student_database.update_by_name(student_object)
            if is_updated:
                print("The data is updated")
            else:
                print("The data is not updated")
        elif update_choice == 7:
            update_name = input("Enter the name to update:")
            update_address = input("Enter the address to update:")
            update_contact_no = input("Entert the contact no to update")
            student_object = Student(name=update_name, address=update_address, contact_no=update_contact_no)
            student_object.setRollNo(student_deatail[0])
            is_updated = student_database.update_by_name(student_object)
            if is_updated:
                print("The data is updated")
            else:
                print("The data is not updated")
    else:
        print("The data is not in database")
