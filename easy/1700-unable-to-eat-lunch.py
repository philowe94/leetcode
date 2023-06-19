from typing import List
import pdb

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = len(students)
        while students and sandwiches:
            if (students == sandwiches):
                return 0
            
            if (students[0] == sandwiches[0]):
                students = students[1:]
                sandwiches = sandwiches[1:]
                count = len(students)
            else:
                student = students[0]
                students = students[1:]
                students.append(student)
                count -= 1
            
            if (count == 0):
                return len(students)

        if students:
            return len(students)
        else:
            return 0