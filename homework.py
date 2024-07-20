from matplotlib import pyplot as plt


# N' = -lamda*N
def f(t, N, lam=0.0866434):  # Функция вычисления значения N' (вероятность радиоактивного распада)
    return -1 * lam * N


def eyler(t0=0, N0=0, t1=16, num=100, lam=1): # Функция эйлера
    dt = (t1 - t0) / num

    t = [t0]
    N = [N0]

    for i in range(num):
        t.append(t[i] + dt)
        N.append(N[i] + dt * f(t[i], N[i], lam))

    return t, N


lam = []
i = 0.1
while i < 1:
    lam.append(i)
    i += 0.1

t = []
N = []
#N0 = int(input('Введите кол-во ядер в момент t=0: '))
N0 = 10
for i in lam:
    t, N = eyler(0, N0, 16, 100, i)
    plt.plot(t, N) # создаём график со значениями по x и y (t, N)
    plt.xlabel('Время') # меняем название оси Ох
    plt.ylabel('Количество ядер') # меняем название оси Оу
plt.show()
