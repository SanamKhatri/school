import teacher_database
from Teacher import Teacher


def update_teacher():
    sn = int(input("Enter the roll no:"))
    is_inserted = teacher_database.getTeacherDetails(sn)
    if is_inserted:
        teacher_deatail = teacher_database.getStudentDetails(sn)
        print(teacher_deatail)
        print("The detail are")
        print("Name= " + teacher_deatail[1])
        print("Address= " + teacher_deatail[2])
        print("Contact no= " + teacher_deatail[3])
        print("Salary= " + teacher_deatail[4])
        print("Subject= " + teacher_deatail[5])
        print("Sex= " + teacher_deatail[6])
    update_menu = """
        1.Name
        2.Address
        3.Contact
        4.Salary
        5.Subject"""
    print(update_menu)
    update_choice = int(input("Enter the update choice"))
    if update_choice == 1:
        update_name = input("Enter the name of the teacher to update:")
        teacher_object = Teacher(name=update_name, address=None, contact_no=None, salary=None, subject=None, sex=None)
        teacher_object.set(teacher_deatail[0])
        is_updated = teacher_database.update_name(teacher_object)
        if is_updated:
            print("The data is updated")
        else:
            print("The data is not updated")
    elif update_choice == 2:
        update_address = input("Enter the address of the teacher to update:")
        teacher_object = Teacher(name=None, address=update_address, contact_no=None, salary=None, subject=None,
                                 sex=None)
        teacher_object.set(teacher_deatail[0])
        is_updated = teacher_database.update_address(teacher_object)
        if is_updated:
            print("The data is updated")
        else:
            print("The data is not updated")
    elif update_choice == 3:
        update_contact = input("Enter the contact of the teacher to update:")
        teacher_object = Teacher(name=None, address=None, contact_no=update_contact, salary=None, subject=None,
                                 sex=None)
        teacher_object.setSN(teacher_deatail[0])
        is_updated = teacher_database.update_contact_no(teacher_object)
        if is_updated:
            print("The data is updated")
        else:
            print("The data is not updated")
    elif update_choice == 4:
        update_salary = input("Enter the address of the teacher to update:")
        teacher_object = Teacher(name=None, address=None, contact_no=None, salary=update_salary, subject=None,
                                 sex=None)
        teacher_object.setSN(teacher_deatail[0])
        is_updated = teacher_database.update_salary(teacher_object)
        if is_updated:
            print("The data is updated")
        else:
            print("The data is not updated")
    elif update_choice == 5:
        update_subject = input("Enter the subject of the teacher to update:")
        teacher_object = Teacher(name=None, address=None, contact_no=None, salary=None, subject=update_subject,
                                 sex=None)
        teacher_object.setSN(teacher_deatail[0])
        is_updated = teacher_database.update_address(teacher_object)
        if is_updated:
            print("The data is updated")
        else:
            print("The data is not updated")
    else:
        print("Invalid Choice")
