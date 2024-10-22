# DNS Tool with Python / Herramienta DNS con Python

This Python script allows you to query DNS records (A, MX, NS, and AAAA) for any domain and attempts a DNS zone transfer (if allowed by the DNS server). It is built using the `dnspython` library.

Este script de Python te permite consultar registros DNS (A, MX, NS y AAAA) de cualquier dominio e intenta realizar una transferencia de zona DNS (si el servidor DNS lo permite). Está construido usando la librería `dnspython`.

## Features / Funcionalidades

- Query DNS records: A, MX, NS, and AAAA.
- Attempt DNS zone transfer if the server allows it.
- Provides clear error handling for when records or transfers are not available.

- Consultar registros DNS: A, MX, NS, y AAAA.
- Intentar la transferencia de zona DNS si el servidor lo permite.
- Manejo de errores claro cuando no se encuentran registros o no es posible realizar la transferencia.

## Requirements / Requisitos

- Python 3.x
- `dnspython` library

You can install the required library with:
Puedes instalar la librería requerida con:


`pip install dnspython`

## Kali Linux / Parrot OS
In Kali Linux and Parrot OS, due to restrictions on system packages, you might need to install dependencies in a virtual environment with the --break-system-packages option. Here’s how to set it up:

En Kali Linux y Parrot OS, debido a las restricciones sobre los paquetes del sistema, es posible que debas instalar dependencias en un entorno virtual con la opción --break-system-packages. Aquí te explicamos cómo configurarlo:

`pip install dnspython --break-system-packages`

## Run the script / Ejecuta el script:

Now you can run the script within the virtual environment.

Ahora puedes ejecutar el script dentro del entorno virtual.

`python3 DNS_Python.py`

## MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



