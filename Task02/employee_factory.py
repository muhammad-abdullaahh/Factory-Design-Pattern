from manager import Manager
from developer import Developer
from intern import Intern

class EmployeeFactory:

    @staticmethod
    def create_employee(emp_type):

        if emp_type == "manager":
            return Manager()

        elif emp_type == "developer":
            return Developer()

        elif emp_type == "intern":
            return Intern()