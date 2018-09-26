class Student:
    def __init__(self, first_name, middle_name, last_name, address, contact_no,roll_no):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.contact_no = contact_no
        self.roll_no=roll_no

    def getFirstName(self):
        return self.first_name

    def getMiddleName(self):
        return self.middle_name

    def getLastName(self):
        return self.last_name

    def getAddress(self):
        return self.address

    def getContactNo(self):
        return self.contact_no

    def setFirstName(self, first_name):
        self.first_name = first_name

    def setMiddleName(self, middle_name):
        self.middle_name = middle_name

    def setLastName(self, last_name):
        self.last_name = last_name
    def setAddress(self,address):
        self.address=address

    def setContactNo(self, contact_no):
        self.contact_no = contact_no

    def getRollNo(self):
        return self.roll_no;

    def setRollNo(self, roll_no):
        self.roll_no = roll_no
