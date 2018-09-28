import staff_database
from Staff import Staff


def update_staff():
    sn = int(input("Enter the roll no:"))
    is_inserted = staff_database.getStaffDetails(sn)
    if is_inserted:
        staff_detail = staff_database.getStaffDetails(sn)
        print(staff_detail)
        print("The detail are")
        print("Name= " + staff_detail[1])
        print("Address= " + staff_detail[2])
        print("Contact no= " + staff_detail[3])
        print("Salary= " + staff_detail[4])
        print("Subject= " + staff_detail[5])
        print("Sex= " + staff_detail[6])
    update_menu = """
        1.Name
        2.Address
        3.Contact
        4.Salary
        5.Post"""
    print(update_menu)
    update_choice = int(input("Enter the update choice"))
    if update_choice == 1:
        update_name = input("Enter the name of the staff to update:")
        staff_object = Staff(name=update_name, address=None, contact_no=None, salary=None, post=None, sex=None)
        staff_object.setSN(staff_detail[0])
        is_updated = staff_database.update_name(staff_object)
        if is_updated:
            print("The data is updated")
        else:
            print("The data is not updated")
    elif update_choice == 2:
        update_address = input("Enter the address of the staff to update:")
        staff_object = Staff(name=None, address=update_address, contact_no=None, salary=None, post=None,
                                 sex=None)
        staff_object.setSN(staff_detail[0])
        is_updated = staff_database.update_address(staff_object)
        if is_updated:
            print("The data is updated")
        else:
            print("The data is not updated")
    elif update_choice == 3:
        update_contact = input("Enter the contact of the staff to update:")
        staff_object = Staff(name=None, address=None, contact_no=update_contact, salary=None, post=None,
                                 sex=None)
        staff_object.setSN(staff_detail[0])
        is_updated = staff_database.update_contact_no(staff_object)
        if is_updated:
            print("The data is updated")
        else:
            print("The data is not updated")
    elif update_choice == 4:
        update_salary = input("Enter the address of the staff to update:")
        staff_object = Staff(name=None, address=None, contact_no=None, salary=update_salary, post=None,
                                 sex=None)
        staff_object.setSN(staff_detail[0])
        is_updated = staff_database.update_salary(staff_object)
        if is_updated:
            print("The data is updated")
        else:
            print("The data is not updated")
    elif update_choice == 5:
        update_post = input("Enter the post of the staff to update:")
        staff_object = Staff(name=None, address=None, contact_no=None, salary=None, post=update_post,
                                 sex=None)
        staff_object.setSN(staff_detail[0])
        is_updated = staff_database.update_post(staff_object)
        if is_updated:
            print("The data is updated")
        else:
            print("The data is not updated")
    else:
        print("Invalid Choice")
