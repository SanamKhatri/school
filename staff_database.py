import sys

from Staff import Staff
from student_database import connection


def add_staff(staff_object):
    is_added = False
    db = connection()
    sql = "insert into staff(name,address,contact_no,salary,post,sex) values ('{}','{}','{}','{}','{}','{}')".format(
        staff_object.getName(), staff_object.getAddress(), staff_object.getContactNo(),
        staff_object.getSalary(), staff_object.getPost(), staff_object.getSex())
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


def staff_search_by_name(name):
    db = connection()
    sql = "select * from staff where name='{}'".format(name)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        s = Staff(name=result[1], address=result[2],
                  contact_no=result[3], salary=result[4], post=result[5], sex=result[6])
        s.setSN(result[0])
    return result
    return s


def staff_search_by_contact_no(contact_no):
    db = connection()
    sql = "select * from staff where contact_no='{}'".format(contact_no)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        s = Staff(name=result[1], address=result[2],
                  contact_no=result[3], salary=result[4], post=result[5], sex=result[6])
        s.setSN(result[0])
    return result
    return s


def staff_search_by_address(address):
    db = connection()
    sql = "select * from staff where address='{}'".format(address)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        s = Staff(name=result[1], address=result[2],
                  contact_no=result[3], salary=result[4], post=result[5], sex=result[6])
        s.setSN(result[0])
    return result
    return s


def staff_search_by_subject(subject):
    db = connection()
    sql = "select * from staff where subject='{}'".format(subject)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        s = Staff(name=result[1], address=result[2],
                  contact_no=result[3], salary=result[4], post=result[5], sex=result[6])
        s.setSN(result[0])
    return result
    return s


def delete_by_name(staff_object):
    is_deleted = False
    db = connection()
    sql = "delete from staff where name='{}'".format(staff_object.getName())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_deleted = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_deleted


def delete_by_address(staff_object):
    is_deleted = False
    db = connection()
    sql = "delete from staff where address='{}'".format(staff_object.getAddress())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_deleted = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_deleted


def delete_by_post(staff_object):
    is_deleted = False
    db = connection()
    sql = "delete from staff where post='{}'".format(staff_object.getPost())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_deleted = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_deleted


def show_staff(staff_object):
    is_shown = False
    db = connection()
    sql = "select * from staff"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_shown = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_shown


def update_name(staff_object):
    is_updated = False
    db = connection()
    sql = "update staff set name='{}' where s.n='{}'".format(staff_object.getName(), staff_object.getSN())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_updated


def update_address(staff_object):
    is_updated = False
    db = connection()
    sql = "update staff set address='{}' where s.n='{}'".format(staff_object.getAddress(), staff_object.getSN())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_updated


def update_post(staff_object):
    is_updated = False
    db = connection()
    sql = "update staff set post='{}' where s.n='{}'".format(staff_object.getPost(), staff_object.getSN())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_updated


def update_contact_no(staff_object):
    is_updated = False
    db = connection()
    sql = "update staff set contact_no='{}' where s.n='{}'".format(staff_object.getContactNo(),
                                                                   staff_object.getSN())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_updated


def update_salary(staff_object):
    is_updated = False
    db = connection()
    sql = "update staff set salary='{}' where s.n='{}'".format(staff_object.getName(), staff_object.getSN())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        is_updated = True
    except:
        print(sys.exc_info())
    finally:
        db.close()
    return is_updated


def getStaffDetails(sn):
    db = connection()
    sql = "select * from staff where s.n='{}'".format(sn)
    cursor = db.cursor()
    cursor.execute(sql)
    original_staff = cursor.fetchone()
    if (original_staff):
        s = Staff(name=original_staff[1], address=original_staff[2], contact_no=original_staff[3],
                    salary=original_staff[4], postt=original_staff[5], sex=original_staff[6])
        s.setSn(original_staff[0])
    return original_staff
    return s
