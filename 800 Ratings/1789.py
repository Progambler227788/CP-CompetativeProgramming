# Python code to demonstrate naive
# method to compute gcd ( recursion )


def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)

a = int(input())
b = int(input())

# prints 12
print(f"The gcd of {a} and {b} is : ", end="")
print(hcf(a,b))