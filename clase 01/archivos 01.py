#leer y recorrer un archivo
archivo = open("nombreDelArchivo.csv/txt","r") #read
for linea in archivo:
  linea.strip().replace("buscamos", "el que reemplazara al que buscamos")
  lista_split = linea.stript().split(",")#linea = juan,acevedo,1990 -> #["juan","acevedo","1990"]
  print(lista_split[0])
archivo.close()

#crear un archivo

semis_copa_america = ["Brasil", "Peru","Colombia","Argentina","Panama","Chile","Bolivia"]

archivo = open("semis.txt","w") #write 
archivo.write("Semifinales Copa America\n")
archivo.write("\n")

for pais in semis_copa_america:
  archivo.write(pais+"\n")

archivo.close()

semis_copa_america2 =   [
                            ["Brasil",20], 
                            ["Peru",2],
                            ["Colombia",1],
                            ["Argentina",15]
                        ]

archivo = open("semis2.txt","w")
archivo.write("Informacion de semifinalistas\n")
archivo.write("\n")

#brasil ha salido campeon 20 veces
s = "{0} ha salido campeon {1} veces\n"
for pais in semis_copa_america2: #pais = ["Brasil",20]
  archivo.write(s.format(pais[0],pais[1]))
archivo.close()
