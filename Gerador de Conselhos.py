import time

import os

import  random

def argumento():
    quantidade = int(input("Digite a quantidade de palavras a serem sorteadas: "))
    conselho_aleatorios = ['Não viva somente do que faz sentido. Viva do que te faz feliz.', 
    'Livre-se dos bajuladores. Mantenha perto de você pessoas que te avisem quando você erra.',
    'Tente não julgar uma pessoa sem antes conhecer suas dores, sua vida e sua história.' ,
    'Não grite alto por sua felicidade, pois a inveja possui sono leve.' ,
    'Se você está andando no caminho certo e está disposto a continuar caminhando, eventualmente, você vai progredir.' ,
    'Quem tem mais do que precisa ter quase sempre se convence que não tem o bastante, e fala demais por não ter nada a dizer.' ,
    'Bobeira é não viver a realidade.', 
    'A verdade alivia mais do que machuca. E estará sempre acima de qualquer falsidade como o óleo sobre a água.',
    'Não diga as coisas com pressa. Mais vale um silêncio certo que uma palavra errada!' , 
    'Se não puder se destacar pelo talento, vença pelo esforço.' , 
    'Cuide da sua saúde: se estiver boa, preserve-a. Se estiver instável, melhore-a. Se estiver além do que você possa fazer, peça ajuda.' ,
    'Regra de ouro: não faça com os outros o que você não gostaria que fizessem com você.' ,
    'Aproveitar um bom conselho requer mais sabedoria do que dá-lo.' ,
    'A felicidade é um problema individual. Aqui, nenhum conselho é válido. Cada um deve procurar, por si, tornar-se feliz.' ,
    'Ouça o silêncio, esse é o melhor conselho.' ,
    'Você pode se lamentar muitas vezes por ter pronunciado uma palavra indelicada, mas nunca por ter pronunciado uma palavra bondosa.' ,
    'Pelos erros dos outros, o homem sensato corrige os seus.' ,
    'O essencial é invisível aos olhos. Só se vê bem com o coração.'
    'A vida é imprevisível, mas tentamos estar prontos da melhor forma possível. Confira, nesta categoria, frases que vão te preparar para todas as situações.' ,
    'Aprecie as coisas simples.' ,
    'O caminho mais fácil, nem sempre é o melhor.' ,
    'Lágrimas fazem parte. Suporte, queixe-se e vá adiante. As únicas pessoas que estão conosco a vida inteira somos nós mesmos. Mostre estar vivo enquanto estiver vivo.' ,
    'Nunca se esqueça daquilo que faz seus olhos brilharem.' ,
    'Livre-se de todos os números não-essenciais. Isto inclui idade, peso e altura. Deixe os médicos se preocupar com eles. É para isso que você os paga.' ,
    'Cerque-se daquilo que ama, seja família, animais de estimação, coleções, música, plantas, hobbies, seja o que for. Seu lar é seu refúgio.' ,
    'Se você ficar sozinho, pega a solidão e dança!' ,
    'Aquele que tem medo do novo, tem medo da vida, pois cada dia é um novo dia. Vivendo e aprendendo…' ,
    'Se você não pode ser o Sol, seja um planeta, mas nunca deixe de irradiar a luz que mora no seu coração.' ,
    'Faça algo que valha a pena ser recordado mais tarde.' ,
    'Ria sempre, em alto e bom som! Ria até perder o fôlego.' ,
    'É impossível agradar a todos. Portanto, pare de viver para os outros e viva para você mesmo.' ,
    'Você só tem um inimigo e um campo de batalha: a sua mente.' ,
    'Se os problemas te derem uma rasteira, levante e ria da cara deles.' ,
    'Ao invés de chorar pelo leite derramado, aperte as tetas da vaca e baba mais um copo.' ,
    'O único modo de alguém ser feliz é julgar-se feliz.' ,
    'Deixe aos homens a ignorância dos homens, então, dê tempo ao tempo.' ,
    'Mais difícil do que ter uma grande ideia é reconhecer uma. Especialmente se for de outra pessoa!']
    
    if quantidade == 0:
        print("Você digitou Zero! , por isso nenhum conselho foi gerado.")
    
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
    
def menu():
    print("*" * 25)
    print("GERADOR DE CONSELHOS")
    print("*" * 25)
    time.sleep(1)
    print()
 
while True: 
    menu()
    argumento()
    os.system('clear') or None