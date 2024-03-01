def factor(f):
    if f == 1:
        return 1
    if f == 0:
        return 1
    else:
        return factor(f-1)*f

def sochet(k, k1):
    o = factor(k)/(factor(k1) * factor(k-k1))
    return o

def fbernuli(n, k, p, q):
    x = sochet(n, k)*(p**(k))* (q**(n-k))
    return x

#1В среднем 20% пакетов акций на аукционах продаются по первоначально заявленной цене. 
# Найти вероятность того, что из 9 пакетов акций в результате торгов по первоначально заявленной цене: 
#     1) не будут проданы 5 пакетов; 
#     2) будет продано: а) менее 2 пакетов; б) не более 2; в) хотя бы 2 пакета; г) наивероятнейшее число пакетов
A1 = int(input("Сколько пакетов продаются по первоначальной цене?"))/100
n1 = int(input("Сколько пакетов продается?"))
Pan = int(input("Сколько пакетов не продано?"))
P1 = 1-A1
#1
Pa11 =  fbernuli(n1, Pan, P1, A1) #вероятность того, что не продано n пакетов
#2a
k11 = 1
k10 = 0
k12=2
Pa12 =  fbernuli(n1, k11, A1, P1) + fbernuli(n1, k10, A1, P1)
#2b
Pa13 = fbernuli(n1, k11, A1, P1) + fbernuli(n1, k10, A1, P1) + fbernuli(n1, k12, A1, P1)
#2c
Pa14 = 1- fbernuli(n1, k11, A1, P1) - fbernuli(n1, k10, A1, P1)
#2d 
k11D = n1* A1 - P1
k12D = n1*A1 + A1
Pa15 = fbernuli(n1, k11D, A1, P1) + fbernuli(n1, k12D, A1, P1)
print(Pa11, Pa12, Pa13, Pa14, Pa15)


