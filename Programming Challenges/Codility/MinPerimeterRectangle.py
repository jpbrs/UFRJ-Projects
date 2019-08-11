# An integer N is given, representing the area of some rectangle.
# #
# # The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).
# #
# # The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.
# #
# # For example, given integer N = 30, rectangles of area 30 are:
# #
# # (1, 30), with a perimeter of 62,
# # (2, 15), with a perimeter of 34,
# # (3, 10), with a perimeter of 26,
# # (5, 6), with a perimeter of 22.
# # Write a function:
# #
# # def solution(N)
# #
# # that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.
# #
# # For example, given an integer N = 30, the function should return 22, as explained above.
# #
# # Write an efficient algorithm for the following assumptions:
# #
# # N is an integer within the range [1..1,000,000,000].

def solution(N : int):
    min_perimeter = (1,N)
    i = 2
    while i*i < N:
        if N % i == 0:
            min_perimeter = (i, N/i)
        i += 1

    if i*i == N:
        min_perimeter = (i,i)

    return(int(min_perimeter[0]*2+min_perimeter[1]*2))

print(solution(100))