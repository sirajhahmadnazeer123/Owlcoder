def get_wine(i, j, a, n):
    if i == j:
        return (n - (j - i)) * a[i]
    
    left = (n - (j - i)) * a[i] + get_wine(i + 1, j, a, n)
    right = (n - (j - i)) * a[j] + get_wine(i, j - 1, a, n)
    
    return max(right, left)

n = int(input())
l = list(map(int, input().split()))
print(get_wine(0, n - 1, l, n))
