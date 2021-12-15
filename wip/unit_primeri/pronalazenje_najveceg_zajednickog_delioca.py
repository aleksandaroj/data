# pronalazenje najveceg zajednickog delioca

def gcd(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b

    return a


print(gcd(60, 96))  # 12
print(gcd(96, 60))
print(gcd(20, 8))  # 4
