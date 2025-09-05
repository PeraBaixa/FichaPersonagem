import random
#classes
class Persona:
    def __init__(obj, nome):
        obj.nome = nome
        obj.vida = [0, 0]
        obj.atributos = {"FOR": 0, "DES": 0, "CON": 0, "INT": 0, "SAB": 0, "CAR": 0}
        obj.bonAtr = {"FOR": 0, "DES": 0, "CON": 0, "INT": 0, "SAB": 0, "CAR": 0}
        obj.ataques = []
        obj.caracs = []
        obj.resist = []
        obj.fraq = []

    def aumentaAtr(obj, valor, atr):
        obj.atributos[str(atr)] += int(valor)

    def recebeAtr(obj, forca, des, con, intel, sab, car):
        obj.atributos["FOR"] = forca
        obj.atributos["DES"] = des
        obj.atributos["CON"] = con
        obj.atributos["INT"] = intel
        obj.atributos["SAB"] = sab
        obj.atributos["CAR"] = car
    
    def sofreDano(obj, dano, tipo):
        if tipo in obj.resist:
            dano /= 2
        elif tipo in obj.fraq:
            dano *= 2
        
        if obj.vida[1] > 0:
            if obj.vida[1] < dano:
                dano -= obj.vida[1]
                obj.vida[1] = 0
            else:
                obj.vida[1] -= dano
                dano = 0
        
        obj.vida[0] -= dano

    def retornaAtr(obj):
        return {"FOR": (obj.atributos["FOR"]+obj.bonAtr["FOR"]), 
                "DES": (obj.atributos["DES"]+obj.bonAtr["DES"]),
                "CON": (obj.atributos["CON"]+obj.bonAtr["CON"]),
                "INT": (obj.atributos["INT"]+obj.bonAtr["INT"]),
                "SAB": (obj.atributos["SAB"]+obj.bonAtr["SAB"]),
                "CAR": (obj.atributos["CAR"]+obj.bonAtr["CAR"])}
    
    def setVida(obj, vida):
        obj.vida[0] = vida
    
    def adiCarac(obj, carac):
        if carac.atr != 'SUP':
            obj.bonAtr[carac.atr] += carac.bonus
        obj.caracs.append(carac)
    
    def delCarac(obj, caracNome):
        cont = 0
        
        while cont < len(obj.caracs):
            if obj.caracs[cont].nome == caracNome:
                if obj.caracs[cont].atr != 'SUP':
                    obj.bonAtr[obj.caracs[cont].atr] -= obj.caracs[cont].bonus
                del obj.caracs[cont]
                break
            cont += 1
        else:
            print(f"O personagem {obj.nome} não tem a caracteristica {caracNome}")

class Ataque:
    def __init__(obj, tipo, efeito, desc, bonus):
        #tipo do dano ('suporte' se for uma forma de cura)
        obj.tipo = tipo
        
        #'efeito' é o dano ou cura máximo possível do ataque
        obj.efeito = []
        #se receber uma lista,
        #o primeiro item vai ser valor total dos dados
        #e o segundo o bônus fixo:
        if isasset(list, efeito):
            obj.efeito.append(efeito[0])
            obj.efeito.append(efeito[1])
        #se não for uma lista,
        #o item vai ser o valor total dos dados
        #e o bônus fixo será zero:
        else:
            obj.efeito = [efeito, 0]

        #descrição geral do ataque
        obj.desc = desc

        #o valor bonus a ser adicionado quando houver testes para acertar
        obj.bonus = bonus

    def acao():
        return random.random(1, efeito[0])+efeito[1]

class Carac:
    def __init__(obj, nome, bonus, *atr):
        obj.nome = nome
        obj.bonus = bonus
        obj.atr = 'SUP'

        if len(atr) > 0:
            match atr[0]:
                case 'FOR'|'DES'|'CON'|'INT'|'SAB'|'CAR':
                    obj.atr = atr[0]
       
    def getBonus(obj):
        return [obj.bonus, obj.atr]
    
    def __str__(obj):
        return f"O nome dessa característia é {obj.nome}"

caracs = [Carac('Pele de fogo', 4)]
caracs.append(Carac('Língua de aço', 3, 'CAR'))
caracs.append(Carac('Poder do aço', 5, 'CON'))

link = Persona('Link')
link.recebeAtr(16, 15, 14, 13, 12, 11)
print(f"Seu carisma é {link.retornaAtr()['CAR']} sem uma caracteristica")
link.adiCarac(caracs[1])
print(f"Seu carisma é {link.retornaAtr()['CAR']} com uma caracteristica")
link.delCarac('Língua de aço')
print(f"Seu carisma é {link.retornaAtr()['CAR']} sem uma caracteristica")
