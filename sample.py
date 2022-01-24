n = "abababcdefababcdab"
m = "ab"
j = 0
ans = ''
res = ''
while(j<=(len(n)-len(m))):
    ans = ans+n[j:j+2]
    if ans==m:
        res = res+'x'
        j+=2
        ans = ""
    else:
        res = res+n[j]
        j+=1
        ans= ""
print(res)