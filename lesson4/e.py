from itertools import product


class SoftBracketsFSM:
    def __init__(self) -> None:
        self.curr_state = None
        self.num_brackets = 0
    
    def update_state(self, sym: str):
        if self.curr_state == None:
            if sym == '(':
                self.curr_state = '('
                return 1
            
        elif self.curr_state == '(':
            if sym == '(':
                self.num_brackets += 1
                return 1
            
            elif sym == ')':
                self.curr_state = ')'
                if not self.num_brackets:
                    self.curr_state = None

                return 1

        elif self.curr_state == ')':
            if sym == ')':
                self.num_brackets -= 1
            
                if not self.num_brackets:
                    self.curr_state = None
                
                return 1
            

class HardBracketsFSM:
    def __init__(self) -> None:
        self.curr_state = None
        self.num_brackets = 0

    
    def update_state(self, sym: str):
        if self.curr_state == None:
            if sym == '[':
                self.curr_state = '['
                return 1
            
        elif self.curr_state == '[':
            if sym == '[':
                self.num_brackets += 1
                return 1
            
            elif sym == ']':
                self.curr_state = ']'
                if not self.num_brackets:
                    self.curr_state = None
    
                return 1

        elif self.curr_state == ']':
            if sym == ']':
                self.num_brackets -= 1
            
                if not self.num_brackets:
                    self.curr_state = None
                
                return 1


n = int(input())


if n % 2 ==0 and n > 0:

    all_permuts = []
    success_permuts = set()

    commas = {1: '(', 2:'[', 3:')', 4:']'}
    commas_rev = {'(': 1, '[':2, ')':3, ']':4}

    # for begin_comma_id in range(1,2+1):
    #     for end_comma_id in range(3, 4+1):
    products = product(['(', '[', ']', ')'], repeat=n)
    for perm in products:
        # cur_perm = commas[begin_comma_id] + ''.join(perm) + commas[end_comma_id]
        
        all_permuts.append(perm)


    def permut_checker(curr_permut: list, sym_id: int=0, main_cycle: bool=True):
        curr_sym = curr_permut[sym_id]
        if curr_sym == '(':
            soft_bracks_fsm = SoftBracketsFSM()
            soft_bracks_fsm.update_state('(')

            sym_id += 1

            while sym_id < len(curr_permut):
                next_sym = curr_permut[sym_id]
                if next_sym == '[':
                    r = permut_checker(curr_permut, sym_id, False)
                    if not r:
                        return False
                    else:
                        sym_id = r

                else:
                    next_res = soft_bracks_fsm.update_state(curr_permut[sym_id])
                    if not next_res:
                        return False
                
                if soft_bracks_fsm.curr_state == None and not main_cycle:
                    return sym_id
                
                sym_id += 1

            if soft_bracks_fsm.curr_state == None:
                return True
            else:
                return False
            
        if curr_sym == '[':
            hard_bracks_fsm = HardBracketsFSM()
            hard_bracks_fsm.update_state('[')

            sym_id += 1

            while sym_id < len(curr_permut):
                next_sym = curr_permut[sym_id]
                if next_sym == '(':
                    r = permut_checker(curr_permut, sym_id, False)
                    if not r:
                        return False
                    else:
                        sym_id = r


                else:
                    next_res = hard_bracks_fsm.update_state(curr_permut[sym_id])
                    if not next_res:
                        return False
                

                if hard_bracks_fsm.curr_state == None and not main_cycle:
                    return sym_id

                sym_id += 1

            if hard_bracks_fsm.curr_state == None:
                return True
            else:
                return False


    for perm in all_permuts:
        if permut_checker(perm):
            r = tuple([commas_rev[x] for x in perm])
            success_permuts.add(r)



    for p in sorted(success_permuts):
        restore = ''
        for s in p:
            restore += commas[s]
        
        print(restore)
