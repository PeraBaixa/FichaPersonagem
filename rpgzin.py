

#classes
class persona():
    def __init__(obj, vida, ataque):
        obj.vida = vida
        obj.ataque = ataque
        obj.escudo = 0
        obj.listaAtaques = []
        obj.resist = []
        obj.fraq = []
    
    def sofreDano(obj, dano, tipo):
        if tipo in obj.resist:
            dano /= 2
        elif tipo in obj.fraq:
            dano *= 2
        
        if obj.escudo > 0:
            if obj.escudo < dano:
                dano -= obj.escudo
                obj.escudo = 0
            else:
                obj.escudo -= dano
                dano = 0
        
        obj.vida -= dano



class ataque():
    def __init__(obj, tipo, efeito, desc):
        obj.tipo = tipo
        obj.efeito = efeito
        obj.desc = desc