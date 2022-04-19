
class Employee:
    def __init__(self, salary: float, sales=0.0, commission=0.0):
        self.salary = salary
        self.sales = sales
        self.commission = commission

    def calc_total_salary(self) -> float:

        total_sal = self.salary

        if self.commission != 0.0:
            total_sal += (self.sales/100.0) * self.commission

        return total_sal
