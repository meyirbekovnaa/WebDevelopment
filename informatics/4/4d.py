n = int(input())
a = list(map(int,input().strip().split()))[:n] 
length = len(a)
cnt = 0
for i in range(length - 1):
    if a[i + 1] > a[i]:
        cnt += 1

print(str(cnt))