
class Employee:
    def __init__(self, salary: float, commission=0):
        self.salary = salary
        self.commission = commission

    def calc_total_salary(self) -> float:

        total_sal = self.salary

        if self.commission != 0:
            total_sal += (total_sal/100) * self.commission

        return total_sal
