n = int(input())
studs_data = list(map(int, input().split()))


if n:
    prev_starosta_count = 0
    for other_student_id in range(1, len(studs_data)):
        prev_starosta_count += abs(studs_data[other_student_id] - studs_data[0])

    print(prev_starosta_count, end=' ')


    for starosta_id in range(1,len(studs_data) - 1):
        diff = studs_data[starosta_id] - studs_data[starosta_id-1]
        n_plus = len(studs_data) - starosta_id - 1
        n_minus = starosta_id - 1
        prev_starosta_count = prev_starosta_count + diff * n_minus - diff * n_plus
        print(prev_starosta_count, end=' ')

    starosta_id = len(studs_data) - 1
    diff = studs_data[starosta_id] - studs_data[starosta_id-1]
    n_plus = len(studs_data) - starosta_id - 1
    n_minus = starosta_id - 1
    prev_starosta_count = prev_starosta_count + diff * n_minus - diff * n_plus
    print(prev_starosta_count)