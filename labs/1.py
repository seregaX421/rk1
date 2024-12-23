import math
import sys


def get_coef(index):
    coef_dict = {1:'A', 2:'B', 3:'C'}
    prompt = f'Пожалуйста введи валидный коэффициент {coef_dict[index]}: '
    try:
        coef = float(sys.argv[index])
    except:
        while True:
            coef = input(prompt)
            try:
                coef = float(coef)
                break
            except:
                print(prompt)
    return coef

a = get_coef(1)
b = get_coef(2)
c = get_coef(3)
D = math.pow(b,2) - 4 * a * c
response = 'Корни биквадратного уравнения '
if D > 0:
    x1_2 = (-b + math.sqrt(D)) / (2 * a)
    x2_2 = (-b - math.sqrt(D)) / (2 * a)
    roots = [math.sqrt(x) for x in (x1_2, x2_2) if x >= 0]
    response += '{}'.format(*roots) if roots else 'отсутствуют'
elif int(D) == 0:
    x_2 = -b / (2 * a)
    root = math.sqrt(x_2) if x_2 > 0 else 'отсутствуют'
else:
    response = 'Уравнение не имеет действительных решений'
print(response)