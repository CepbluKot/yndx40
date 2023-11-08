
n1 = int(input()) # n elems of arr
arr1 = list(map(int, input().split()))
n2 = int(input()) # n elems of arr
arr2 = list(map(int, input().split()))


def merge(arr1: list, arr2: list):
    if arr1 and arr2:
        merged = [0] * (n1+n2)

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

print(*merge(arr1, arr2))
