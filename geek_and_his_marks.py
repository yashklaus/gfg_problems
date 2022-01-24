def geek_and_marks(m,arr):
    count = 0
    for i in arr:
        if i>m:
            count+=1
    return count

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))[:n]
    res = geek_and_marks(m,arr)
    print(res)
        
