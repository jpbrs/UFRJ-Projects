def solution(N):

    s = str(bin(N)).strip("0b")

    bg = 0
    max_bg = 0
    for i in s:

        if i == "0":
            bg += 1
        if i == "1":
            if max_bg < bg:
                max_bg = bg
            bg = 0
    return max_bg

print(solution(32))

