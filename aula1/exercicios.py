#1) Fazer um programa para ler o nome do aluno, ler 4 notas e calcular a média e imprimir

nome = input("Digite o nome do aluno: ");

nota1 = float(input("Insira a 1ª nota: "));
nota2 = float(input("Insira a 2ª nota: "));
nota3 = float(input("Insira a 3ª nota: "));
nota4 = float(input("Insira a 4ª nota: "));

média = (nota1 + nota2 + nota3 + nota4)/4;

print(f"A média deste aluno é {média}");


