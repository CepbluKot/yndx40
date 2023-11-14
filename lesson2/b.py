from random import randint


default_x_1 = randint(2, 99)
default_x_2 = randint(2, 99)
default_x_3 = randint(2, 99)
default_x_4 = randint(2, 99)
default_x_5 = randint(2, 99)
default_x_6 = randint(2, 99)


default_module_1 = randint(10**9 + 7, 90**9 + 7)
while default_module_1 % default_x_1 == 0:
    default_module_1 = randint(10**9 + 7, 90**9 + 7)

default_module_2 = randint(10**9 + 7, 90**9 + 7)
while default_module_2 % default_x_2 == 0:
    default_module_2 = randint(10**9 + 7, 90**9 + 7)
    
default_module_3 = randint(10**9 + 7, 90**9 + 7)
while default_module_3 % default_x_3 == 0:
    default_module_3 = randint(10**9 + 7, 90**9 + 7)
    

default_module_4 = randint(10**9 + 7, 90**9 + 7)
while default_module_4 % default_x_4 == 0:
    default_module_4 = randint(10**9 + 7, 90**9 + 7)

default_module_5 = randint(10**9 + 7, 90**9 + 7)
while default_module_5 % default_x_5 == 0:
    default_module_5 = randint(10**9 + 7, 90**9 + 7)
    
default_module_6 = randint(10**9 + 7, 90**9 + 7)
while default_module_6 % default_x_6 == 0:
    default_module_6 = randint(10**9 + 7, 90**9 + 7)


def count_hash_prefixes(inp: str, x: int, module: int):
    hash_prefixes = [0] * len(inp)

    hash_prefixes[0] = ord(inp[0]) % module
    for letter_id in range(1, len(inp)):
        hash_prefixes[letter_id] = (hash_prefixes[letter_id-1] * x + ord(inp[letter_id])) % module 
    
    return hash_prefixes

def precount_x_orders(inp: str, x:int, module: int):
    precounted = [0] * (len(inp) + 1)
    precounted[0] = 1
    for order in range(1, len(inp)+1):
        precounted[order] = (x * precounted[order - 1]) % module

    return precounted

def count_substr_hash(init_hashes: str, from_id: int, len: int, precounted_x: dict, module: int):
    if from_id > 0:
        return init_hashes[from_id + len - 1] - (init_hashes[from_id - 1] * precounted_x[len]) % module
    else:
        return init_hashes[from_id + len - 1]% module

s = input()
# s = 'vpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdq'
# s1 = 'a'*20 + 'vpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdq'


x_ords_1 = precount_x_orders(s, default_x_1, default_module_1)
x_ords_2 = precount_x_orders(s, default_x_2, default_module_2)
x_ords_3 = precount_x_orders(s, default_x_3, default_module_3)
x_ords_4 = precount_x_orders(s, default_x_4, default_module_4)
x_ords_5 = precount_x_orders(s, default_x_5, default_module_5)
x_ords_6 = precount_x_orders(s, default_x_6, default_module_6)

hash_prefs_1 = count_hash_prefixes(s, default_x_1, default_module_1)
hash_prefs_2 = count_hash_prefixes(s, default_x_2, default_module_2)
hash_prefs_3 = count_hash_prefixes(s, default_x_3, default_module_3)
hash_prefs_4 = count_hash_prefixes(s, default_x_4, default_module_4)
hash_prefs_5 = count_hash_prefixes(s, default_x_5, default_module_5)
hash_prefs_6 = count_hash_prefixes(s, default_x_6, default_module_6)




min_found = None


for checked_len in range(len(s) - 1, 0, -1):
    pref_begin_id = 0
    suff_begin_id = pref_begin_id + (len(s) - checked_len)

    pref_hash_1 = count_substr_hash(init_hashes=hash_prefs_1, from_id=pref_begin_id, len=checked_len, precounted_x=x_ords_1, module=default_module_1)
    suff_hash_1 = count_substr_hash(init_hashes=hash_prefs_1, from_id=suff_begin_id, len=checked_len, precounted_x=x_ords_1, module=default_module_1)

    pref_hash_2 = count_substr_hash(init_hashes=hash_prefs_2, from_id=pref_begin_id, len=checked_len, precounted_x=x_ords_2, module=default_module_2)
    suff_hash_2 = count_substr_hash(init_hashes=hash_prefs_2, from_id=suff_begin_id, len=checked_len, precounted_x=x_ords_2, module=default_module_2)

    pref_hash_3 = count_substr_hash(init_hashes=hash_prefs_3, from_id=pref_begin_id, len=checked_len, precounted_x=x_ords_3, module=default_module_3)
    suff_hash_3 = count_substr_hash(init_hashes=hash_prefs_3, from_id=suff_begin_id, len=checked_len, precounted_x=x_ords_3, module=default_module_3)


    pref_hash_4 = count_substr_hash(init_hashes=hash_prefs_4, from_id=pref_begin_id, len=checked_len, precounted_x=x_ords_4, module=default_module_4)
    suff_hash_4 = count_substr_hash(init_hashes=hash_prefs_4, from_id=suff_begin_id, len=checked_len, precounted_x=x_ords_4, module=default_module_4)

    pref_hash_5 = count_substr_hash(init_hashes=hash_prefs_5, from_id=pref_begin_id, len=checked_len, precounted_x=x_ords_5, module=default_module_5)
    suff_hash_5 = count_substr_hash(init_hashes=hash_prefs_5, from_id=suff_begin_id, len=checked_len, precounted_x=x_ords_5, module=default_module_5)

    pref_hash_6 = count_substr_hash(init_hashes=hash_prefs_6, from_id=pref_begin_id, len=checked_len, precounted_x=x_ords_6, module=default_module_6)
    suff_hash_6 = count_substr_hash(init_hashes=hash_prefs_6, from_id=suff_begin_id, len=checked_len, precounted_x=x_ords_6, module=default_module_6)


    if (pref_hash_1 == suff_hash_1 ) or (pref_hash_2 == suff_hash_2) or (pref_hash_3 == suff_hash_3 ) or (pref_hash_4 == suff_hash_4 ) or (pref_hash_5 == suff_hash_5) or (pref_hash_6 == suff_hash_6 ) :
   
        if min_found is None:
            min_found = len(s) - checked_len
        else:
            min_found = min(len(s) - checked_len, min_found)


if not min_found is None:
    print(min_found)

else:
    print(len(s))
