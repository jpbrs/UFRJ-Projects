a = 4
b = 3

a = a ^ b
b = a ^ b
a = a ^ b

print(a,b)

#Ao inves de criar outra variavel para fazer o swap de variaveis o operador xor consegue fazer o swap
#ex : 3 = 011 e 4 = 100
#a = 011 xor 100 = 111
#b = 111 xor 100 = 011
#a = 111 xor 011 = 100
#A troca de variaveis eh possivel utilizando 3 xors