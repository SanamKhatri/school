import student_database
from Student import Student
from student_main import student_menu
from teacher_main import teacher_menu
from staff_main import staff_menu


def main():
    menu = """
            1.Student
            2.Teacher
            3.Staff"""
    print(menu)
    choice = int(input("Enter the choice:"))
    if choice == 1:
        student_menu()
    elif choice == 2:
        teacher_menu()
    elif choice == 3:
        staff_menu()


if __name__ == '__main__':
    main()
