n = int(input())
a = list(map(int, input().split()))
res = tuple(a)
print(hash(res))
