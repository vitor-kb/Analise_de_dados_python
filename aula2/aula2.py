#estruturas condicionais
a=10;
b=10;
c=11;
if a>b:
    print('b é maior que a');
elif b == a:
    print('a e b são iguais');
else:
    print('b é menor que a');

#estruturas condicionais²
var1 = 18;
var2 = 2;
var3 = "Maria";
var4 = 4;

if var2 > var1:
    print("var1 é maior que var 2");
elif var2 == 500:
    print("var2 vale 500");
elif var3 == var2:
    print("var3 e var2 são iguais");
elif var4 is str("4"):
    print("var4 não é do tipo string");
else:
    print("Nenhuma condição é verdadeira!");


#estruturas de repetição
#for é utilizado em situações que precisamos trabalhar uma estrutura de repetição
for x in range(0, 6):
    print(x);

nomes = ["Maria", "Joao", "Pedro", "Leticia"];
for n in nomes:
    print(n);
    

#while, é executado enquanto em sua instrução houver uma condição verdadeira
x = 1
while x < 6:
    print(x);
    x += 1;
    
#quebra de loop
x = 1;
while x < 10:
    print(x);
    x += 1;
    if x == 4: # <- se essa parte for removida, todos os números entre 1 e 10 serão impressos
        break;
    

#strings
#convertendo o conteudo para maiusculo
mensagem = "Linguagem de Programacao I - Python";
print(mensagem.upper()); # passa o texto para maiúscula

mensagem = "LINGUAGEM DE PROGRAMACAO I - PYTHON";
print(mensagem.lower()); # passa o texto para minúscula

mensagem = "hoje vai fazer calor";
print("hoje" in mensagem); #acha uma palavra especifica dentro da variavel

mensagem = "Ontem choveu e hoje esta fazendo sol";
print(mensagem.split());

mensagem = "1,4,5,67,78,9";
print(mensagem.split(",")); #carcater em referencia