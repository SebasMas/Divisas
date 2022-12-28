#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.




Divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

DivisaTextual = input("Escriba una divisa: ")

for divisa in Divisas:
    if divisa == DivisaTextual:
        print("El símbolo del ",DivisaTextual," es ",Divisas[DivisaTextual])
    else:
        pass
