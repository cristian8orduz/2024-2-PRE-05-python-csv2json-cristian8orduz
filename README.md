# Descripción

El archivo `country_scientific_production.py` implementa un un programa que 
computa el número de publicaciones científicas por país a partir de la columna
`affilitions` de un archivo CSV. El programa genera un mapa mundial donde los 
colores de los paises son proporcionales al número de publicaciones científicas.


Complete el código siguiendo las instrucciones que aparecen en 
`country_scientific_production.py`.

# Configuración en MacOS y Linux

## Instalación del ambiante de desarrollo

Ejecute los siguientes comandos en el terminal:

```bash
python3 -m venv .venv
source .venv/bin/activate
source setup.sh
```

## Calificación del laboratorio

Ejecute los siguientes comandos en el terminal:

```bash
./tests/run.sh
```

# Configuración en Windows

## Instalación del ambiante de desarrollo

Ejecute los siguientes comandos en el terminal:

```bash
python3 -m venv .venv
.venv\Scripts\activate
setup
```

## Calificación del laboratorio

Ejecute los siguientes comandos en el terminal:

```bash
tests\run
```