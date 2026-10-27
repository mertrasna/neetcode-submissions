class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # we know the length of students and sandwiches arrays equal 
        fails = 0
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                fails = 0 # someone ate -> not stuck
            else: 
                value = students.pop(0)
                students.append(value)
                fails += 1
            if fails == len(students):
                break
        return len(students)
