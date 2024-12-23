class Student:
    def __init__(self, student_id, group_id, fio, attendance):
        self.student_id = student_id
        self.group_id = group_id  # реализация связи один ко многим
        self.fio = fio
        self.attendance = attendance  # количественный признак


class Group:
    def __init__(self, group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name


def query_a1(students, groups):
    """
    Возвращает список списков с названиями групп и ФИО студентов.
    """
    result = []
    for student in students:
        for group in groups:
            if student.group_id == group.group_id:
                result.append([group.group_name, student.fio])
    return result


def query_a2(students, groups):
    """
    Возвращает список групп с суммарным количеством посещений, отсортированных по убыванию.
    """
    result = []
    for group in groups:
        students_in_group = filter(lambda s: s.group_id == group.group_id, students)
        total_attendance = sum(student.attendance for student in students_in_group)
        result.append([group.group_name, total_attendance])
    result.sort(key=lambda x: x[1], reverse=True)  # Сортировка по посещаемости
    return result


def query_a3(students, groups):
    """
    Возвращает группы, содержащие 'Б' в названии, и ФИО студентов из этих групп.
    """
    result = []
    for group in groups:
        if 'Б' in group.group_name:
            students_in_group = filter(lambda s: s.group_id == group.group_id, students)
            result.append([group.group_name] + [student.fio for student in students_in_group])
    return result


# Данные для тестирования
students = [
    Student(1, 1, "Иванов", 12),
    Student(2, 1, "Баранов", 10),
    Student(3, 3, "Архипов", 9),
    Student(4, 2, "Куклова", 23),
    Student(5, 3, "Панкратова", 1),
]

groups = [
    Group(1, "ИБМ3-34Б"),
    Group(2, "ИУ8-13Б"),
    Group(3, "РК1-25"),
]


# Основной код
if __name__ == "__main__":
    print("Запрос A1:", query_a1(students, groups))
    print("Запрос A2:", query_a2(students, groups))
    print("Запрос A3:", query_a3(students, groups))


# Модульное тестирование
import unittest


class TestQueries(unittest.TestCase):
    def setUp(self):
        self.students = [
            Student(1, 1, "Иванов", 12),
            Student(2, 1, "Баранов", 10),
            Student(3, 3, "Архипов", 9),
            Student(4, 2, "Куклова", 23),
            Student(5, 3, "Панкратова", 1),
        ]
        self.groups = [
            Group(1, "ИБМ3-34Б"),
            Group(2, "ИУ8-13Б"),
            Group(3, "РК1-25"),
        ]

    def test_query_a1(self):
        expected = [
            ["ИБМ3-34Б", "Иванов"],
            ["ИБМ3-34Б", "Баранов"],
            ["РК1-25", "Архипов"],
            ["ИУ8-13Б", "Куклова"],
            ["РК1-25", "Панкратова"],
        ]
        self.assertEqual(query_a1(self.students, self.groups), expected)

    def test_query_a2(self):
        expected = [
            ["ИУ8-13Б", 23],
            ["ИБМ3-34Б", 22],
            ["РК1-25", 10],
        ]
        self.assertEqual(query_a2(self.students, self.groups), expected)

    def test_query_a3(self):
        expected = [
            ["ИБМ3-34Б", "Иванов", "Баранов"],
            ["ИУ8-13Б", "Куклова"],
        ]
        self.assertEqual(query_a3(self.students, self.groups), expected)


if __name__ == "__main__":
    unittest.main()
