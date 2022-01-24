n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    arr = list(map(int,input().strip().split()))[:x]
    res = []
    for i in range(y,len(arr)):
        res.append(arr[i])
    for i in range(0,y):
        res.append(arr[i])
    for i in res:
        print(i,end=" ")
    print()
    