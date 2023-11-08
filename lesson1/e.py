from random import randint
from copy import deepcopy


n = int(input()) # n elems of arr
arr = [0] * n


max_amount_of_digits = 0
id = 0
for _ in range(n):
    inp_num = input()

    max_amount_of_digits = max(max_amount_of_digits, len(inp_num))
    
    arr[id] = inp_num
    id += 1


def buckets_by_1_digit(arr: list, digit_id: int):
    buckets = [[] for _ in range(10)] 
    
    for num in arr:
        num_digit = int(num[len(num) - 1 - digit_id])

        buckets[num_digit].append(num)

    return buckets

def digi_sort(arr: list, max_amount_of_digits: int, digit_id: int = 0):
    while digit_id < max_amount_of_digits:
        sorted_arr = []

        buckets = buckets_by_1_digit(arr, digit_id)

        buck_id = 0
        print('**********')
        print('Phase', digit_id + 1)
        for bucket in buckets:
            

            if bucket:
                print('Bucket ',  buck_id,': ', end='', sep='')
                print(*bucket, sep=', ')
            else:
                print('Bucket ',  buck_id,': empty', sep='')
            
            sorted_arr.extend(bucket)

            buck_id += 1

        return digi_sort(sorted_arr, max_amount_of_digits, digit_id + 1)

    return arr


print('Initial array:')
print(*arr, sep=', ')

res = digi_sort(arr, max_amount_of_digits)

print('**********')
print('Sorted array:')
print(*res, sep=', ')
