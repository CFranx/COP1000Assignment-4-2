import unittest
import main

class TestMain(unittest.TestCase):
  def test_input1(self):
    result = main.employeeProductivity()
    self.assertEqual(result, ("Employee Name: Dave Matthews", "Employee Bonus: $200.0"))

  def test_input2(self):
    result = main.employeeProductivity()
    self.assertEqual(result, ("Employee Name: James Patterson", "Employee Bonus: $100.0"))

  def test_input3(self):
    result = main.employeeProductivity()
    self.assertEqual(result, ("Employee Name: Jenna Jenkins", "Employee Bonus: $75.0"))

if __name__ == "__main__":
  unittest.main()