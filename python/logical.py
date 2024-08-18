# a = 30
# b = 20
# c = 5
# if a>b and a>c:
#     print(f"{a} is getter then b and c")
# elif b>a and b>c:
#     print(f"{b} is getter then a and c")
# else:
#     print(f"{c} is getter then a and b")

# **vowel consonant
# name = input("Enter a character: ")
# if name=='a' or name=='e' or name=='i' or name=='o' or name=='u':
#     print(f"{name} is vowel")
# else:
#     print(f"{name} is consonant")

# letter grade

# if marks <= 100 and marks>= 80:
i = 1
while i<5:
    marks = int(input("Enter marks: "))
    if 80 <= marks <= 100:
        print(f"cgpa {marks} = A+")
    # elif marks >= 70 and marks <=79:
    elif 70 <= marks <=79:
        print(f"cgpa {marks} = A")
    # elif marks >= 60 and marks <= 69:
    elif 60 <= marks <= 69:
        print(f"cgpa {marks} = A-")
    i = i+1

