# Game Ping-Pong

#Meu trabalho aqui é apenas comentar o código e identificar o que sei



from tkinter import *
import random
import time

""""
importando bibliotecas:
tkinter para construir a interface
random para solecionar números aleatoriamente
time para fazer o código 'esperar' e/ou utilizar temporizador
"""

level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))
length = 500/level

#Aqui uma variável vai recceber um número, que será o denominador de um cálculo para definição da variável length

root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

#aqui, uma variável root está recebendo alguns parâmetros da biblioteca tkinter, o que certamente está reacionado a interface do jogo

canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()

#Aqui é definido o tamano e cores da tela, com o método .pack(), que também é da biblioteca tkinter e serve para widgets

root.update()

# definição de Variável count como zero e lost como false
count = 0
lost = False

class Bola:
#Definida a classe Bola para colcoar as configurações referentes a bolinha do jogo

    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

#dentro da função init são definidos os parâmetros, o tamanho da bolinha e movimento.

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)
#marou a posição nicial da bolinha e o random para alternar a posição
        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)

#Acima, imagino que seja a veriicação do final do jogo, caso esteja acima/abaixo de 3 ...

        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1
                score()


        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True

#Saiu das condições de ifs, GmeOver!

class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3


def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()


def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

def game_over():
    canvas.itemconfig(game, text="Game over!")


Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

root.mainloop()



