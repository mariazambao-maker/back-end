Estrutura de repetição While
Esta estrutura é utilizada para quando não sabemos o número de repetições devem ser executadas. 
Nessa estrutura repetimos o laço enquanto uma condição é atendida, quando a condição imposta não é mais atendida o laço para. 
A sintaxe desse laço é a seguinte: while + condição:. Dentro da estrutura while podemos utilizar diferentes condicionais para que o código siga caminhos diferentes ao longo de sua execução.
 exemplo 1
c = 1
while c < 10:
    print(c)
    c += 1
print('fim')
 exemplo 2
n = 1
while n != 0:
    n =int(input('digite um valor'))
print("fim")

