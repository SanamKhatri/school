import sys

import pymysql
from Student import Student

def connection():
    dbconnection = pymysql.connect("localhost", "root", "", "school")
    return dbconnection


def add_student(student_object):
    is_added = False
    db = connection()
    sql = "insert into student(first_name,middle_name,last_name,address,contact_no) values ('{}','{}','{}','{}','{}')".format(
        student_object.getFirstName(), student_object.getMiddleName(), student_object.getLastName(),
        student_object.getAddress(), student_object.getContactNo())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_added = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_added


def show_student(student_object):
    is_shown = False
    db = connection()
    sql = "select * from student"
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for r in result:
        print("Roll No={}".format(r[0]))
        print("First Name={}".format(r[1]))
        print("Middle Name={}".format(r[2]))
        print("Last Name={}".format(r[3]))
        print("Address={}".format(r[4]))
        print("Contact No={}".format(r[5]))
    try:
        cursor.execute(sql)
        db.commit()
        is_shown = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_shown


def search_student_by_roll_no(roll_no):
    db = connection()
    sql = "select * from student where roll_no='{}'".format(roll_no)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        s = Student(roll_no=result[0],first_name=result[1], middle_name=result[2], last_name=result[3], address=result[4],
                    contact_no=result[5])
        s.setRollNo(result[0])
    return result
    return s
