from typing import List


class Student:
    __slots__ = ['name', 'score']

    def __init__(self, name: str, score: int):
        self.name: str = name
        self.score: int = score

    def __repr__(self) -> str:
        return "(name = " + self.name + "  score = " + str(self.score) + ")"


if __name__ == '__main__':
    student1: Student = Student("student1", 45)
    student2: Student = Student("student2", 60)
    student3: Student = Student("student3", 56)
    student4: Student = Student("student4", 30)
    student5: Student = Student("student5", 80)
    student6: Student = Student("student6", 75)
    student_list: List[Student] = list()
    student_list.append(student1)
    student_list.append(student2)
    student_list.append(student3)
    student_list.append(student4)
    student_list.append(student5)
    student_list.append(student6)
    print("Unsorted list")
    print(student_list)
    # student_list.sort(key=lambda x:x.score)
    # print("\nAscending order")
    # print(student_list)
    # student_list.sort(key=lambda x:x.score,reverse=True)
    # print("\nDescending order")
    # print(student_list)
    print("\n**********************************************")
    print(sorted(student_list,key=lambda x:x.score,reverse=True))

