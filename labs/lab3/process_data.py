import json
import sys
from print_result import print_result
from cm_timer import cm_timer_1
from gen_random import gen_random
from unique import Unique

# Получаем путь к файлу из аргументов командной строки
path = sys.argv[1]

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(Unique([item['job-name'] for item in arg], ignore_case=True), key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f'{x} с опытом Python', arg))

@print_result
def f4(arg):
    salaries = gen_random(len(arg), 100000, 200000)
    return [f'{job}, зарплата {salary} руб.' for job, salary in zip(arg, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
