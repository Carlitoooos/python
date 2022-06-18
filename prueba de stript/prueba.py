archivo = open("prueba.txt","w")
archivo.write("asuka:asuka"+"\n")
archivo.write("asuka:asuka"+"\n")
archivo.write("asuka:asuka"+"\n")
archivo.write("asuka:asuka"+"\n")
archivo.write("asuka:asuka"+"\n")
archivo.close()


archivo = open("prueba.txt","r")
for linea in archivo:
    l = linea.strip().strip("a").split(":")
    print(l[-1])
archivo.close()