from functools import total_ordering
from typing import List


@total_ordering
class Student:
    __slots__ = ['name', 'score']

    def __init__(self, name: str, score: int):
        self.name: str = name
        self.score: int = score

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Student) and self.score == o.score

    def __lt__(self, other) -> bool:
        return isinstance(other, Student) and self.score < other.score

    def __repr__(self) -> str:
        return "(name = " + self.name + "  score = " + str(self.score) + ")"


if __name__ == '__main__':
    student2: Student = Student("Spock", 100)
    student1: Student = Student("Kirk", 50)
    student4: Student = Student("Mccoy", 50)
    student3: Student = Student("Scotty", 60)
    stu_list: List[Student] = list()
    stu_list.append(student4)
    stu_list.append(student2)
    stu_list.append(student3)
    stu_list.append(student1)

    # stu_list.sort(reverse=True)
    # print(stu_list)
    print(sorted(stu_list, reverse=True))
