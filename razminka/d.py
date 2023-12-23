word_a = input()
word_b = input()

word_a_container = {}
for l in word_a:
    if not l in word_a_container: 
        word_a_container[l] = 0
    word_a_container[l] += 1


fault = False
for l in word_b:
    if not l in word_a_container: 
        fault = True
        break
    else:
        word_a_container[l] -= 1


if not fault:
    for l in word_a_container:
        if word_a_container[l]:
            fault = True
    
    if not fault:
        print('YES')
    else:
        print('NO')
    
else:
    print('NO')
