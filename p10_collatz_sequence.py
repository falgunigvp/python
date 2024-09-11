''' 10: collatz sequence 1. for even numbers, divide by 2; 2. for odd numbers,multiply by 3 and add 1;
3.repeat above steps until it becmes 1.'''


n = int(input("Input a positive integer (n): "))

print(n, end=" ")

while n != 1:
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = 3 * n + 1
    print(n, end=" ")