# Power of Three

def isPowerOfThree(n):
    while n>1:
        n = n/3
    return n==1

print(isPowerOfThree(45))