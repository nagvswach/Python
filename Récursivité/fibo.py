""" F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) -->  pour n ≥ 2 """





def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(6))
