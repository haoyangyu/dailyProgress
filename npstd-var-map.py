import numpy as np

fi = [ 11, 15, 14, 5, 8 ]
xi = [ 63.5, 69.5, 75.5, 81.5, 87.5 ]

data = np.repeat(xi, fi)
print("data")
print(data)

std = np.std(data)
var = np.var(data)
print("std")
print(std)
print("var")
print(var)

xi2 = map(lambda x: x * x, xi)
fixi2 = map(lambda x, y: x * y, fi ,xi2 )
fixi = map(lambda x, y: x * y, fi, xi)
fixiP2 = map(lambda x: x * x, fixi )
sumfixi2 = sum(fixi2)
sumfixiP2 = sum(fixiP2)

print(fixi2)
print(fixiP2)
print(sumfixi2)
print(sumfixiP2)
