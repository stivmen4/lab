
# 1. Функція перевірки на парність/непарність числа
def check_number(num):
    if isinstance(num, (int, float)):
        return "Ïàðíå" if num % 2 == 0 else "Íåïàðíå"
    else:
        return ""

# 2. Функція знаходження суми перших п'яти простих чисел
def sum_of_primes():
    primes = []
    num = 2
    while len(primes) < 5:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
        num += 1
    return sum(primes)

# 3. Функція для обчислення суми ряду
def sum_of_series(n):
    result = 0
    for i in range(1, n + 1):
        number = int('1' * i)
        result += number
    return result

# Приклади викликів функцій:
print(check_number(10))  # Виведе "Парне"
print(check_number(7))   # Виведе "Непарне"
print(check_number("abc"))  # Виведе ""

print(sum_of_primes())   # Знайде суму перших п'яти простих чисел

print(sum_of_series(5))  # Виведе 12345 
