# Program to display the Fibonacci sequence up to n-th term

upto_num = int(input("input number of elemnt of series: "))


n1, n2 = 0, 1
count = 0

if upto_num <= 0:
   print("Please enter a positive integer")

else:
   print("Fibonacci sequence:")
   while count < upto_num:
       print(n1)
       nth = n1 + n2
    
       n1 = n2
       n2 = nth
       count += 1