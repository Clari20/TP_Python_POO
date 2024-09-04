"""Codifique un método que reciba como parámetro una cadena y determine si la
misma contiene o no números."""

cadena = input("Ingrese una cadena: ")

letras = cadena.isalpha()

digit = cadena.isdigit()

ambos = cadena.isalnum()

if letras == True:
    print(f"La cadena ''{cadena}'' tiene letras dentro")

elif digit == True:
    print(f"La cadena ''{cadena}'' tiene numeros en su interior")

elif ambos == True:
    print(f"La cadena ''{cadena}'' tiene tanto numeros como letras")

else: 
    print("La cadena no es valida")





