
from typing import List


# restricted rows/cols ids

# n = int(input())
n = 8

allowed_rows = set()
allowed_cols = set()
allowed_top_right_down_left_diags = set()
allowed_top_left_down_right_diags = set()

for c in range(n):
    allowed_cols.add(c)

for r in range(n):
    allowed_rows.add(r)

for top_right_down_left_diag in range(0, (n-1)*2+1):
    allowed_top_right_down_left_diags.add(top_right_down_left_diag)

for top_left_down_right_diag in range(-(n-1), (n-1)+1):
    allowed_top_left_down_right_diags.add(top_left_down_right_diag)


f = open('output.txt', 'w')


# def get_possible_permuts_rec( allowed_rows: set, allowed_cols: set, allowed_top_right_down_left_diags: set, allowed_top_left_down_right_diags:set, n_of_bishops: int, count: int=0):
#     if n_of_bishops:
#         if allowed_rows and allowed_cols and allowed_top_right_down_left_diags and allowed_top_left_down_right_diags:
#             allowed_rows_id = 0
#             while allowed_rows_id < len(allowed_rows):
#                 allowed_rows_id += 1
#                 row = allowed_rows.pop()
                
#                 allowed_cols_cp = allowed_cols.copy()
#                 allowed_cols_cp_id = 0
#                 while allowed_cols_cp_id < len(allowed_cols_cp):
#                     allowed_cols_cp_id += 1

#                     col = allowed_cols_cp.pop()

#                     top_right_down_left_diag_id = row + col
#                     top_left_down_right_diag_id = row - col


#                     if top_right_down_left_diag_id in allowed_top_right_down_left_diags and top_left_down_right_diag_id in allowed_top_left_down_right_diags:
                        
#                         allowed_top_right_down_left_diags_cp = allowed_top_right_down_left_diags.copy()
#                         allowed_top_left_down_right_diags_cp = allowed_top_left_down_right_diags.copy()

#                         allowed_top_right_down_left_diags_cp.remove(top_right_down_left_diag_id)
#                         allowed_top_left_down_right_diags_cp.remove(top_left_down_right_diag_id)
                        
#                         # f.write(str(str(row) + ' ' + str( col) + '\n'))

                        
#                         count = get_possible_permuts_rec( allowed_rows.copy(), allowed_cols_cp.copy(), allowed_top_right_down_left_diags_cp, allowed_top_left_down_right_diags_cp, n_of_bishops-1, count)

                
#                     allowed_cols_cp.add(col)

#                 allowed_rows.add(row)

#     else:
#         return count + 1

#     return count


def get_possible_permuts_rec( allowed_rows: set, allowed_cols: set, allowed_top_right_down_left_diags: set, allowed_top_left_down_right_diags:set, n_of_bishops: int, count: int=0, curr_answer: set = set(), all_answer_points: set=set()):
    if n_of_bishops:
        for row in allowed_rows:
            for col in allowed_cols:

                top_right_down_left_diag_id = row + col
                top_left_down_right_diag_id = row - col


                if top_right_down_left_diag_id in allowed_top_right_down_left_diags and top_left_down_right_diag_id in allowed_top_left_down_right_diags:
                    allowed_rows_cp = allowed_rows.copy()
                    allowed_cols_cp = allowed_cols.copy()

                    allowed_rows_cp.remove(row)
                    allowed_cols_cp.remove(col)


                    allowed_top_right_down_left_diags_cp = allowed_top_right_down_left_diags.copy()
                    allowed_top_left_down_right_diags_cp = allowed_top_left_down_right_diags.copy()

                    allowed_top_right_down_left_diags_cp.remove(top_right_down_left_diag_id)
                    allowed_top_left_down_right_diags_cp.remove(top_left_down_right_diag_id)

                    curr_answer.add((row, col))
                    count = get_possible_permuts_rec( allowed_rows_cp, allowed_cols_cp, allowed_top_right_down_left_diags_cp, allowed_top_left_down_right_diags_cp, n_of_bishops-1, count, curr_answer.copy(), all_answer_points)


    else:
        not_all_in_answer = False
        for point in curr_answer:
            row, col = point
            if (row, col) not in all_answer_points:
                not_all_in_answer = True


        if not_all_in_answer:
            for point in curr_answer:
                row, col = point
                all_answer_points.add((row, col))
    
            return count + 1

    return count
 




n_of_bishops = n
count = get_possible_permuts_rec(allowed_rows, allowed_cols, allowed_top_right_down_left_diags, allowed_top_left_down_right_diags, n_of_bishops)

print(count)
