# Write a function:
#
# def solution(A, B, K)
#
# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
#
# { i : A ≤ i ≤ B, i mod K = 0 }
#
# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
#
# Write an efficient algorithm for the following assumptions:
#
# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.

# Se N/M = R isso significa que existem R numeros diviseis por N
# Entre N e K existem X numeros diviseis por R sendo a diferenca das divisoes
# Porem, como estamos falando de um intervalo contendo o numero N e o numero K, temos que verificar se K%M = 0 para saber se incluiremos ou nao o numero

def solution(A, B, K):
    if not A%K:
        return B//K - A//K +1
    return B//K - A//K

print(solution(6,11,2))