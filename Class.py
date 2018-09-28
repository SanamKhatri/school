class Class():
    def __init__(self, name, subject_1, subject_2, subject_3, subject_4, total, percentage):
        self.name = name
        self.subject_1 = subject_1
        self.subject_2 = subject_2
        self.subject_3 = subject_3
        self.subject_4 = subject_4
        self.total = total
        self.percentage = percentage

    def getRollNo(self):
        return self.roll_no

    def getName(self):
        return self.name

    def getSubject1(self):
        return self.subject_1

    def getSubject2(self):
        return self.subject_2

    def getSubject3(self):
        return self.subject_3

    def getSubject4(self):
        return self.subject_4

    def getTotal(self):
        return self.total

    def getPercentage(self):
        return self.percentage

    def setRollNo(self, roll_no):
        self.roll_no = roll_no

    def setName(self, name):
        self.name = name

    def setSubject1(self, subject_1):
        self.subject_1 = subject_1

    def setSubject2(self, subject_2):
        self.subject_2 = subject_2

    def setSubject3(self, subject_3):
        self.subject_3 = subject_3

    def setSubject4(self, subject_4):
        self.subject_4 = subject_4

    def setTotal(self, total):
        self.total = total

    def setPercentage(self, percentage):
        self.percentage = percentage
