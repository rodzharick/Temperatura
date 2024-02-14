# Ejerecicio N.2: programa para convertir una cantidad de grados c en la equivalencia a k y f

# imput
C= input("digitela cantidad de grados C a convertir")
C= int(C)

# PROCESSING
F= (C*(9/5))+32
K= C+273.15

# OUTPUT
print("grados fahrenheit:"+str(F))
print("grados kelvin:"+str(K))