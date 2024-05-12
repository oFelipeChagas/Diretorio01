# helo, that's my first python challange.
# You may find all initial chalanges at bit.ly/PPZPythonExercicios

#1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser 
#um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

a = int(input('Lado do triângulo: '))
b = int(input('Lado do triângulo: '))
c = int(input('Lado do triângulo: '))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print ('Equilátero')
    elif a==b or b==c or c == a:
        print ('Isóceles')
    else:
        print ('Escaleno')
else:
    print ('Isto não é um triângulo')
    print ('a soma dos lados menores é maior que o terceiro')

#2. Determine se um ano é bissexto.

ano = int(input('Digite o ano desejado: '))
if (ano%4 == 0 and ano%100 !=0) or ano%400 == 0:
	print ('Este ano é bissexto')
else:
	print ('Este ano não é bissexto')
 
#  3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de 
# seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do 
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você 
# faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na 
# variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais 
# variáveis com o conteúdo ZERO

peixe = float(input('Pescado (KG): '))
if peixe > 50:
    print (f'Multa de R${((peixe - 50)*4)}')
    print (f'Excede em: {(peixe-50)}KG')
else:
    print ("00,00")
    print ("0 KG")
    
#4. Faça um Programa que leia três números e mostre o maior deles

numero = input('Digite números com espaçamento simples: ')
entradas = numero.split()
entradas = [int(x) for x in entradas]
maior = max(entradas)
print (f'{maior} é o  número entre eles')

#5. Faça um Programa que leia três números e mostre o maior e o menor deles

numero = input('Digite números com espaçamento simples: ')
entradas = numero.split()
entradas = [int(x) for x in entradas]
maior = max(entradas)
menor = min(entradas)
print (f'{maior} é o maior número entre eles')
print (f'{menor} é o menor número entre eles')

# 6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule 
# e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, 
# quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os 
# descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato ( 5%) : R$
# e. = Salário Liquido : R$

hora = int(input('Quantas horas você trabalha por mês? '))
relacao = float(input('Quanto você ganha por hora em R$: '))
bruto = (hora*relacao)
IRRF = (bruto * 0.11)
INSS = (bruto * 0.08)
sindicato = (bruto * 0.05)
descontos = (IRRF + INSS + sindicato)

print (f'Salário bruto    +{bruto}')
print (f'IRRF             -{IRRF}')
print (f'INSS             -{INSS}')
print (f'Imposto sindical -{sindicato}')
print (f'Total de proventos R$ {bruto:.2f}')
print (f'Total de descontos R$ {descontos}')
print (f'Salário líquido R$ {bruto - descontos}')

# 7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem 
# compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas

import math
area = int (input('Qual a area a ser pintada em m²? '))
latas = area / 54
print (math.ceil(latas))