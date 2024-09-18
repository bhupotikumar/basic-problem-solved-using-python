# Import math to access mathmatics functions such as square roots and trigononmetric functions etc.
import math

# Define a function
def find_roots(a, b, c):
    # Calculate Discriminant
    dis = (b**2) - (4*a*c)

    if dis > 0:
        root1 = (-b + math.sqrt(dis)) / (2 * a)
        root2 = (-b - math.sqrt(dis)) / (2 * a)
        return root1, root2
    elif dis == 0:
        root = -b / (2 * a)
        return root
    else:
        return None

# Input the value of a, b and c
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

# call the find_roots function
roots = find_roots(a, b, c)

if roots is None:
    print("There are no any real roots")
else:
    print("The roots are = ", roots)