class Employee():
    def __init__(self):
        self.emp_id=input("enter empid")
        self.emp_name=input("enter empname")
        self.emp_salary=float(input("enter empsalary"))
        self.emp_department=input("enter department")
    def  calculate_emp_salary(self,hours_worked):
        if hours_worked>50:
            overtime=hours_worked-50
            overtime_amount=(overtime*(self.emp_salary//50))
            self.emp_salary+=overtime_amount
            print(self.emp_salary)
        else:
            print(self.emp_salary)
    def print_employee_details(self):
        print("empid=",self.emp_id)
        print("empname=",self.emp_name)
        print("empsalary=",self.emp_salary)
        print("emp department=",self.emp_department)
obj1=Employee()
obj1.calculate_emp_salary(70)
obj1.print_employee_details()
            
        
        
        
        
        
        
    