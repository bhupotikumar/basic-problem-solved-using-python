# Input Your Marks
marks = int(input("Enter Your Marks : "))

# Conditions for find out Grade
if marks >= 90:
    print("Your Grade is A+")
elif marks >= 80:
    print("Your Grade is A")
elif marks >= 70:
    print("Your Grade is A-")
elif marks >= 60:
    print("Your Grade is B+")
elif marks >= 50:
    print("Your Grade is B")
elif marks >= 40:
    print("Your Grade is C")
else:
    print("""Your Grade is F
You are failed""")
