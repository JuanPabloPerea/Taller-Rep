x = input ("ingrese un numero: ")
n = int(x)
def factorial(n):
    fac = 1
    while n > 1 :
        fac = fac*n
        n = n-1
    return fac
print (factorial(n))
        



