from random import randint



def precount_x_orders(inp: str, x:int, module: int):
    precounted = [0] * (len(inp) + 1)
    precounted[0] = 1
    for order in range(1, len(inp)+1):
        precounted[order] = (x * precounted[order - 1]) % module

    return precounted

def count_substr_hash(init_hashes: str, from_id: int, len: int, precounted_x: dict, module: int):
    if from_id > 0:
        return (init_hashes[from_id + len - 1] - (init_hashes[from_id - 1] * precounted_x[len])) % module
    else:
        return init_hashes[from_id + len - 1]% module

# f = open('/home/oleg/Documents/algo4/lesson2/41')
# s = f.readline()

s =  input()


default_x_1 = randint(28, 28*2)

default_module_1 = randint(10**9 + 7, 12**9 + 7)
while default_module_1 % default_x_1 == 0:
    default_module_1 = randint(10**9 + 7, 12**9 + 7)



x_ords_1 = precount_x_orders(s, default_x_1, default_module_1)
hash_prefs_1 = count_hash_prefixes(s, default_x_1, default_module_1)
hash_prefs_1_rev = count_hash_prefixes_reversed(s, default_x_1, default_module_1)

answer = len(s)
for begin_id in range(len(s)):
    for end_id in range(begin_id,len(s)):
        checked_len = end_id - begin_id + 1
        if checked_len > 1:
            left_to_right_begin_id = begin_id
            right_to_left_begin_id = len(s) - 1 - end_id 
            
            pref_hash_1 = count_substr_hash(init_hashes=hash_prefs_1, from_id=left_to_right_begin_id, len=checked_len, precounted_x=x_ords_1, module=default_module_1)
            pref_hash_1_rev = count_substr_hash(init_hashes=hash_prefs_1_rev, from_id=right_to_left_begin_id, len=checked_len, precounted_x=x_ords_1, module=default_module_1)
        
            if pref_hash_1 == pref_hash_1_rev :
                answer += 1

print(answer)
