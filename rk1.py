class Student:
    def __init__(self, student_id, group_id, fio, attendance):
        self.student_id = student_id
        self.group_id = group_id #реализация связи один ко многим
        self.fio = fio
        self.attendance = attendance #количественный признак

class Group:
    def __init__(self, group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name

class StudentGroup:
    def __init__(self, group_id, student_id):
        self.group_id = group_id
        self.student_id = student_id


students = [
    Student(1, 1, "Иванов",12),
    Student(2, 1, "Баранов", 10),
    Student(3, 3, "Архипов", 9),
    Student(4, 2, "Кирова", 23),
    Student(5, 3, "Панкратова", 1)
]

groups = [
    Group(1, "ИБМ3-34Б"),
    Group(2, "ИУ8-13Б"),
    Group(3, "РК1-25")
]

students_groups = [
    StudentGroup("Группа 1", 1),
    StudentGroup("Группа 1", 2),
    StudentGroup("Группа 3", 3),
    StudentGroup("Группа 2", 4),
    StudentGroup("Группа 3", 5)
]

a1 = []
a2 = []
a3 = []


def main(students, groups, a1, a2, a3):
    for student in students:
        one_to_many = []
        for group in groups:
            if student.group_id == group.group_id:
                one_to_many.append(group.group_name)
                one_to_many.append(student.fio)
                a1.append(one_to_many)

    print('Запрос A1:', a1)

    for group in groups:
        one_to_many2 = []
        cnt = 0
        students_in_group = list(filter(lambda i: i.group_id == group.group_id, students))
        one_to_many2.append(group.group_name)
        for student in students_in_group:
            cnt += student.attendance
        a2.append(one_to_many2)
        one_to_many2.append(cnt)

    for i in range(len(a2)): #сортировка по суммарному количеству посещений в группе
        for j in range(i, len(a2)):
            if a2[i][1] <= a2[j][1]:
                a2[i], a2[j] = a2[j], a2[i]

    print('Запрос A2:', a2)

    for group in groups:
        res = []
        if 'Б' in group.group_name:
            students_in_group = list(filter(lambda i: i.group_id == group.group_id, students))
            res.append(group.group_name)
            for student in students_in_group:
                res.append(student.fio)
            a3.append(res)

    print('Запрос A3:', a3)


if __name__ in '__main__':
    main(students, groups, a1, a2, a3)










