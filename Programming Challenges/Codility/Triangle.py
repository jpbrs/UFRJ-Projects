# An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:
#
# A[P] + A[Q] > A[R],
# A[Q] + A[R] > A[P],
# A[R] + A[P] > A[Q].
# For example, consider array A such that:
#
#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 20
# Triplet (0, 2, 4) is triangular.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.
#
# For example, given array A such that:
#
#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 20
# the function should return 1, as explained above. Given array A such that:
#
#   A[0] = 10    A[1] = 50    A[2] = 5
#   A[3] = 1
# the function should return 0.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
def solution(A):
    N = len(A)
    A.sort() #O(N)*log(N)

    # If A length is lesser than 3 A can't be triangular
    if N < 3:
        return 0

    # Since Array is sorted, only have to look for each element once
    for k in range(N - 2):
        new_array = [A[k], A[k + 1], A[k + 2]]
        maximo = A[k+2]
        soma = sum(new_array)
        if maximo < (soma-maximo) :
            return 1

    return 0
print(solution([10,2,5,1,8,20]))

#COMO o array esta ordenado, como um triangulo so eh triangulo se seu maior lado for menor que a soma dos outros dois
#caso o teste de triangulo falhe, ao passarmos para o proximo item da lista, se A[k+1]+A[k]<A[K+2] entao tambem sera menor que A[k+3]
#portanto so eh logico comparar com o proximo item na lista com os dois anteriores.


