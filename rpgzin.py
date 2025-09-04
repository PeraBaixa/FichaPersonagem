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
    def __init__(obj, nome, bonus, atr):
        match atr:
            case 'FOR'|'DES'|'CON'|'INT'|'SAB'|'CAR':
                obj.atr = atr
            case __:
                print("Atributo inválido")
                return None
        obj.nome = nome
        obj.bonus = bonus
       
    def getBonus(obj):
        return [obj.bonus, obj.atr]
    
    def __str__(obj):
        return f"O nome dessa característia é {obj.nome}

carc = Carac('Fogo', 4, 'CON')
print(carc)
