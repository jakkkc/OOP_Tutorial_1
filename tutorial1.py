class Student:
    def __init__(self, first, last, fee_balance):
        self.first = first
        self.last = last
        self.pay = fee_balance
        self.email = first + "." + last + "@school.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

stud_1 = Student("Jackson", "Munene", 500)
stud_2 = Student("John", "Doe", 6000)

print(stud_1.email, stud_2.email)



print(stud_1.fullname())
print(Student.fullname(stud_2))