texto="Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres."

letra = input("ingrese una letra")

lista= texto.lower().replace(",","").split()

for ele in lista:
    if ele[0] == letra:
        print(ele)