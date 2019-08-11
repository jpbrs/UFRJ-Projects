# A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).
#
# For example, array A such that:
#
#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# contains the following example slices:
#
# slice (1, 2), whose average is (2 + 2) / 2 = 2;
# slice (3, 4), whose average is (5 + 1) / 2 = 3;
# slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
# The goal is to find the starting position of a slice whose average is minimal.
#
# Write a function:
#
# def solution(A)
#
# that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.
#
# For example, given array A such that:
#
#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# the function should return 1, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000].

# Um slice sempre sera menor quando estiver em um tamanho de dois ou tres. Pois caso apareca um numero menor que a primeira posicao o slice
#pode ser trocado pelas duas ultimas e caso a media das 3 ultimas seja menor que das duas primeiras tambem pode ser trocado
# caso apareca algum outro numero que torne a media menor, consequentemente a media desse numero somado ao penultimo sera menor ou igual a media anterior

# dado um array [n,m,r,s]
# mean(n+m) > mean(n+m+r) > mean(n+m+r+s) , logo 6n + 6m > 4n + 4m + 4r > 3n + 3m + 3r + 3s
#Entao 6n + 6m > 3n + 3m + 3r + 3s
# logo 3n + 3n > 3r + 3s -> n + m > r + s, entao se r + s < n + m , entao r + s < n + m + r + s

def solution(A : bytearray):
    min_idex = 0
    min_value = float("inf")

    for i in range(0, len(A) - 1):
        if (A[i] + A[i + 1]) / 2.0 < min_value:
            min_index = i
            min_value = (A[i] + A[i + 1]) / 2.0
        if i < len(A) - 2 and (A[i] + A[i + 1] + A[i + 2]) / 3.0 < min_value:
            min_index = i
            min_value = (A[i] + A[i + 1] + A[i + 2]) / 3.0

    return min_index

print(solution([4,2,2,5,1,5,8]))