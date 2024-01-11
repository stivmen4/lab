
# 1. ������� �������� �� �������/��������� �����
def check_number(num):
    if isinstance(num, (int, float)):
        return "�����" if num % 2 == 0 else "�������"
    else:
        return ""

# 2. ������� ����������� ���� ������ �'��� ������� �����
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

# 3. ������� ��� ���������� ���� ����
def sum_of_series(n):
    result = 0
    for i in range(1, n + 1):
        number = int('1' * i)
        result += number
    return result

# �������� ������� �������:
print(check_number(10))  # ������ "�����"
print(check_number(7))   # ������ "�������"
print(check_number("abc"))  # ������ ""

print(sum_of_primes())   # ������ ���� ������ �'��� ������� �����

print(sum_of_series(5))  # ������ 12345 
