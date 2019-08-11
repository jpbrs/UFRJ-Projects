# You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.
# #
# # The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.
# #
# # Write a function:
# #
# # def solution(H)
# #
# # that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.
# #
# # For example, given array H containing N = 9 integers:
# #
# #   H[0] = 8    H[1] = 8    H[2] = 5
# #   H[3] = 7    H[4] = 9    H[5] = 8
# #   H[6] = 7    H[7] = 4    H[8] = 8
# # the function should return 7. The figure shows one possible arrangement of seven blocks.
# #
# #
# #
# # Write an efficient algorithm for the following assumptions:
# #
# # N is an integer within the range [1..100,000];
# # each element of array H is an integer within the range [1..1,000,000,000].

# Funcao correta em 100% porem em O(n**2), tentarei fazer com O(n)
# def solution(A : bytearray):
#     base_stack = [0]
#     block_count = 0
#     last = 0
#     for floor in A:
#         if floor > last:
#             base_stack.append(floor)
#             block_count += 1
#         elif floor < last:
#             base_stack.pop()
#             trigger = False
#             for i in range(0,len(base_stack)):
#                 if base_stack[i] == floor:
#                     trigger = True
#                     base_stack = base_stack[0:i]
#                     if i != 0:
#                         base_stack.append(floor)
#                     break
#             if not trigger:
#                 base_stack.append(floor)
#                 block_count += 1
#
#         last = floor
#     return block_count

def solution(A : bytearray):
    block_count = 0

    base_stack = [0]

    for floor in A:
        #O segredo eh enquanto a pilha estiver maior que o teto remover tudo que ha para cima pois sera necessario criar novos blocos, nao precisa analisar individualmente
        while base_stack[-1] > floor:
            base_stack.pop()

        if base_stack[-1] != floor:
            block_count += 1
            base_stack.append(floor)

    return block_count
