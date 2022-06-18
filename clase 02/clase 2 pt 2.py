archivo = open("alumnos.txt","r")
aprobados = open("aprobados.txt","w")
reprobados = open("reprobados.txt","W")
for linea in archivo:
    linea_split = linea.strip().split(":") #return: [Esteban","Gutierres","48","18","32"]
    suma = int(linea_split[2])+int(linea_split[3])+int(linea_split[4])
    promedio = round(suma/3,0)
    print(promedio)
    if promedio >= 55:
        aprobados.write("linea_split[0]+" "+linea_split[1]+" "+str(promedio)" +"\n")
    else:
        reprobados.write(linea_split[0]+linea_split[1]+str(promedio))
archivo.close
aprobados.close
reprobados.close
