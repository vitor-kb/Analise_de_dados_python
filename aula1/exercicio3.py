#3) Fazer um programa para ler o ome do aluno, ler 4 notas, ler faltas, calcular media e imprimir

#Forma utilizada na aula
nome = input("Digite o nome do aluno: ");

nota1 = float(input("Insira a 1ª nota: "));
nota2 = float(input("Insira a 2ª nota: "));
nota3 = float(input("Insira a 3ª nota: "));
nota4 = float(input("Insira a 4ª nota: "));

faltas = int(input('Digite a quantidade de faltas: '))

media = (nota1 + nota2 + nota3 + nota4)/4;

print('Nome do Aluno: ', nome);
print('Media do Aluno: ', media);
print('Faltas: ', faltas);

if media >= 7 and faltas <= 5:
    print('Aprovado!');
elif media >= 7 and faltas > 5:
    print('Reprovado por faltas!');
elif media < 7 and faltas <= 5:
    print('Reprovado por media');
else:
    print('Reprovado por Media e por faltas');

    
#Forma utilizando laço de repetição
média = 0
# O "for" é um laço de repetição com contador de repetições
for contador in range(1, 5, 1):
	nota = float(input(f"Insira a {contador}ª nota do aluno: "))
	média = média + nota
média = média / 4

faltas = int(input("Insira quantas faltas o aluno possui: "))

if média >= 7 and faltas <= 5:
	print("Aprovado por tudo!")
elif média >= 7 and faltas > 5:
	print("Aprovado por nota, mas reprovado pela frequência.")
elif média < 7 and faltas <= 5:
	print("Aprovado por frequência, mas reprovado por nota.")
else:
	print("Reprovado por tudo!")
