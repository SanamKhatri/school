import student_database
from Student import Student
from student_main import student_menu


def main():
    menu = """
            1.Student
            2.Teacher
            3.Staff"""
    print(menu)
    choice = int(input("Enter the choice:"))
    if choice == 1:
        student_menu()


if __name__ == '__main__':
    main()
