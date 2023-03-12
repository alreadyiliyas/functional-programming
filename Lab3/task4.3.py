# Даны два целых числа A и В, A>B.
# Выведите все нечётные числа от A до B включительно, в порядке убывания.
# В этой задаче можно обойтись без инструкции if.

a = int(input())
even = bool(a%2==0)
b = int(input())
while (a > b and even == True):
    print(a)
    a -= 2
while (a > b and even == False):
    print(a-1)
    a-= 2
