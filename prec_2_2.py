
n = int(input("Enter the index up to which you want the Fibonacci string sequence: "))

if n < 0:
       print("Index must be a non-negative integer.")
else:
     
    a = "A"
    b = "B"       
    print(a)
              
    for i in range(2, n + 1):
                  
        a, b = b, b + a
        print(b)


