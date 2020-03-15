from bisect import insort_right
from collections import defaultdict


class School:
    def __init__(self):
        self.grades_by_student = {}
        self.students_by_grade = defaultdict(list)

    def add_student(self, name, grade):
        self.grades_by_student[name] = grade
        insort_right(self.students_by_grade[grade], name)

    def roster(self):
        key = lambda s: (self.grades_by_student[s], s)
        return sorted(self.grades_by_student.keys(), key=key)

    def grade(self, grade_number):
        return self.students_by_grade[grade_number]