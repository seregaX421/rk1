data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    # Без использования lambda-функции
    result1 = sorted(data, key=abs, reverse=True)
    print(result1)

    # С использованием lambda-функции
    result2 = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result2)
