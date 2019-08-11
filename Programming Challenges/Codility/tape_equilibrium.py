def solution(tape : bytearray):

    left_side = 0
    right_side = sum(tape)
    min_dif = float("inf")


    for i in tape[:-1]:
        left_side += i
        right_side -= i
        min_dif = min(abs(right_side-left_side), min_dif)

    return min_dif


print(solution([3,1,2,4,3]))
