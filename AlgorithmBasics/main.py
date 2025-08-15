
# Euclidean Method
def gcd(a, b):

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a

if __name__ == "__main__":

    print(gcd(123456,789012))