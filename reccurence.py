'''recurrence relation '''

#x(n) = x(n-1)+2x(n-2), x(0) = 0 and x1 = 1

def x (n):
    if n == 0: return 6
    elif n == 1: return 3
    else: return 12*x(n-1) + 3*x(n-2)
    # else: return (2**n  +1 )/ 3
    # # else : return -1*x(n-1) + 5
    # else: return 2* 3**n - (-1)**n

for i in range(0,5):
    print ("x",i,"=",x(i))

