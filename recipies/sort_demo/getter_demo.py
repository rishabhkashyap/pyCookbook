from operator import itemgetter, attrgetter

from typing import List, Dict


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
    # lst=sorted(student_list,key=attrgetter("score"),reverse=True)
    # print(lst)
    # student_list.sort(key=attrgetter("score"))
    # print(student_list)
    max_score_student:Student=max(student_list,key=attrgetter("score"))
    print(f"Max score = {max_score_student}")
    stu_list_map:List[Dict[str, int]]= [{'name': 'student1', 'score': 45},
                                        {'name': 'student4', 'score': 89},
                                        {'name': 'student2', 'score': 24}
                                        ]
    stu_sorted=sorted(stu_list_map, key=itemgetter('score'))
    print(stu_sorted)
    list_of_tuples = [(1, 2), (3, 4), (5, 0)]
    print(sorted(list_of_tuples,key=itemgetter(1)))
    print(min(list_of_tuples,key=itemgetter(0)))
    print(f"Second element of typle = {itemgetter(1)(list_of_tuples)}")
