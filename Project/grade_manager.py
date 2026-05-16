class GradeManager:
    def __init__(self):
        self.grades = {}

    def add_student(self, name):
        if name in self.grades:
            return f"{name} already exists."
        else:
            self.grades[name] = []
            return f"{name} added."

    def add_grade(self, name, grade):
        if name not in self.grades:
            return f"{name} not found."
        if grade < 0 or grade > 100:
            return "Invalid grade. Must be 0-100."
        self.grades[name].append(grade)
        return f"Grade {grade} added for {name}."

    def calculate_average(self, name):
        if name not in self.grades:
            return f"{name} not found."
        if not self.grades[name]:
            return f"No grades for {name}."
        avg = sum(self.grades[name]) / len(self.grades[name])
        return round(avg, 2)

    def pass_fail(self, name, passing_score=60):
        avg = self.calculate_average(name)
        if isinstance(avg, str):  # error message returned
            return avg
        return "Pass" if avg >= passing_score else "Fail"

    def display_all(self):
        if not self.grades:
            return "No students found."
        result = ""
        for name in self.grades:
            avg = self.calculate_average(name)
            result += f"{name}: Grades {self.grades[name]}, Avg {avg}\n"
        return result.strip()