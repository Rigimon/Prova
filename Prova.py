#Exercicio 5
prod = float(input("Digite o preço do produto:"))
print ("Preço com desconto",prod-(prod*0.05))

#Exercicio 6
n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))
if n1 > n2:
    print (n1,"é o maior número")
elif n2 > n1:
    print (n2,"é o maior número")
else:
    print ("Os números são iguais")

#Exercicio 7
cont = 1000
while cont > 99:
    if cont%2 == 0 or cont%3 == 0:
        print (cont)
    cont = cont - 1

#Exercicio 9
fem = 0
masc = 0
chocofem = 0
chocomasc = 0
for i in range (0,10):
    print ("qual seu sexo?")
    print()
    print ("(1) Masculino")
    print ("(2) Feminino")
    sex = int(input())
    if sex == 1:
        fem = fem + 1
        print ("Voce gosta de chocolate?")
        print ()
        print ("(1) Sim")
        print ("(2) Não")
        resp = int(input())
        if resp == 1:
            chocofem = chocofem + 1
    if sex == 2:
        masc = masc + 1
        print ("Voce gosta de chocolate?")
        print ()
        print ("(1) Sim")
        print ("(2) Não")
        resp = int(input())
        if resp == 1:
            chocomasc = chocomasc + 1
gost = (chocomasc + chocofem)*10
print (gost,"% gosta de chocolate")
print (chocomasc*10,"% são homens")
print (chocofem*10,"% são mulheres")

#Exercicio 10
cont = 1
maior = 0
menor = int(input("Digite um número:"))
while cont < 3:
    num = int(input("Digite um número:"))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont = cont + 1
print ("Maior:",maior)
print ("Menor:",menor)
