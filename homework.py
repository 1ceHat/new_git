import random as rnd

number = rnd.randint(3, 20)
password = ''
deliters = set()
for i in range(1, int(number**0.5)+1):
    if number%i==0:
        deliters.add(i)
        deliters.add(number//i)
sorted(deliters)


for num in range(1,number//2+1):
    for deliter in deliters:
        if num<deliter-num:
            password += str(num)+str(deliter-num)

print(number, password)