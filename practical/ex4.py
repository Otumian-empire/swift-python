""" write a program to evalute and print the results of the following given that a = 2 and b = 5 :

a * (2 * b) - 5
2 * (b - a) + b
(-(a * b) ** 2 - (4 * a * b) ) / ((b // a) // 3 + (16 / a / b))
((a ** 2) - (b ** 2)) // ((b - a) ** 2)
((a + b) % 2) - ((b % a) + 1)

sample output
15
11
-87.5
-3
-1
"""

a = 2
b = 5

z = a * (2 * b) - 5
print(z)

r = 2 * (b - a) + b
print(r)

q = (-(a * b) ** 2 - (4 * a * b)) / ((b // a) // 3 + (16 / a / b))
print(q)

v = ((a ** 2) - (b ** 2)) // ((b - a) ** 2)
print(v)

s = ((a + b) % 2) - ((b % a) + 1)
print(s)

