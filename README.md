# Desafío Legalbot

## Objetivo e Instrucciones

El objetivo de este desafío es validar tus habilidades lógicas y conocimientos de programación en Python. Hemos preparado esta actividad con desarrollos que ya hemos realizado en la empresa y nos gustaría saber cómo los hubieses enfrentado tú.

El desafío se separa en los tres ámbitos que te tocará abordar en tu rol: Web Scraping, Extracción de información y Procesamiento de Lenguaje Natural

Este desafío cuenta de tres partes independientes. Si no logras realizar alguna de ellas envía de todas formas tus respuestas de las otras partes. Envía tus resultados en forma de repositorio en Github.

## Parte 1: Web Scraping

En la página del Diario Oficial (https://www.diariooficial.interior.gob.cl/) se encuentran todas las publicaciones digitalizadas de los últimos años. Estas publicaciones corresponden a extractos de publicaciones de leyes, normas y constitución de empresas entre otras. Para este ejercicio nos enfocaremos solo en la parte de empresas.

Si navegas a la sección de "EDICIÓN ELECTRÓNICA" y luego a la sub-sección de "EMPRESAS Y COOPERATIVAS" verás un detalle de todas las Constituciones, Modificaciones y Disoluciones del día actual.

1.- Construye una función que descargue en una carpeta todos los PDFs (CVE-157XXXX) del tipo CONSTITUCIÓN del día actual. Incluye los archivos en la respuesta.

```python
"""
path:string > path a la carpeta donde bajar los archivos
"""
def download_todays_constituciones(path):
   ...
   ...
```

2.- **(BONUS)** Construye una función que descargue todas las constituciones del año 2019. No es necesario correr esta función ni incluir los archivos en la respuesta.

```python
"""
path:string > path a la carpeta donde bajar los archivos
year:number > año a descargar (ej: 2019)
"""
def download_constituciones_from_year(year, path):
   ...
   ...
```

## Parte 2: Extracción de información

1.- En la carpeta "sociedades-pdf" verás 5 archivos PDF con constituciones de sociedad. Escribe una función que sea capaz de extraer el texto de cada PDF.

**Importante**: para resolver este problema no utilices una librería que lo traspase primero a imagen, intenta leer directamente el archivo y transformarlo a texto.

```python
"""
pdf_path:string > path al archivo PDF
"""
def pdf_to_text(pdf_path):
   ...
   ...
   return text
```

2.- **(BONUS)** ¿Puedes extraer con la misma función de la parte (1) los textos de los PDF en la carpeta "sociedades-b-pdf"? ¿Qué es lo distinto? Si es que no pudiste: ¿Cómo lo resolverías? No es necesario escribir/programar la solución, solamente mencionar el problema y como lo abordarías.

## Parte 3: Procesamiento de Lenguaje

En la carpeta "sociedades-texto" verás una lista de +400 textos de sociedades ya extraídas.

1.- Escribe una función que imprima en consola el nombre y RUT de quienes comparecen(\*) en la escritura.

(\*) Puedes ver quienes comparecen generalmente en el tercer párrafo, bajo el RUT de la sociedad. Ejemplo:

> En RECOLETA, Región METROPOLITANA DE SANTIAGO, Chile, a 18 de mayo del 2018, ante el Registro Electrónico de Empresas y Sociedades, **comparecen: ANDREA PAULINA NÚÑEZ ESPINOZA, Rut 15.602.114-8, domiciliada en El Marco N°1020 villa Augusto Zamorano, comuna de RECOLETA, Región METROPOLITANA DE SANTIAGO;** y expone/n: Por el presente acto...

```python
def print_owners():
   ...
   ...
   for...
      ...
      print(...)
   ...
   ...
```

Output esperado

```
-- AC0AV8Q7cIeH.txt --
ANDREA PAULINA NÚÑEZ ESPINOZA, 15.602.114-8

-- AC0b5mWFT80k.txt --
MAURICIO ANDRÉS CAROCA LARA, 15.630.469-7
SANDRA ELIZABETH CORTÉS-MONROY ARAOS, 15.044.523-K

....+400
```
