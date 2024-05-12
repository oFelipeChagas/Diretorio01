# helo, that's my first python challange.
# You may find all initial chalanges at bit.ly/PPZPythonExercicios
# 1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números

x = int(input("Digite um número: "))
y = int(input("Digite mais um número: "))
print(x + y)

# 2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

x = int(input("Metros: "))
print(x * 1000)

# 3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos
k = int(input("Digite os dias: "))
x = int(input("Digite as horas: "))
y = int(input("Digite os minutos: "))
z = int(input("Digite os segundos: "))
print(f"Em segundos: {x*24*60*60+x*60*60+y*60+z}")

# 4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('Salário atual: '))
aumento = float(input('Porcentagem do aumento: '))
aumento = aumento/100
print (f'Seu novo salário é R${salario*aumento}')

#5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

atual = float(input('Valor atual: '))
desconto = float(input('Porcentagem de desconto: '))
print (f'O valor com desconto é R${atual*desconto/100}')

#6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

dist = float(input('Distância a percorrer: '))
vel = float(input('Qual a velocidade média esperada: '))
print (f'O tempo estimado da viagem é de: {dist/vel} horas')

#7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

temp = float(input('Temperatura em Celsius: '))
print (f'Em Fahrenheit: {9*temp/5 + 32}°F')

#8) Faça agora o contrário, de Fahrenheit para Celsius.

f = float(input('Fahrenheit:'))
print (f'Celsius: {(f – 32) / 1,8}°C')

#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo 
#usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input('Quilômetros percorridos: '))
dias = int(input('Dias alugados: '))
print = (f'Você deve R$ {dias*60 + km*0,15}')

#10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a 
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante 
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o 
#total de dias.

por_dia = int(input('Quantos cigarros você fuma por dia: '))
anos = int(input('Há quantos anos você é tabagista: '))
vida = por_dia * 365 * anos
vida = vida / (6*24)
print (f'Você já fumou {vida} dias de sua vida')

#11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão
import math
print (str(2**1000000))
