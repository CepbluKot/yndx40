default_x = 3
default_module = 10**9 + 7


def count_hash_prefixes(inp: str, x: int=default_x, module: int=default_module):
    hash_prefixes = [0] * len(inp)

    hash_prefixes[0] = ord(inp[0]) % module
    for letter_id in range(1, len(inp)):
        hash_prefixes[letter_id] = (hash_prefixes[letter_id-1] * x + ord(inp[letter_id])) % module 
    
    return hash_prefixes

def precount_x_orders(inp: str, x:int=default_x):
    precounted = [0] * (len(inp) + 1)
    precounted[0] = 1
    for order in range(1, len(inp)+1):
        precounted[order] = (x * precounted[order - 1]) % default_module

    return precounted

def count_substr_hash(init_hashes: str, from_id: int, len: int, precounted_x: dict, module: int=default_module):
    if from_id > 0:
        return init_hashes[from_id + len - 1] - (init_hashes[from_id - 1] * precounted_x[len]) % module
    else:
        return init_hashes[from_id + len - 1]% module


f = open('input.txt')
# f = open('43')

# s = input()
# q = int(input())
s = f.readline()
q = int(f.readline())

x_ords = precount_x_orders(s)
hash_prefs = count_hash_prefixes(s)



# cache = {}


res = [0] * q
for id in range(q):
    l, a, b = f.readline().split()
    # l, a, b = input().split()
    l, a, b = int(l), int(a), int(b)
      
    res_a = count_substr_hash(init_hashes=hash_prefs, from_id=a, len=l, precounted_x=x_ords)

    res_b = count_substr_hash(init_hashes=hash_prefs, from_id=b, len=l, precounted_x=x_ords)


    if res_a == res_b:
        print( 'yes')
        # pass
    else:
        print('no')
        # pass
# print(count_substr_hash(init_hashes=hash_prefs, from_id=0, len=2, precounted_x=x_ords))
# print(count_substr_hash(init_hashes=hash_prefs, from_id=4, len=2, precounted_x=x_ords))
# print(count_substr_hash(init_hashes=hash_prefs, from_id=6, len=2, precounted_x=x_ords))
