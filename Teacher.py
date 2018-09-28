class Teacher:
    def __init__(self, name, address, contact_no, salary, subject,sex):
        self.name = name
        self.address = address
        self.contact_no = contact_no
        self.salary = salary
        self.subject = subject
        self.sex=sex


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

    def getSex(self,sex):
        return self.sex

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setContactNo(self, contact_no):
        self.contact_no = contact_no

    def setSalary(self, salary):
        self.salary = salary

    def setSubject(self, subject):
        self.subject = subject

    def setSex(self,sex):
        self.sex=sex
    def getSN(self):
        return self.sn

    def setSN(self, sn):
        self.sn = sn
