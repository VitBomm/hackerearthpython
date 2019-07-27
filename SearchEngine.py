from collections import defaultdict
n, q = map(int,input().split())

diction = defaultdict(int)
for i in range(n):
    a, b = input().split()
    b = int(b)
    for j in range(len(a)+1):
        if diction[a[0:j]] < b:
            diction[a[0:j]] = b
    
for j in range(q):
    a = input()
    if diction[a] == 0:
        print("-1")
    else:
        print(diction[a])

    
