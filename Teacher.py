class Teacher:
    def __init__(self, name, address, contact_no, salary, subject):
        self.name = name
        self.address = address
        self.contact_no = contact_no
        self.salary = salary
        self.subject = subject

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getContactNo(self):
        return self.contact_no

    def getSalary(self):
        return self.salary

    def getSubject(self):
        return self.subject

    def setName(self, name):
        self.name = name

    def setMiddleName(self, middle_name):
        self.middle_name = middle_name

    def setLastName(self, last_name):
        self.last_name = last_name

    def setAddress(self, address):
        self.address = address

    def setContactNo(self, contact_no):
        self.contact_no = contact_no

    def setSalary(self, salary):
        self.salary = salary

    def setSubject(self, subject):
        self.subject = subject

    def getSN(self):
        return self.sn

    def setSN(self, sn):
        self.sn = sn
