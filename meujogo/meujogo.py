

def adicionar_bloco():
    window.model._adicionar_bloco()

def remover_bloco():
    window.model._remover_bloco()

def mover_personagem_frente():
    window.model._mover_personagem_frente()

def mover_personagem_atras():
    window.model._mover_personagem_atras()

def mover_personagem_acima():
    window.model._mover_personagem_acima()

def mover_personagem_abaixo():
    window.model._mover_personagem_abaixo()

def mover_personagem_direita():
    window.model._mover_personagem_direita()

def mover_personagem_esquerda():
    window.model._mover_personagem_esquerda()

def iniciarMundo():
    pyglet.app.run()
    
def configurarMundo():
    global window 
    global bloco 
    global voar 
    bloco = 'GRAMA'
    voar = False
    window = Window(width=1200, height=900, caption='Pyglet', resizable=True)
    window.set_exclusive_mouse(False)
    setup()
    window.model._initialize()
