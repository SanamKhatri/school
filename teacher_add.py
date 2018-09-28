import teacher_database
from Teacher import Teacher


def add_teacher():
    name = input("Enter the name of the teacher")
    address = input("Enter the address of the teacher")
    contact_no = int(input("Enter the contact no of the teacher"))
    salary = int(input("Enter the salary of the teacher"))
    subject = input("Enter the subject the teacher")
    sex=input("Enter the sex of the teacher")
    t = Teacher(name=name, address=address, contact_no=contact_no, salary=salary, subject=subject,sex=sex)
    is_inserted = teacher_database.add_teacher(t)
    if is_inserted:
        print("The data have been inserted")
    else:
        print("The data have not been inserted")
