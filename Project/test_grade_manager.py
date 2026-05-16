import unittest
from grade_manager import GradeManager

class TestGradeManager(unittest.TestCase):
    def setUp(self):
        self.manager = GradeManager()
        self.manager.add_student("Ali")

    def test_add_student_new(self):
        result = self.manager.add_student("Sara")
        self.assertEqual(result, "Sara added.")

    def test_add_student_duplicate(self):
        result = self.manager.add_student("Ali")
        self.assertEqual(result, "Ali already exists.")

    def test_add_grade_valid(self):
        result = self.manager.add_grade("Ali", 85)
        self.assertEqual(result, "Grade 85 added for Ali.")
        self.assertIn(85, self.manager.grades["Ali"])

    def test_add_grade_invalid_range(self):
        result = self.manager.add_grade("Ali", 105)
        self.assertEqual(result, "Invalid grade. Must be 0-100.")

    def test_average_calculation(self):
        self.manager.add_grade("Ali", 80)
        self.manager.add_grade("Ali", 90)
        avg = self.manager.calculate_average("Ali")
        self.assertEqual(avg, 85.0)

    def test_pass_fail_pass(self):
        self.manager.add_grade("Ali", 75)
        status = self.manager.pass_fail("Ali")
        self.assertEqual(status, "Pass")

if __name__ == "__main__":
    unittest.main()