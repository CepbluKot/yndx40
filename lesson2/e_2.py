
# s = input()
# s = 'vpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdq'
# s1 = 'a'*20 + 'vpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdq'

def make_zfunc(s: str, pref_str: str=None, from_id: int=0, to_id: int=None):
    # coord systems:
    # fake: l_elem_id, fake_coords, z_func_res
    # real: real_coords
    if to_id is None:
        to_id = len(s) - 1

    to_transformed = len(s) - 1 - to_id

    z_func_res = [0] * (len(s)-from_id-to_transformed)
    l_elem_id = 0

    if pref_str is None:
        

        for fake_coords in range(1, len(s)-from_id-to_transformed):
            real_coords = fake_coords + from_id

            z_func_res[fake_coords] = min(z_func_res[fake_coords-l_elem_id], l_elem_id + z_func_res[l_elem_id] - fake_coords)
            z_func_res[fake_coords] = max(z_func_res[fake_coords], 0)
            
            wha1 = real_coords + z_func_res[fake_coords]
            wha2 = from_id + z_func_res[fake_coords]

            while z_func_res[fake_coords] < len(s)-from_id - fake_coords and s[real_coords + z_func_res[fake_coords]] == s[from_id + z_func_res[fake_coords]]:
                # find using lin search
                z_func_res[fake_coords] += 1
            
            if l_elem_id + z_func_res[l_elem_id] < fake_coords + z_func_res[fake_coords]:
                l_elem_id = fake_coords

        return z_func_res

    else:

        for fake_coords in range(1, len(s)-from_id-to_transformed):
            real_coords = fake_coords + from_id

            z_func_res[fake_coords] = min(z_func_res[fake_coords-l_elem_id], l_elem_id + z_func_res[l_elem_id] - fake_coords)
            z_func_res[fake_coords] = max(z_func_res[fake_coords], 0)
            
            while z_func_res[fake_coords] < len(s)-from_id - fake_coords and z_func_res[fake_coords] < len(pref_str) and s[real_coords + z_func_res[fake_coords]] == pref_str[from_id + z_func_res[fake_coords]] :
                # find using lin search
                z_func_res[fake_coords] += 1
            
            if l_elem_id + z_func_res[l_elem_id] < fake_coords + z_func_res[fake_coords]:
                l_elem_id = fake_coords

        return z_func_res


def make_zfunc_rev(s: str, pref_str: str=None, from_id: int=0, to_id: int=None):
    # coord systems:
    # fake: l_elem_id, fake_coords, z_func_res
    # real: real_coords
    if to_id is None:
        to_id = len(s) - 1

    to_transformed = len(s) - 1 - to_id

    z_func_res = [0] * (len(s)-from_id-to_transformed)
    l_elem_id = 0

    if pref_str is None:
        
        for fake_coords in range(1, len(s)-from_id-to_transformed):
            real_coords = fake_coords + from_id

            z_func_res[fake_coords] = min(z_func_res[fake_coords-l_elem_id], l_elem_id + z_func_res[l_elem_id] - fake_coords)
            z_func_res[fake_coords] = max(z_func_res[fake_coords], 0)
            

            wha1 = len(s) - 1 - (real_coords + z_func_res[fake_coords])
            wha2 = len(s) - 1 - z_func_res[fake_coords]
            while z_func_res[fake_coords] < len(s)-from_id - fake_coords and s[len(s) - 1 - (real_coords + z_func_res[fake_coords])] == s[len(s) - 1 -  (from_id + z_func_res[fake_coords])]:
                # find using lin search
                wha1 = len(s) - 1 - (real_coords + z_func_res[fake_coords])
                wha2 = len(s) - 1 - z_func_res[fake_coords]

                z_func_res[fake_coords] += 1
            
            if l_elem_id + z_func_res[l_elem_id] < fake_coords + z_func_res[fake_coords]:
                l_elem_id = fake_coords

        return z_func_res

    else:

        for fake_coords in range(1, len(s)-from_id-to_transformed):
            real_coords = fake_coords + from_id

            z_func_res[fake_coords] = min(z_func_res[fake_coords-l_elem_id], l_elem_id + z_func_res[l_elem_id] - fake_coords)
            z_func_res[fake_coords] = max(z_func_res[fake_coords], 0)
            
            while z_func_res[fake_coords] < len(s)-from_id - fake_coords and z_func_res[fake_coords] < len(pref_str) and s[len(s) - 1-real_coords + z_func_res[fake_coords]] == pref_str[len(s) - 1- (from_id + z_func_res[fake_coords])] :
                # find using lin search
                z_func_res[fake_coords] += 1
            
            if l_elem_id + z_func_res[l_elem_id] < fake_coords + z_func_res[fake_coords]:
                l_elem_id = fake_coords

        return z_func_res


s = '111211'
ss = '321'

print(make_zfunc(s))
print(make_zfunc(s[::-1]))
print(make_zfunc(s[::-1], from_id=0, to_id=len(s)-2))
print(make_zfunc_rev(s, from_id=0, to_id=len(s)-2))

def find_all_subpolyndroms(s: str, from_id:int=0, to_id:int=0):
    middle = (from_id - to_id) // 2
    




    find_all_subpolyndroms(s, from_id, middle, first_time=False)
    find_all_subpolyndroms(s, middle, to_id, first_time=False)
