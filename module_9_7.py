
def is_prime(func):
    def wrapper(*args):
        """ Определяет простое число """
        a = func(*args)
        k = 0
        # Поиск делителей
        for i in range(2, a // 2+1):
            if a % i == 0:
                k = k+1
        if k <= 0:
            print('Простое')
            return a
        else:
            print('Составное')
            return a
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)