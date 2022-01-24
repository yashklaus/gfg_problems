def geekonacci(a,b,c,n):
    if n==4:
        return a+b+c
    return geekonacci(b,c,a+b+c,n-1)

t = int(input())
for _ in range(t):
    a,b,c,n = map(int, input().split())
    d = geekonacci(a,b,c,n)
    print(d)
    
    
