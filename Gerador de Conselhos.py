import random
import tkinter as tk
import time

def gerar_conselhos():
    conselho_aleatorios = [
        "As montanhas da vida não existem apenas para que você chegue no topo, mas para que você aprenda o valor da escalada.",
            "A vida pode até te derrubar, mas é você quem escolhe a hora de se levantar.",
            "É melhor ser verdadeiro e solitário do que viver em falsidade e estar sempre acompanhado.",
            "Na minha vida até agora, descobri que na verdade só há dois tipos de pessoas: aqueles que estão com você, e aqueles que estão contra você. Aprenda a reconhecê-los, pois eles são frequentemente e facilmente confundidos um com o outro.",
            "Ser feliz não é ter uma vida perfeita, mas sim reconhecer que vale a pena viver apesar de todos os desafios e perdas.",
            "Aprendi que não devo me importar com comentários que não vão mudar minha vida.",
            "A vida tem sons, que pra gente ouvir precisa aprender a começar de novo. É como tocar o mesmo violão e nele compor uma nova canção.",
            "Na vida irás encontrar três tipos de pessoas: aquelas que irão mudar a tua vida, aquelas que irão prejudicar a tua vida, aquelas que serão a tua vida.",
            "A vida é basicamente uma montanha russa. Tem seus altos e baixos, e o mais importante: você tem que fazer o ingresso valer a pena.",
            "O mundo está nas mãos daqueles que têm a coragem de sonhar e de correr o risco de viver seus sonhos.",
            "Deus sabe quem colocar na sua vida, da mesma forma que sabe quem tirar.",
            "Não viva para que sua presença seja notada, mas para que sua falta seja sentida.",
            "Um novo dia é uma página em branco na sua vida. Escreva apenas o que vale a pena. Bom dia!",
            "Passamos a vida procurando em pessoas o que só podemos encontrar em Deus.",
            "...bom mesmo é ir à luta com determinação, abraçar a vida com paixão, perder com classe e vencer com ousadia, porque o mundo pertence a quem se atreve e a vida é muito pra ser insignificante."]
    try:
        quantidade = int(entrada.get())
    except ValueError:
        gerado["text"] = "Por favor, digite uma número inteiro."
        return
        
    if quantidade == 0:
        gerado["text"] = "Você digitou Zero!, por isso nenhum conselho foi gerado."
        return
    
    if quantidade <= 15:
        palavras_sorteadas = []
        conselhos = []
        for i in range(quantidade):
            conselho = random.choice(conselho_aleatorios)
        
            while conselho in palavras_sorteadas:
                conselho = random.choice(conselho_aleatorios)
            
            palavras_sorteadas.append(conselho)
            conselhos.append(conselho)
        
        gerado["text"] = "\n\n".join([f"conselho {i+1}: {conselho}" for i, conselho in enumerate(conselhos)])
        
    else:
        gerado["text"] = "A quantidade de conselhos é 15. Por favor informe novamente."

janela = tk.Tk()
janela.title("GERADOR DE CONSELHOS")

menu = tk.Label(janela, text="GERADOR DE CONSELHOS", font=("Arial", 20))
menu.pack()

entrada_label = tk.Label(janela, text="Digite a quantidade de conselhos (1-15):")
entrada_label.pack()

entrada = tk.Entry(janela)
entrada.pack()

botao_gerar = tk.Button(janela, text="Gerar Conselhos", command=gerar_conselhos)
botao_gerar.pack()

gerado = tk.Label(janela, text="")
gerado.pack()

janela.mainloop()
