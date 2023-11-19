
# s = input()
# s = 'vpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdq'
# s1 = 'a'*20 + 'vpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdqznunkvpkuywezpuqhsgdq'

def make_zfunc(s: str, pref_str: str=None, from_id: int=0, to_id: int=None):
    # coord systems:
    # fake: l_elem_id, fake_coords, z_func_res
    # real: real_coords
    if to_id is None:
        to_id = len(s)

    to_transformed = len(s) - to_id

    z_func_res = [0] * (len(s)-from_id-to_transformed)
    l_elem_id = 0

    if pref_str is None:
        

        for fake_coords in range(1, len(s)-from_id-to_transformed):
            real_coords = fake_coords + from_id

            z_func_res[fake_coords] = min(z_func_res[fake_coords-l_elem_id], l_elem_id + z_func_res[l_elem_id] - fake_coords)
            z_func_res[fake_coords] = max(z_func_res[fake_coords], 0)
            
            while z_func_res[fake_coords] < len(s)-from_id - fake_coords and s[real_coords + z_func_res[fake_coords]] == s[z_func_res[fake_coords]]:
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
            
            while z_func_res[fake_coords] < len(s)-from_id - fake_coords and z_func_res[fake_coords] < len(pref_str) and s[real_coords + z_func_res[fake_coords]] == pref_str[z_func_res[fake_coords]] :
                # find using lin search
                z_func_res[fake_coords] += 1
            
            if l_elem_id + z_func_res[l_elem_id] < fake_coords + z_func_res[fake_coords]:
                l_elem_id = fake_coords

        return z_func_res


s = '111111'
ss = '321'

print(make_zfunc(s))
print(make_zfunc(s,  from_id=1, to_id=4))
# def find_all_subpolyndroms(s: str):
#     middle = len(s) // 2

