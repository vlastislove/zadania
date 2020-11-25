def is_prime(n, k):
    for i in range(2, n):
        if n % i == 0:
            k+=1
    if k == 0:
        return mine(print('TAK'))
    else:
        return mine(print('NIE'))
        

def mine(ans):
    k = 0
    n = int(input('Liczba: '))
    if n > 1:
        print(is_prime(n, k))
    else:
        return mine(print('NIE'))


mine(ans = '')
