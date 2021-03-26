texto ="Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigrestigres" 
texto = texto.lower().replace(",","").split()
palabra=input("ingrese una palabra")
cant=0
for elem in texto:
    if elem == palabra:
        cant+=1
print(f"la palabra {palabra} se repite {cant} veces")        