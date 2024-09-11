price = int(input("Enter the price :"))
coin=[1,2,5]

if (price<=0):
    print("0")

else:
    count = 0
    for t1 in range(0,(price//coin[0])+1):
        for t2 in range(0,(price//coin[1])+1):
            for t3 in range(0,(price//coin[2])+1):
                if (t1*coin[0]+t2*coin[1]+t3*coin[2]==price):
                    count += 1
                    print(f"{count}.combination {count}:{coin[0]} of {t1}, {coin[1]} of {t2}, {coin[2]} of {t3}")
print("total combination :- ",count)

