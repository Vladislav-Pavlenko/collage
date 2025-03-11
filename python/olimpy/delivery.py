def max_score(a, b):
    # Сортуємо масив a за зростанням, b - за спаданням
    a.sort()
    b.sort(reverse=True)

    # Визначаємо мінімальну довжину k
    k = min(len(a), len(b))

    # Підраховуємо максимальну суму
    max_sum = 0
    for i in range(k):
        max_sum += abs(a[i] - b[i])

    return max_sum

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if not (1 <= n <= 10**5):
    exit()
if not (1 <= m <= 10**5):
    exit()
if not all(0 <= ai <= 10**9 for ai in a):
    exit()
if not all(0 <= bi <= 10**9 for bi in b):
    exit()

a.sort()
b.sort()

k = min(n, m)

max_sum = 0
for i in range(k):
    max_sum += abs(a[i] - b[k-i-1])

print(max_sum)
