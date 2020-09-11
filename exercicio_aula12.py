#Faça um programa que receba um número. Após isso, ele deve pedir ao usuário a quantidade solicitada de números. Ao fim, ele deve exibir a média de todos os números informados.

qtd_num = float(input('Digite a quantidade desejada: '))
valores = []
cont = 1

while len(valores) != qtd_num:
    valores.append(float(input('Digite o valor {}: '.format(cont))))
    cont +=1

media = sum(valores)/qtd_num

print('A média de todos os números informados é {}'.format(media))

