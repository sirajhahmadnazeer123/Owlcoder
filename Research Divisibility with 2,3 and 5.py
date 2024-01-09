def divisibility_optimized(n):
    count = 0

    count += n // 2 + n // 3 + n // 5
    count -= n // (2 * 3) + n // (2 * 5) + n // (3 * 5)
    count += n // (2 * 3 * 5)

    return count

n = int(input("Enter a number: "))
print(divisibility_optimized(n))
