n = int(input())

arr = []

for i in range(n):
    name, score = input().split()
    arr.append((int(score), name))

arr.sort()
print(' '.join(name for _, name in arr))
