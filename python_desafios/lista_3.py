# helo, that's my third python challange.
# You may find all initial chalanges at bit.ly/PPZPythonExercicios

# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
# seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    numero = int (input ('Digite a nota: '))
    if numero >= 0 and numero <= 10:
        print ('Cadastraado com sucesso')
        break
    else:
        print ('Valor inválido, tente novamente!')

# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao 
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nome = str(input('Digine o nome de usuário: '))
    senha = str (input('Digite a senha: '))
    if nome != senha:
        print ('Cadastrado com sucesso')
        break
    else:
        print ('Use caracteres diferentes')

# 3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa 
# anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de 
# crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos 
# necessários para que a população do país A ultrapasse ou iguale a população do país B, 
# mantidas as taxas de crescimento

cid_a = 80000
cid_b = 200000
tx_a = 0.03
tx_b = 0.015
ano = 0

while cid_b >= cid_a:
    cid_a += cid_a * tx_a
    cid_b += cid_b * tx_b
    ano = ano + 1
print (ano)

# 4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de 
# formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a 
# soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número 
# de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a+b
        return b
    
n = int(input('Qual posição quer verificar? '))
resultado = fibonacci(n)
print (f'O {n}º Fibonacci é: {resultado}')

# 5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando 
# o algoritmo de Euclides.

def mdc(a, b):
    while True:
        if a%b == 0:
            print (f'O MDC de A e B é {b}')
            break
        else:
            a, b = b, a%b
        return b

a = int (input('Qual o maior numero? '))
b = int (input('Qual o menor numero? '))
resultado = mdc (a,b)
print (f'O MDC de  {a} e {b} é {resultado}')