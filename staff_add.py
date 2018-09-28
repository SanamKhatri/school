import staff_database
from Staff import Staff


def add_teacher():
    name = input("Enter the name of the staff")
    address = input("Enter the address of the staff")
    contact_no = int(input("Enter the contact no of the staff"))
    salary = int(input("Enter the salary of the staff"))
    post = input("Enter the post the staff")
    sex=input("Enter the sex of the staff")
    s = Staff(name=name, address=address, contact_no=contact_no, salary=salary, post=post,sex=sex)
    is_inserted = staff_database.add_staff(s)
    if is_inserted:
        print("The data have been inserted")
    else:
        print("The data have not been inserted")
