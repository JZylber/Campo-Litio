# Simulador Extracción de Litio

## Introducción
Luego de un exitoso trabajo en el simulador de los campos minados, la corporación A.C.M.E. vuelve a pedir tus servicios. Con los caminos limpios, los camiones pueden traer la producción de litio para procesar. Nuevamente, contamos con un simulador que nos permite optimizar la producción. Tiene alguno errores y faltan funcionalidades, necesitamos que lo arreglen.

## Objetivos
Hacer un conjunto de tests para el programa, y debugguearlo usando dichos tests.

## Especificiación del programa
El programa simula la extracción de litio. Recibe una lista de campos de litio, en donde cada veta de litio representa una tonelada de litio. Para cada campo:
1. Se extrae todo el litio, que implica pasar de una veta de litio "L" a el litio extraído, "LE", listo para ser recogido
2. Se prepara un camión con la nafta justa para recorrer el campo. El camión gasta una unidad de nafta por cada lote del campo, y debe recorrer el campo entero.
3. El camión recorre el campo, recogiendo el litio extraído, es decir, donde hay "LE", deja nada. Si el camión se queda sin nafta en el medio del recorrido, se queda ahí (Agregando una "C" al campo) y no puede continuar juntando el material extraído ni acumularlo en la central.

Finalmente, se guardan los totales de litio extraídos en todos los campos y las unidades de nafta utilizadas. Se calcula el total de agua usada (2,000,000 por tonelada de litio) y se devuelve el litio extraído, los tanques de nafta y agua usadas.

## Detalles técnicos
Ya hay una implementación parcial de este programa. Se divide en algunas funciones que **deberían** cumplir con estas características:
- `excavar_campo`: Toma un campo (lista de listas de str) y a toda veta de litio, "L", la extrae, "LE"
- `preparar_camion`: Toma un campo (lista de listas de str), y retorna un camión con la nafta **justa** para recorrer dicho campo. Cada camión es un diccionario que tiene dos llaves: nafta y litio. Nafta representa el combustible, y litio el litio juntado.
- `recuperar_litio`: Toma un campo y un camión (dicionario con nafta y litio) y recorre todo el campo, juntando el litio extraído ("LE" -> ""). Si el camión se queda sin nafta en medio del recorrido, se debe marcar que hay un camión abandonado en el campo ("" -> "C"), y la función debe retornar falso (ya que el camión no llegó a destino). Si el camión recorre existosamente todo el campo, se debe retornar verdadero.
- `extraer_litio`: Realiza el proceso principal. Toma una lista de campos de litio, y a cada uno excava el litio, prepara un camión y lo recoge. Guarda el total de litio obtenido (siempre y cuando el camión no se haya quedado sin nafta), la nafta usada y el agua usada. Retorna estos 3 valores.