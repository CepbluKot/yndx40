default_x = 3
default_module = 10**9 + 7


def count_hash_prefixes(inp: list, x: int=default_x, module: int=default_module):
    hash_prefixes = [0] * len(inp)

    hash_prefixes[0] = inp[0] % module
    for letter_id in range(1, len(inp)):
        hash_prefixes[letter_id] = (hash_prefixes[letter_id-1] * x + inp[letter_id]) % module 
    
    return hash_prefixes

def count_hash_prefixes_reversed(inp: list, x: int=default_x, module: int=default_module):
    hash_prefixes = [0] * len(inp)

    hash_prefixes[0] = inp[len(inp)-1] % module

    hash_prefs_id = 1
    for letter_id in range(len(inp)-1-1, -1, -1):
        hash_prefixes[hash_prefs_id] = (hash_prefixes[hash_prefs_id-1] * x + inp[letter_id]) % module 
        hash_prefs_id += 1

    return hash_prefixes


def precount_x_orders(inp: list, x:int=default_x):
    precounted = [0] * (len(inp) + 1)
    precounted[0] = 1
    for order in range(1, len(inp)+1):
        precounted[order] = (x * precounted[order - 1]) % default_module

    return precounted

def count_substr_hash(init_hashes: str, from_id: int, len: int, precounted_x: dict, module: int=default_module):
    if from_id > 0:
        return (init_hashes[from_id + len - 1] - (init_hashes[from_id - 1] * precounted_x[len])) % module
    else:
        return init_hashes[from_id + len - 1]% module



ss = '1212'
s = []
for chr in ss:
    s.append(int(chr))


x_ords = precount_x_orders(s)
hash_prefs = count_hash_prefixes(s)
hash_prefs_rev = count_hash_prefixes_reversed(s)

# print(hash_prefs)
# print(hash_prefs_rev)

# print(count_substr_hash(init_hashes=hash_prefs, from_id=3, len=1, precounted_x=x_ords))
# print(count_substr_hash(init_hashes=hash_prefs_rev, from_id=3, len=1, precounted_x=x_ords))
