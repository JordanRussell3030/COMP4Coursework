def FindFactors(n):
    while n > 1:
        factor = LeastFactor(n)
        print(factor)
        n = n / factor

def LeastFactor(n):
    i = 1
    while (n % i) != 0:
        i += 1
    return i

FindFactors(12)
        
