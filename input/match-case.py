# a = int(input("Enter Number : "))

# match a:
#     case 0:
#         print('x is zero')
#     case 4:
#         print('x is Four')
#     case _:
#         print('x is numbers')
a = int(input("Enter Number : "))

match a:
    case 0:
        print('x is zero')
    case 4:
        print('x is Four')
    case _ if a!=90:
        print('x is not equal 90')
    case _ if a !=80:
        print('x is not equal 80')
    case _:
        print("This is number")