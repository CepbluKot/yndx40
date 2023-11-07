# partition

from random import randint, choice



n = int(input()) # n elems of arr
arr = list(map(int, input().split()))
x = int(input()) # support element


def make_partition(x: int, arr: list, begin: int=0, end: int=len(arr)):
    # making partition by elem using  3 ptrs

    if len(arr) >= 2:
        begin_equals_id = -1
        begin_greater_id = -1
        curr_elem_id = 1

        while curr_elem_id < end:
            first_elem = arr[begin]
            curr_elem = arr[curr_elem_id]
            prev_elem = arr[curr_elem_id - 1]

            if first_elem < x:
                # case 1.1 / 1.2 / 1.3 / 1.4

                # just go ahead
                if (prev_elem < x and curr_elem < x) or (prev_elem == x and curr_elem == x) or (prev_elem > x and curr_elem > x):
                    curr_elem_id += 1
                    continue

                # found equals after less
                if prev_elem < x and curr_elem == x:
                    begin_equals_id = curr_elem_id
                    curr_elem_id += 1
                    continue

                # found greater after equals / less
                if (prev_elem == x and curr_elem > x) or (prev_elem < x and curr_elem > x):
                    begin_greater_id = curr_elem_id
                    curr_elem_id += 1
                    continue

                # -----------------------

                # case 1.1
                if prev_elem > x and first_elem < x and curr_elem < x and begin_equals_id != -1 and begin_greater_id != -1:
                    equals_elem = arr[begin_equals_id]
                    greater_elem = arr[begin_greater_id]

                    arr[begin_equals_id] = curr_elem
                    arr[begin_greater_id] = equals_elem
                    arr[curr_elem_id] = greater_elem

                    begin_equals_id += 1
                    begin_greater_id += 1
                    curr_elem_id += 1
                    continue

                # case 1.2
                if prev_elem > x and first_elem < x and curr_elem == x and begin_greater_id != -1:

                    arr[begin_greater_id], arr[curr_elem_id] = arr[curr_elem_id], arr[begin_greater_id]
                    
                    if begin_equals_id == -1:
                        begin_equals_id = begin_greater_id


                    begin_greater_id += 1
                    curr_elem_id += 1
                    continue

                # case 1.3
                if prev_elem > x and first_elem < x and curr_elem < x and begin_greater_id != -1 and begin_equals_id == -1:

                    arr[begin_greater_id], arr[curr_elem_id] = arr[curr_elem_id], arr[begin_greater_id]
                    
                    begin_greater_id += 1
                    curr_elem_id += 1
                    continue

                # case 1.4
                if prev_elem > x and first_elem < x and curr_elem == x and begin_greater_id != -1:

                    arr[begin_greater_id], arr[curr_elem_id] = arr[curr_elem_id], arr[begin_greater_id]
                    
                    if begin_equals_id == -1:
                        begin_equals_id = begin_greater_id


                    begin_greater_id += 1
                    curr_elem_id += 1
                    continue

                # case 1.5
                if prev_elem == x and first_elem < x and curr_elem < x and begin_equals_id != -1:

                    arr[begin_equals_id], arr[curr_elem_id] = arr[curr_elem_id], arr[begin_equals_id]
                    
                    if begin_greater_id == -1:
                        begin_greater_id = begin_equals_id

                    begin_equals_id += 1
                    curr_elem_id += 1
                    continue

            elif first_elem == x:
                # case 2.1 / 2.2 / 2.3
                
                # тк если потом первый элемент будет != сепаратору, то эта строчка не выполнится
                begin_equals_id = 0

                # just go ahead
                if (prev_elem == x and curr_elem == x) or (prev_elem > x and curr_elem > x):
                    curr_elem_id += 1
                    continue

                # found greater after equals 
                if (prev_elem == x and curr_elem > x):
                    begin_greater_id = curr_elem_id
                    curr_elem_id += 1
                    continue
                # -----------------------

                # case 2.1
                if prev_elem > x and curr_elem < x and begin_greater_id != -1 and begin_equals_id != -1:
                    equals_elem = arr[begin_equals_id]
                    greater_elem = arr[begin_greater_id]

                    arr[begin_equals_id] = curr_elem
                    arr[curr_elem_id] = greater_elem
                    arr[begin_greater_id] = equals_elem

                    begin_greater_id += 1
                    begin_equals_id += 1
                    curr_elem_id += 1
                    continue
                    
                # case 2.2
                if prev_elem > x and curr_elem == x and begin_greater_id != -1:

                    arr[curr_elem_id], arr[begin_greater_id] = arr[begin_greater_id], arr[curr_elem_id]

                    begin_greater_id += 1
                    curr_elem_id += 1
                    continue
                    
                # case 2.3
                if prev_elem == x and curr_elem < x and begin_equals_id != -1:

                    arr[curr_elem_id], arr[begin_equals_id] = arr[begin_equals_id], arr[curr_elem_id]

                    if begin_greater_id == -1:
                        begin_greater_id = begin_equals_id

                    begin_equals_id += 1
                    curr_elem_id += 1
                    continue
                    

            else:
                # case 3.1 / 3.2
                
                # тк если потом первый элемент будет != сепаратору, то эта строчка не выполнится
                begin_greater_id = 0

                # just go ahead
                if (prev_elem > x and curr_elem > x):
                    curr_elem_id += 1
                    continue
                # -----------------------

                # case 3.1 and 3.2
                if (prev_elem > x and curr_elem == x and begin_greater_id != -1) \
                    or (prev_elem > x and curr_elem < x and begin_greater_id != -1):

                    arr[curr_elem_id], arr[begin_greater_id] = arr[begin_greater_id], arr[curr_elem_id]


                    if begin_equals_id == -1 and curr_elem == x:
                        begin_equals_id = begin_greater_id


                    begin_greater_id += 1
                    curr_elem_id += 1
                    continue
        
        if begin_equals_id != -1 and begin_greater_id != -1:
            return begin_equals_id, len(arr) - begin_equals_id

        elif begin_equals_id != -1:
            return begin_equals_id, len(arr) - begin_equals_id

        elif begin_greater_id != -1:
            return begin_greater_id, len(arr) - begin_greater_id

        else:
            # all nums are less than x
            return len(arr), 0

    else:
        if arr[0] < x:
            return  1,0
        else:
            return 0,1

less, others = 0,0

if arr:
    less, others = make_partition(x, arr, 0, 3)

print(less)
print(others)
