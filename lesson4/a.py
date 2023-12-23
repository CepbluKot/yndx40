from itertools import permutations


n = int(input())
# n = 9

f = open('output.txt', 'w')

all_perms = list(permutations(range(1, n+1)))

for perm in all_perms:
    res = ''
    for digit in perm:
        res += str(digit)
    res += '\n'
    f.write(res)
