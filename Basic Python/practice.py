
def solve():
    n = int (input())
    st = input().split()
    list = []
    for i in range(0, n):
        x = int (st[i])
        list.append(x)
    
    ans = 1e9
    for i in range(0, n):
        for j in range(i + 1, n):
            x = list[i] + list[j] + j - i
            ans = min(ans, x)
    
    print(ans)

tc = int (input())
while tc > 0:
    tc -= 1
    solve()