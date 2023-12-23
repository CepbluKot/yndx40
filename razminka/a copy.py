n,m = input().split()
n,m=int(n),int(m)

seq = list(map(int , input().split()))


for _ in range(m):
    l,r = input().split()
    l,r = int(l),int(r)

    max_el = max(seq[l:r+1])
    min_el = min(seq[l:r+1])

    if max_el == min_el:
        print('NOT FOUND')
    else:
        print(max_el)
        