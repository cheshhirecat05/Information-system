import random

def fermat_primality_test(p, k=5):
    if p <= 1:
        return False
    if p <= 3:
        return True

    for _ in range(k):
        a = random.randint(2, p - 2)
        print("random integer a:", a)
        #test= a^(p-1)mod p
        test=pow(a, p - 1, p)
        print(f"Test {_+1} result: {test}")
        if test != 1:
            print(f"Test {_+1} result: {test}")

            return False

    return True


# -------- USER INPUT --------
num = int(input("Enter a number to test (Fermat): "))

if fermat_primality_test(num):
    print("Probably Prime (Fermat Test)")
else:
    print("Composite")