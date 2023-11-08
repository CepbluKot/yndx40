from random import randint
from copy import deepcopy

n = int(input()) # n elems of arr
arr = list(map(int, input().split()))


def merge(arr1: list, arr2: list):
    if arr1 and arr2:
        merged = [0] * (len(arr1)+len(arr2))

        arr1_id = 0
        arr2_id = 0

        while (arr1_id < len(arr1)) and (arr2_id < len(arr2)):
            arr1_selected_elem = arr1[arr1_id]
            arr2_selected_elem = arr2[arr2_id]

            if arr1_selected_elem <= arr2_selected_elem:
                merged[arr1_id + arr2_id] = arr1_selected_elem
                arr1_id += 1
            else:
                merged[arr1_id + arr2_id] = arr2_selected_elem
                arr2_id += 1

        stop_id = arr1_id + arr2_id
        if arr1_id < len(arr1):
            
            for elem in arr1[arr1_id:]:
                merged[stop_id] = elem
                stop_id += 1

        elif arr2_id < len(arr2):
            for elem in arr2[arr2_id:]:
                merged[stop_id] = elem
                stop_id += 1

        return merged

    elif arr1:
        return arr1
    
    elif arr2:
        return arr2
    
    else:
        return []

def merge_sort(arr: list) -> list:
    if len(arr) > 1:
        # not_sorted = 1
        not_sorted = 0
        i = 1
        while i < len(arr):
            if(arr[i] < arr[i - 1]):
                not_sorted = 1
                break
            i += 1


        if not_sorted:
            split_by_id = randint(1, len(arr)-1)
            # split_by_id = len(arr) // 2
            arr_1 = arr[:split_by_id]
            arr_2 = arr[split_by_id:]

            arr_1_sorted = merge_sort(arr_1)
            arr_2_sorted = merge_sort(arr_2)

            return merge(arr_1_sorted, arr_2_sorted)
       
        else:
            return arr
    
    else:
        return arr



# arr_new = [randint(1, 7) for _ in range (randint(5,8))]

# arr_1 = deepcopy(arr_new)
# arr_2 = deepcopy(arr_new)

# while arr_1 == arr_2:
#     arr_new = [randint(1, 7) for _ in range (randint(5,8))]

#     arr_1 = deepcopy(arr_new)
#     arr_2 = deepcopy(arr_new)

#     arr_1 = merge_sort(arr_1)
#     arr_2.sort()

# print(arr_new)
# print(arr_1)
# print(arr_2)

# arr = [1, 3, 4, 7, 2]
print(*merge_sort(arr))
