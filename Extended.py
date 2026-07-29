# Extended Euclidean Algorithm
# Also finds multiplicative inverse

# input
r1 = int(input("Enter first number: "))
r2 = int(input("Enter second number: "))

# store original values
a = r1
b = r2

# initialization of e coefficients
s1 = 1
s2 = 0

t1 = 0
t2 = 1

# algorithm
while r2 != 0:

    q = r1 // r2

    r = r1 - q * r2
    r1 = r2
    r2 = r

    s = s1 - q * s2
    s1 = s2
    s2 = s

    t = t1 - q * t2
    t1 = t2
    t2 = t


# results
print("GCD =", r1)
print("s =", s1)
print("t =", t1)

# equation
print("#Test:IS r1*s+r2*t=1?")
print(a, "* (", s1, ") +", b, "* (", t1, ") =", r1)

# multiplicative inverse
if r1 == 1:

    inverse_a = s1 % b
    inverse_b = t1 % a

    print()
    print("Multiplicative inverse of", a, "mod", b, "=", inverse_a)
    print("Multiplicative inverse of", b, "mod", a, "=", inverse_b)

else:
    print()
    print("Multiplicative inverse does not exist")