import math


def check_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


pi = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
x = 0

while (x < 90):
    input = int(pi[x:x+10])
    if check_prime(input):
        print(input)
        break
    x += 1
