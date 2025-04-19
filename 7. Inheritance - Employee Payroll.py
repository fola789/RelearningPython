class Employee:
    def __init__(self, name: str, employee_id: int, monthly_salary: float) -> None:
        self.name = name
        self.employee_id = employee_id
        self.monthly_salary = monthly_salary

    def calculate_pay(self) -> float:
        annual_salary = self.monthly_salary * 12
        return annual_salary

    def find_annual_salary(self, annual_salary: float) -> str:
        return f'Your annual salary is £) {annual_salary:.2f}'


class PartTimeEmployee(Employee):
    def __init__(self, name: str, employee_id: int, monthly_salary: float, num_months_worked: int) -> None:
        super().__init__(name, employee_id, monthly_salary)
        self.num_months_worked = num_months_worked

    def calculate_pay(self) -> float:
        annual_salary = self.monthly_salary * self.num_months_worked
        return annual_salary

    def find_annual_salary(self) -> str:
        return f'Your annual salary for your part time job of {self.num_months_worked} months is £ {self.calculate_pay():.2f}'


class FullTimeEmployee(Employee):
    def __init__(self, name: str, employee_id: int, monthly_salary: float) -> None:
        super().__init__(name, employee_id, monthly_salary)

    def calculate_pay(self) -> float:
        annual_salary = self.monthly_salary * 12
        return annual_salary

    def find_annual_salary(self) -> str:
        return f'Your annual salary for your full time job is £{self.calculate_pay():.2f}'


partTimeEmployee1 = PartTimeEmployee("Matt", 123213, 24000, 6)
partTimeEmployee2 = PartTimeEmployee("John", 56756, 11000.50, 7)
fullTimeEmployee1 = FullTimeEmployee("Fola", 8923498, 40000)
fullTimeEmployee2 = FullTimeEmployee("James", 777777, 60000.00)

partTimeEmployee1.calculate_pay()
partTimeEmployee2.calculate_pay()
print(partTimeEmployee1.find_annual_salary())
print(partTimeEmployee2.find_annual_salary())
fullTimeEmployee1.calculate_pay()
fullTimeEmployee2.calculate_pay()
print(fullTimeEmployee1.find_annual_salary())
print(fullTimeEmployee2.find_annual_salary())
