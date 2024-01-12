n = int(input())
if 100 <= n <= 999:
    c = 0
    temp = n


    while temp > 0:
        digit = temp % 10
        c += digit ** 3
        temp //= 10
    if c == n:
        print("Yes")
    else:
        print("No")
