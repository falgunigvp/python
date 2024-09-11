# 11: 

n = int(input("Enter a number: "))
l = list()
if n <= 1:
    print("Not perfect")
else:
    for i in range(1, n-1):
        if n % i == 0:
            l.append(i)
    if sum(l) == n:
        print("perfect")
    else:
        print("not perfect")