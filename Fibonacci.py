#fibonacci series

def print_fibonacci(num):
    a,b = 0,1
    if num < 1:
        print("null")
    elif num == 1:
        print(a)
    elif num == 2:
        print(a)
        print(b)
    elif num > 2:
        print(a)
        print(b)
        #genrate next number in series
        for i in range (num - 2):
            c = a + b
            #update  a and b for next iteration
            a,b = b,c
            print(c)

print_fibonacci(eval(input("enter a number for fibonacci series: ")))