from employee_factory import EmployeeFactory

emp1 = EmployeeFactory.create_employee("manager")
emp1.position()

emp2 = EmployeeFactory.create_employee("developer")
emp2.position()