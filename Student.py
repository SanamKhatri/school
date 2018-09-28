class Student:
    def __init__(self, name, address, contact_no):
        self.name = name
        self.address = address
        self.contact_no = contact_no

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getContactNo(self):
        return self.contact_no

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setContactNo(self, contact_no):
        self.contact_no = contact_no

    def getRollNo(self):
        return self.roll_no;

    def setRollNo(self, roll_no):
        self.roll_no = roll_no
