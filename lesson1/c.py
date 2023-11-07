
n1 = int(input()) # n elems of arr
arr1 = list(map(int, input().split()))
n2 = int(input()) # n elems of arr
arr2 = list(map(int, input().split()))


def merge(arr1: list, arr2: list):
    merged = []

    arr1_id = 0
    arr2_id = 0

    for _ in range(n1 + n2):
        
        if arr1_id <= n1 - 1 and arr2_id <= n2 - 1 :
            curr_elem_arr_1 = arr1[arr1_id]
            curr_elem_arr_2 = arr2[arr2_id]
            
            if curr_elem_arr_1 <= curr_elem_arr_2:
                merged.append(curr_elem_arr_1)
                arr1_id += 1

            else:
                merged.append(curr_elem_arr_2)
                arr2_id += 1

                if arr2_id == n2 - 1:
                    pass

                    # do it reqursive way

        else:
            if arr1_id == n1 - 1 and arr2_id < n2 - 1 :
                merged.extend(arr2[arr2_id:])

            elif arr1_id < n1 - 1 and arr2_id == n2 - 1 :
                merged.extend(arr1[arr1_id:])

            return merged
    
        # elif arr1_id == n1  and arr2_id < n2 :
        #     merged.extend(arr2[arr2_id:])
        #     arr2_id = n2 

        # elif arr1_id < n1  and arr2_id == n2 :
        #     merged.extend(arr2[arr1_id:])
        #     arr1_id = n1 

    return merged

print(*merge(arr1, arr2))
