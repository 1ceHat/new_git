def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        num_sqrt = int(res ** 0.5)
        prime = 'Простое'
        delit = []
        for i in range(1, num_sqrt + 1):
            if res % i == 0:
                delit.append(i)
                delit.append(res // i)
            if len(delit) > 2:
                prime = 'Составное'
                break
        print(prime)
        return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(3, 3, 6)
print(result)
