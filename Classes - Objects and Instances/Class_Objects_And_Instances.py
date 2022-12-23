class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay, mail):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = mail
        self.email = first + "." + last + mail

    def fullname(self):
        return print("{} {}".format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Drishtant", "Behera", 50000, "@gmail.com")
emp_2 = Employee("Alex", "Tumbler", 60000, "@yahoo.com")


def emp_1_detail():
    print(emp_1.fullname)
    print(emp_1.pay)
    print(emp_1.email)


def emp_2_detail():
    print(emp_2.fullname)
    print(emp_2.pay)
    print(emp_2.email)

