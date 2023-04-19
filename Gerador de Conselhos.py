import random

import time

def argumento():

    while True:
        try:
            entrada = input("Digite um número inteiro: ")
            if len(entrada) == 0:
                raise ValueError("Entrada Vazia")
            quantidade = int(entrada)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido.")

    conselho_aleatorios = ["As montanhas da vida não existem apenas para que você chegue no topo, mas para que você aprenda o valor da escalada." ,
        "A vida pode até te derrubar, mas é você quem escolhe a hora de se levantar." ,
        "É melhor ser verdadeiro e solitário do que viver em falsidade e estar sempre acompanhado." ,
        "Na minha vida até agora, descobri que na verdade só há dois tipos de pessoas: aqueles que estão com você, e aqueles que estão contra você. Aprenda a reconhecê-los, pois eles são frequentemente e facilmente confundidos um com o outro." ,
        "Ser feliz não é ter uma vida perfeita, mas sim reconhecer que vale a pena viver apesar de todos os desafios e perdas." ,
        "Aprendi que não devo me importar com comentários que não vão mudar minha vida." ,
        "A vida tem sons, que pra gente ouvir precisa aprender a começar de novo. É como tocar o mesmo violão e nele compor uma nova canção." ,
        "Na vida irás encontrar três tipos de pessoas: aquelas que irão mudar a tua vida, aquelas que irão prejudicar a tua vida, aquelas que serão a tua vida." ,
        "A vida é basicamente uma montanha russa. Tem seus altos e baixos, e o mais importante: você tem que fazer o ingresso valer a pena." ,
        "O mundo está nas mãos daqueles que têm a coragem de sonhar e de correr o risco de viver seus sonhos." ,
        "Deus sabe quem colocar na sua vida, da mesma forma que sabe quem tirar." ,
        "Não viva para que sua presença seja notada, mas para que sua falta seja sentida." ,
        "Um novo dia é uma página em branco na sua vida. Escreva apenas o que vale a pena. Bom dia!" ,
        "Passamos a vida procurando em pessoas o que só podemos encontrar em Deus." ,
        "...bom mesmo é ir à luta com determinação, abraçar a vida com paixão, perder com classe e vencer com ousadia, porque o mundo pertence a quem se atreve e a vida é muito pra ser insignificante."]
        
    if quantidade == 0:
        print("Você digitou Zero!, por isso nenhum conselho foi gerado.")
     
    while quantidade == 1:
        conselho1 = random.choice(conselho_aleatorios)
        print()
        print(conselho1)
        print()
        break
        
    while quantidade == 2:
        conselho1 = random.choice(conselho_aleatorios)
        conselho2 = random.choice(conselho_aleatorios)
        print()
        print(conselho1)
        print()
        print(conselho2)
        print()
        break
        
    while quantidade == 3:
        conselho1 = random.choice(conselho_aleatorios)
        conselho2 = random.choice(conselho_aleatorios)
        conselho3 = random.choice(conselho_aleatorios)
        print()
        print(conselho1)
        print()
        print(conselho2)
        print()
        print(conselho3)
        break
        
    while quantidade == 4:
        conselho1 = random.choice(conselho_aleatorios)
        conselho2 = random.choice(conselho_aleatorios)
        conselho3 = random.choice(conselho_aleatorios)
        conselho4 = random.choice(conselho_aleatorios)
        print()
        print(conselho1)
        print()
        print(conselho2)
        print()
        print(conselho3)
        print()
        print(conselho4)
        break
        
    while quantidade == 5:
        conselho1 = random.choice(conselho_aleatorios)
        conselho2 = random.choice(conselho_aleatorios)
        conselho3 = random.choice(conselho_aleatorios)
        conselho4 = random.choice(conselho_aleatorios)
        conselho5 = random.choice(conselho_aleatorios)
        print()
        print(conselho1)
        print()
        print(conselho2)
        print()
        print(conselho3)
        print()
        print(conselho4)
        print()
        print(conselho5)
        break
        
    while quantidade == 6:
        conselho1 = random.choice(conselho_aleatorios)
        conselho2 = random.choice(conselho_aleatorios)
        conselho3 = random.choice(conselho_aleatorios)
        conselho4 = random.choice(conselho_aleatorios)
        conselho5 = random.choice(conselho_aleatorios)
        conselho6 = random.choice(conselho_aleatorios)
        print()
        print(conselho1)
        print()
        print(conselho2)
        print()
        print(conselho3)
        print()
        print(conselho4)
        print()
        print(conselho5)
        print()
        print(conselho6)
        break
        
    while quantidade == 7:
        conselho1 = random.choice(conselho_aleatorios)
        conselho2 = random.choice(conselho_aleatorios)
        conselho3 = random.choice(conselho_aleatorios)
        conselho4 = random.choice(conselho_aleatorios)
        conselho5 = random.choice(conselho_aleatorios)
        conselho6 = random.choice(conselho_aleatorios)
        conselho7 = random.choice(conselho_aleatorios)
        print()
        print(conselho1)
        print()
        print(conselho2)
        print()
        print(conselho3)
        print()
        print(conselho4)
        print()
        print(conselho5)
        print()
        print(conselho6)
        print()
        print(conselho7)
        break
    
    while quantidade == 8:
        conselho1 = random.choice(conselho_aleatorios)
        conselho2 = random.choice(conselho_aleatorios)
        conselho3 = random.choice(conselho_aleatorios)
        conselho4 = random.choice(conselho_aleatorios)
        conselho5 = random.choice(conselho_aleatorios)
        conselho6 = random.choice(conselho_aleatorios)
        conselho7 = random.choice(conselho_aleatorios)
        conselho8 = random.choice(conselho_aleatorios)
        print()
        print(conselho1)
        print()
        print(conselho2)
        print()
        print(conselho3)
        print()
        print(conselho4)
        print()
        print(conselho5)
        print()
        print(conselho6)
        print()
        print(conselho7)
        print()
        print(conselho8)
        break
        
    while quantidade == 9:
        conselho1 = random.choice(conselho_aleatorios)
        conselho2 = random.choice(conselho_aleatorios)
        conselho3 = random.choice(conselho_aleatorios)
        conselho4 = random.choice(conselho_aleatorios)
        conselho5 = random.choice(conselho_aleatorios)
        conselho6 = random.choice(conselho_aleatorios)
        conselho7 = random.choice(conselho_aleatorios)
        conselho8 = random.choice(conselho_aleatorios)
        conselho9 = random.choice(conselho_aleatorios)
        print()
        print(conselho1)
        print()
        print(conselho2)
        print()
        print(conselho3)
        print()
        print(conselho4)
        print()
        print(conselho5)
        print()
        print(conselho6)
        print()
        print(conselho7)
        print()
        print(conselho8)
        print()
        print(conselho9)
        break
        
    while quantidade == 10:
        conselho1 = random.choice(conselho_aleatorios)
        conselho2 = random.choice(conselho_aleatorios)
        conselho3 = random.choice(conselho_aleatorios)
        conselho4 = random.choice(conselho_aleatorios)
        conselho5 = random.choice(conselho_aleatorios)
        conselho6 = random.choice(conselho_aleatorios)
        conselho7 = random.choice(conselho_aleatorios)
        conselho8 = random.choice(conselho_aleatorios)
        conselho9 = random.choice(conselho_aleatorios)
        conselho10 = random.choice(conselho_aleatorios)
        print()
        print(conselho1)
        print()
        print(conselho2)
        print()
        print(conselho3)
        print()
        print(conselho4)
        print()
        print(conselho5)
        print()
        print(conselho6)
        print()
        print(conselho7)
        print()
        print(conselho8)
        print()
        print(conselho9)
        print()
        print(conselho10)
        break
        
def menu():
    print("*" * 25)
    print("GERADOR DE CONSELHOS")
    print("*" * 25)
    print()
    time.sleep(1)
        
while True:

    menu()
    argumento()
