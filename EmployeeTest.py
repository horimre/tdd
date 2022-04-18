import unittest
from Employee import Employee


class TestCalcTotalSalary(unittest.TestCase):

    '''
    # runs once before all tests
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    # runs once after all tests
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    # coverage:
    # pip install coverage
    # coverage run EmployeeTest.py
    # coverage html
    '''

    # runs before each test
    def setUp(self):
        self.employee = Employee(2000.0)

    # runs after each test
    def tearDown(self):
        pass

    def test_function_returns_float(self):
        self.assertIsInstance(self.employee.calc_total_salary(), float)

    def test_no_commission(self):
        self.assertEqual(self.employee.calc_total_salary(), 2000.0)

    def test_10_percent_commission(self):
        self.employee.commission = 10.0
        self.assertEqual(self.employee.calc_total_salary(), 2200.0)

    def test_100_percent_commission(self):
        self.employee.commission = 100.0
        self.assertEqual(self.employee.calc_total_salary(), 4000.0)


if __name__ == '__main__':
    unittest.main()
