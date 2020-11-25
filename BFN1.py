a = input('Liczba: ')
b = 0
k = 0


def is_palindrome(a, b, k):
    str(a)
    str(b)
    b = "".join(reversed(a))
    
    if a == b:
        print('Palindrom: {}, liczba dodawań: {}'.format(a, k))
    else:
        k+=1
        a = str(int(a) + int(b))
        is_palindrome(a, b, k)


print(is_palindrome(a, b, k))
