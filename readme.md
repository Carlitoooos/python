# Apuntes de archivos en python

 *leer y recorrer un archivo con python*

 1.  los archivo se cargan por completo dentro de una variable.
 2.  al recorrer un archivo con un for e imprimir su contenido de manera bruta se incorporaran los saltos de lineas.

 3. para abrir un archivo en python se debe de almacenar el archivo ya sea .csv , .html , .json dentro de una variable como se muestra en el siguiente ejemplo.

 4. ademas el codigo con el que se planea abrir un archivo se tiene que encontrar en la misma carpeta que el archivo.

 ```py
archivo = open("campeones_rally_virtual.csv","r")
 ```
 donde archivo es la variable en la que se almacenara el contenido del archivo, open el comando, "campeones_rally_virutal.csv" el nombre del archivo que se quiere leer junto con su extencion y "r" la operacion a realizar con el archivo, r = read y w = write es decir lectura o escritura, si no se especifica la operacion a realizar python interpretara por defecto que es lectura.

 ---
## replace:

sirve para reemplazar caracteres en especificos por otros.

  ```py
  .replace("x","y")
  ``` 
  
  *donde x es el caracter por reemplazar e y el caracter con el que se reemplazara*

  es de destacar que el string original no modifica su valor o contenido sino que en realidad el reemplazo se hace en una nueva variable que es retornada.


---
## comando **stript**:

el comando stript sirve para eliminar caracteres al inicio y al final de un string, si no se especifica un parametros strip eliminara caracteres especiales como los saltos de linea.

## recomendacion

usar el stript antes del split.

`
linea = linea.stript(";")
`

`.stript()`

---
## split:

sirve para separar elementos en base a un caracter especificado generando una lista con sub strings en base de los elementos obtenidos del string original, si no se especifica un parametro se recorta en los espacios espacios en blanco 

`.split(x)` *donde x es el caracter en donde se separara*

---
## close:

importante siempre recordar cerrar el archivo

`.close()`

```py
archivo.close()
```

---
## codigo de ejemplo

```py
archivo = open("archivoDeTexto.txt","r")
for linea in archivo:
    l = linea.stript().split(";")
    print(l[-1])
archivo.close()
```
---

## crear archivos en python

para crear archivos en python se emplea la siguiente estructura

```py
archivo = open("archivo.txt","w")
```

donde el primer parametro es el nombre del archivo que se creara acompañado de la extencion del archivo y el segundo parametro que designa la escritura

## importante

* si el archivo existe este se formateara y quedara en blanco para proseguir a escribir encima.

escribir en un archivo:

```py
archivo.write()
```

en el parametro se inserta la cadena de texto que se quiere escribir en el archivo 

## recordar

para los saltos de linea se usa el  `"\n"`

---

## format
                