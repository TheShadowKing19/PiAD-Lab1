import numpy as np

#  Tablice
a = np.array([1, 2, 3, 4, 5, 6, 7])
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(a)
print(b)

b = np.transpose(b)
print(b)

c = np.arange(0, 101)
print(c)

d = np.linspace(0, 2, 10)
print(d)

e = np.arange(0, 105, 5)
print(e)


# Liczby Losowe
f = np.random.rand(20)
f = np.around(f, 2)
print(f)

g = np.random.randint(1, 1000+1, 100)
print(g)

zero_a = np.zeros((3, 2))
one_a = np.ones((3, 2))
print(zero_a)
print(one_a)
