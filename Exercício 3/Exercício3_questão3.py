#definindo a função que clacula o IMC:
def IMC (altura, peso):
#cálculo do IMC - os valores são colocados nos parênteses quando se chama a função.
    IMC = float(peso/(altura**2))
#condições
    if IMC<18.5:
        print(IMC, "Abaixo do Peso")
    elif IMC>18.5 or IMC<25:
        print(IMC, "Peso Normal")
    elif IMC>25 or IMC<30:
        print(IMC, "Acima do Peso")
    elif IMC>30:
        print(IMC, "Obeso")
IMC(altura,peso)
