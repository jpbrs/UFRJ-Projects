# A non-empty array A consisting of N integers is given.
#
# The leader of this array is the value that occurs in more than half of the elements of A.
#
# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.
#
# For example, given array A such that:
#
#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# we can find two equi leaders:
#
# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count the number of equi leaders.
#
# Write a function:
#
# def solution(A)
#
# that, given a non-empty array A consisting of N integers, returns the number of equi leaders.
#
# For example, given:
#
#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# the function should return 2, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

#from collections import defaultdict


# def solution(A):
#     # write your code in Python 3.6
#     marker_l = defaultdict(lambda: 0)
#     marker_r = defaultdict(lambda: 0)
#
#     for i in range(len(A)):
#         marker_r[A[i]] += 1 #Dicionario com todas as ocorrencias de um index ate o final
#
#
#     n_equi_leader = 0
#     leader = A[0]
#     for i in range(len(A)):
#         marker_r[A[i]] -= 1
#         marker_l[A[i]] += 1
#
#         if i == 0 or marker_l[leader] < marker_l[A[i]]: #Confere se o novo candidato a lider possui mais ocorrencias que o ultimo lider da primeira metade
#             leader = A[i]
#
#         if (i + 1) // 2 < marker_l[leader] and (len(A) - (i + 1)) // 2 < marker_r[leader]: #confere se o novo lider tem mais de metade das ocorrencias tanto na prmeira metade quanto na segunda
#             n_equi_leader += 1
#
#     return n_equi_leader

from collections import defaultdict #Because defaultdict has not the KeyError exception if used with lambda : 0

def solution(A : bytearray):
    first_half = defaultdict(lambda : 0) #lambda : 0 para caso da KeyError exception, assim sera criado o elemento ao inves de de dar excecao
    second_half = defaultdict(lambda : 0)
    size = len(A)
    equi_leader_count = 0
    leader = None

    for element in A:
        second_half[element]+=1

    for i in range(0,size-1):
        first_half[A[i]]+=1
        second_half[A[i]]-=1
        if(i+1)//2<first_half[A[i]]: # Confere se o novo elemento eh o novo lider, precisa ter mais que a metade
            leader = A[i]  # Se for o leader salva, se nao for o lider vai ser o lider que era anteriormente, o que nao necessariamente eh verdade, precisa checar novamente se eh leader
        elif first_half[leader]>((i+1)//2): #Ve se o antigo lider ainda eh o lider
            #leader = leader
            pass
        else:
            leader = None

        if (size-(i+1))//2<second_half[leader]: #Confere se existem lideres os lideres sao iguais
            equi_leader_count += 1
    return equi_leader_count


print(solution([4,3,4,4,4,2]))



