from random import randint


def count_hash_prefixes(inp: list, x: int, module: int):
    hash_prefixes = [0] * len(inp)

    hash_prefixes[0] = inp[0] % module
    for letter_id in range(1, len(inp)):
        hash_prefixes[letter_id] = (hash_prefixes[letter_id-1] * x + inp[letter_id]) % module 
    
    return hash_prefixes


def count_hash_prefixes_reversed(inp: list, x: int, module: int):
    hash_prefixes = [0] * len(inp)

    hash_prefixes[0] = inp[len(inp)-1] % module

    hash_prefs_id = 1
    for letter_id in range(len(inp)-1-1, -1, -1):
        hash_prefixes[hash_prefs_id] = (hash_prefixes[hash_prefs_id-1] * x + inp[letter_id]) % module 
        hash_prefs_id += 1

    return hash_prefixes


def precount_x_orders(inp: str, x:int, module: int):
    precounted = [0] * (len(inp) + 1)
    precounted[0] = 1
    for order in range(1, len(inp)+1):
        precounted[order] = (x * precounted[order - 1]) % module

    return precounted

def count_substr_hash(init_hashes: str, from_id: int, len: int, precounted_x: dict, module: int):
    if from_id > 0:
        what_1 = init_hashes[from_id + len - 1] 
        what_2 = init_hashes[from_id - 1] * precounted_x[len]

        return (init_hashes[from_id + len - 1] - (init_hashes[from_id - 1] * precounted_x[len])) % module
    else:
        return init_hashes[from_id + len - 1]% module

# f = open('input.txt')
# s = f.readline()

sz, colors = input().split()
sz, colors = int(sz), int(colors)
s = list(map(int, input().split()))
len_s = len(s)

# s = 'vpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdq'
# s1 = 'a'*20 + 'vpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdq'



default_x_1 = randint(colors, colors*2)

default_module_1 = randint(10**9 + 7, 90**9 + 7)
while default_module_1 % default_x_1 == 0:
    default_module_1 = randint(10**9 + 7, 90**9 + 7)



x_ords_1 = precount_x_orders(s, default_x_1, default_module_1)
hash_prefs_1 = count_hash_prefixes(s, default_x_1, default_module_1)
hash_prefs_1_rev = count_hash_prefixes_reversed(s, default_x_1, default_module_1)


answers = []
for delimit_len in range(len(s)//2, 0, -1):
    pref_hash_1 = count_substr_hash(init_hashes=hash_prefs_1, from_id=0, len=delimit_len, precounted_x=x_ords_1, module=default_module_1)
    pref_hash_1_rev = count_substr_hash(init_hashes=hash_prefs_1_rev, from_id=len(s)-2*delimit_len, len=delimit_len, precounted_x=x_ords_1, module=default_module_1)


    
    if pref_hash_1 == pref_hash_1_rev :

        # print(s[:delimit_len], ' | ', s[delimit_len:])
        answers.append(len(s)-delimit_len)

answers.append(len(s))
print(*answers)
