import matplotlib.pyplot as plt
import scipy.integrate
import sympy

# Найти математическое ожидание случайной величины Z = 8X - 5Y + 7 , если известно, что M ( X ) = 3, M (Y ) = 2 .
print("Формула Z = 8X - 5Y + 7")
Mx = int(input("M(x)=?"))
My = int(input("M(y)=?"))
Mz = 8*Mx - 5*My + 7
print("M(z)= ", Mz)

# 2. Найти дисперсию случайной величины Z = 8X - 5Y + 7 , если известно, что случайные величины X и Y независимы и D(X ) = 1,5, D(Y ) = 1.
print("Формула Z = 8X - 5Y + 7")
Dx = float(input("D(x)=?"))
Dy = float(input("D(y)=?"))
Dz = 8*8*Dx - 5*5*Dy + 7
print("D(z)= ", Dz)
# 3. Ряд распределения дискретной случайной величины состоит из двух неизвестных значений.
# Вероятность того, что случайная величина примет одно из этих значений, равна 0,8.
# Составить ряд распределения случайной величины, если ее математическое ожидание равно 3,2, а дисперсия 0,16.
P3 = float(input("Введите вероятность принятия случайного значения"))
P31 = P3-1
Mx = float(input("M(x)=?"))
Dx = float(input("D(x)=?"))
# P3*x1 +P31 * x2 = Mx
# (P3**2) * x1 +(P31**2) * x2 = Dx

x1 = sympy.Symbol("x1")
x2 = sympy.Symbol("x2")
eq1 = sympy.Eq(P3*x1 +P31*x2, Mx)
eq2 = sympy.Eq((x1**2)*P3 + (x2**2)*P31 - (Mx**2), Dx)
M = sympy.solve([eq1, eq2], (x1, x2))
print("Решение: ", M)

# 4. Даны законы распределения двух независимых случайных величин:
# Найти математическое ожидание и дисперсию случайной величины Z = 2X+3Y.
print("Формула Z = 2X+3Y")

xi = [int(value) for value in input("Введите xi через пробел").split()]
pxi = [float(value) for value in input("Введите Pi через пробел").split()]
yi = [int(value) for value in input("Введите yi через пробел").split()]
pyi = [float(value) for value in input("Введите Pi через пробел").split()]
zij = []
zij2 = []
Pi=[]
for i in range(len(xi)):
    for j in range(len(yi)):
        k = 2*xi[i]+3*yi[j]
        k1 = k**2
        zij.append(k)
        zij2.append(k1)
        k3 = pxi[i]*pyi[j]
        Pi.append(k3)
Mx=0
for i in range(len(zij)):
    Mx = Mx + zij[i]*Pi[i] #<-тут все прекрасно
x=0
for j in range(len(zij2)):
    x = x + (zij2[j]*Pi[i])
Dx = x - (Mx**2)

print("Математическое ожидание: ", Mx, "\nДисперсия: ", Dx)

# 5. Число иногородних судов, прибывающих ежедневно под погрузку в определенный порт – случайная величина X, заданная так:
# х 3 4 5 6 7
# р 0.1 0.2 0.4 0.1 0.2
# а) Найти функцию распределения вероятностей дискретной СВ Х, построить ее график;
# б) Если в заданный день прибывает больше пяти судов, то порт берет на себя ответственность за издержки вследствие необходимости нанимать дополнительных водителей и грузчиков. Чему равна вероятность того, что порт понесет дополнительные расходы?
# в) Найти математическое ожидание и дисперсию случайной величины X.
xi = [0]+[int(value) for value in input("Введите xi через пробел").split()]
pxi = [0.0] + [float(value) for value in input("Введите Pi через пробел").split()]
Fx=[]
k=0
for i in range(len(pxi)):
    k = k + pxi[i]
    Fx.append(k)
# Создать данные для графика
fig, ax = plt.subplots()
x1 = [xi[0], xi[1]]
y1 = [Fx[0], Fx[0]]
x2 = [xi[1], xi[2]]
y2 = [Fx[1], Fx[1]]
x3 = [xi[2], xi[3]]
y3 = [Fx[2], Fx[2]]
x4 = [xi[3], xi[4]]
y4 = [Fx[3], Fx[3]]
x5 = [xi[4], xi[5]]
y5 = [Fx[4], Fx[4]]
ax.plot(x1, y1, color='red')
ax.plot( x2, y2, color='red')
ax.plot(x3, y3, color='red')
ax.plot(x4, y4, color='red')
ax.plot(x5, y5,color='red')
plt.show()
P5 = pxi[4]+pxi[5]
Mx=0
for i in range(len(xi)):
    Mx+=(xi[i]*pxi[i])
Dx=0
for i in range(len(xi)):
    Dx+=((xi[i]**2) * pxi[i])
print("P(x>5)= ", P5, "\nM(x)= ", Mx, "\nD(x)= ", Dx)

# 6. Случайная величина X задана плотностью вероятности f(x)=x/2 в интервале (0; 2),
# вне этого интервала f(x)=0. Найти математическое ожидание и дисперсию случайной величины X.

fx = float(input("Введите плотностью вероятности:"))
x = [int(value) for value in input("Введите интервал через пробел").split()]
f0 = int(input("Введите значение вне интервала:"))
def f(x):
    return x*x/2
x0=x[0]
x1=x[1]
integral, error = scipy.integrate.quad(f, x0, x1)

def f1(x):
    return (x**2)* x/2
x0=x[0]
x1=x[1]
integral1, error1 = scipy.integrate.quad(f1, x0, x1)
Dx= integral1- (integral**2)

print("Математическое ожидание: ", integral, "\nДисперсия: ", Dx)

# 7. Случайная величина х задана интегральной функцией
# 𝐹(𝑥)= {0 при х≤0 х**2/36 при 0<х≤6 1 при х>6
# Требуется:
# а) найти дифференциальную функцию (плотность вероятности);
# б) найти математическое ожидание и дисперсию х;
# в) построить графики интегральной и дифференциальной функций.
def f(x):
    return x*x/18
def f1(x):
    return x*x*x/18
integral, error = scipy.integrate.quad(f, 0, 6)
integral1, error1 = scipy.integrate.quad(f1, 0, 6)
Dx = integral1 - integral**2

print("Математическое ожидание: ", integral, "\nДисперсия: ", Dx)


# 8. Дана функция распределения вероятностей случайной величины
# а) найти плотность вероятности f(x),
# б) построить графики f(x) и F(x),
# в) найти вероятности P(X=1), P(X<1), H(1<=X<2),
# г) вычислить M(X), D(X)

def f(x):
    return x*x/2
def f1(x):
    return x*x*x/2
integral, error = scipy.integrate.quad(f, 0, 2)
integral1, error1 = scipy.integrate.quad(f1, 0, 2)
Dx = integral1 - integral**2
Px1 =0
Px11=1/4
P1x2 = 3/4
print("Математическое ожидание: ", integral, "\nДисперсия: ", Dx, "\nP(x=1): ", Px1, "\nP(x<1): ", Px11)
