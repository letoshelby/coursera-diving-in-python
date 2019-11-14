import sys


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b**2 - 4*a*c
x_one = (-b + D**0.5)/2*a
x_two = (-b - D**0.5)/2*a
print(int(x_one))
print(int(x_two))






