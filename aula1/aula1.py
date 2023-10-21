#variáveis que podemos utilizar, qualquer caracter é possível, menos caracter especial, o único caracter especial que pode ser utilizado é o "_"
a = 10;
b = 20;
c = a + b;

print(c);

# 1 numero inteiro (int)
# 1.2 numero real (float) ou numero fracionado
# "1" é um texto (string)
# 0 ou 1 variavel booleana (bool)
# python é case sensitive, ou seja, ele faz diferenciação de letras maiúsculas e minúsculas
# exemplo: numero01 = 1, Numero01 = 1

#pegar entrada do teclado do usuário
teclado = input('Digite um numero inteiro: ');
#definimos que é um número inteiro
numero01 = int(teclado);
#pegar outra entrada do usuário
teclado = input('Digite outro numero inteiro: ');
numero02 = int(teclado);
print('A soma dos dois numeros e: ', numero01 + numero02);

#mesmo código como acima, só que mais curto
a = int(input('Digite o valor de A e tecle enter'));
b = int(input('Digite o valor de B e tecle enter'));
c = a+b;
print('A soma é: ', c);

#Operadores aritméticos

# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# % Resto inteiro da divisão

