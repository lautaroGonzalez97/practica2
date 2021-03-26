frase_palabra= input("Ingrese una frase o palabra")
frase_palabra=frase_palabra.lower()
aux=[]
for i in range(len(frase_palabra)):
    if frase_palabra[i] not in aux:
        aux+=(frase_palabra[i])

print(frase_palabra)
palabra="".join(aux)
print(palabra)

if frase_palabra == palabra:
    print ("Es heterograma")
else: print ("No es heterograma")

