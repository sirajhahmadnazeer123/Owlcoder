A = [12, -1, -7, 8, -15, 30, 16, 28]
N = 8
K = 3
f = []

for i in range(N - K + 1):
    subarray = A[i:i + K]
    negatives = [num for num in subarray if num < 0]

    if not negatives:
        f.append(0)
    else:
        f.append(negatives[0])

print(f)
