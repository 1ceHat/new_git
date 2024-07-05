numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers.remove(1)
primes = []
not_primes = []

for number in numbers:
    sqrt = int(number**0.5)
    del_count = 1
    for i in range(1, sqrt+1):
        if number % i == 0:
            del_count += 1
        if del_count > 2:
            break
    if del_count < 3:
        primes.append(number)
    else:
        not_primes.append(number)

print(f"Простые числа {primes}")
print(f"Не простые числа {not_primes}")