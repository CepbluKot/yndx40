

# def count_hash_prefixes(inp: str, x: int, module: int):
#     hash_prefixes = [0] * len(inp)

#     hash_prefixes[0] = ord(inp[0]) % module
#     for letter_id in range(1, len(inp)):
#         hash_prefixes[letter_id] = (hash_prefixes[letter_id-1] * x + ord(inp[letter_id])) % module 
    
#     return hash_prefixes

# def precount_x_orders(inp: str, x:int, module: int):
#     precounted = [0] * (len(inp) + 1)
#     precounted[0] = 1
#     for order in range(1, len(inp)+1):
#         precounted[order] = (x * precounted[order - 1]) % module

#     return precounted

# def count_substr_hash(init_hashes: str, from_id: int, len: int, precounted_x: dict, module: int):
#     if from_id > 0:
#         return init_hashes[from_id + len - 1] - (init_hashes[from_id - 1] * precounted_x[len]) % module
#     else:
#         return init_hashes[from_id + len - 1]% module

f = open('input.txt')
s = f.readline()
# s = input()
# s = 'vpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdq'
# s1 = 'a'*20 + 'vpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdq'


z_func_res = [0] * len(s)


l_elem_id = 0

for i in range(1, len(s)):
    done = False
    
    z_func_res[i] = min(z_func_res[i-l_elem_id], l_elem_id + z_func_res[l_elem_id] - i)
    z_func_res[i] = max(z_func_res[i], 0)
    
    while z_func_res[i] < len(s) - i and s[i + z_func_res[i]] == s[z_func_res[i]]:
        # find using lin search
        z_func_res[i] += 1
    
    if l_elem_id + z_func_res[l_elem_id] < i + z_func_res[i]:
        l_elem_id = i

print(*z_func_res)
