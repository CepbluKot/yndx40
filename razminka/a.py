n,m = input().split()
n,m=int(n),int(m)

seq = list(map(int , input().split()))


# max_prefs = [[0] for _ in range(n)]

# for dig_id in range(n):
#     for elem_id in range(dig_id, n):
#         max_prefs[dig_id].append(max(max_prefs[dig_id][-1], seq[elem_id]))
# 1
# for _ in range(m):
#     l,r = input().split()
#     l,r = int(l),int(r)

#     l_min_val = max_prefs[l][1]
#     r_min_val = max_prefs[r][1]

#     if l_min_val == r_min_val:
#         print('NOT FOUND')
#     else:
#         print(max_prefs[0][r+1])


max_pref = [0]
for elem in seq:
    max_pref.append(max(max_pref[-1], elem))


for _ in range(m):
    l,r = input().split()
    l,r = int(l),int(r)

    # if l_min_val == r_min_val:
    #     print('NOT FOUND')
    # else:
    #     print(max_prefs[0][r+1])
