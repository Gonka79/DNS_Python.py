#!/usr/bin/python3
import dns.resolver
import dns.query
import dns.zone
import sys

# Pedir al usuario que ingrese un dominio
dominio = input("Introduce el dominio a escanear: ")

# Función para realizar una transferencia de zona
def consulta_zona(dominio):
    try:
        # Resolvemos los servidores NS (Name Servers)
        ns = dns.resolver.resolve(dominio, 'NS')
        primary_ns = str(ns[0])  # Seleccionamos el primer servidor NS para la transferencia de zona
        print(f"Intentando la transferencia de zona desde el servidor NS: {primary_ns}")
        
        # Intentamos una transferencia de zona
        zona = dns.query.xfr(primary_ns, dominio)
        z = dns.zone.from_xfr(zona)

        print(f"\nZona DNS para el dominio {dominio}:\n")
        for nombre, nodo in z.nodes.items():
            print(f"Registro: {nombre.to_text()} {z[nombre].to_text(nodo)}")

    except dns.resolver.NoAnswer:
        print(f"No se encontró servidor NS para {dominio}.")
    except dns.exception.FormError:
        print(f"La transferencia de zona no está permitida para {dominio}.")
    except Exception as e:
        print(f"Error en la transferencia de zona: {e}")

# Consultar los registros DNS para el dominio ingresado
try:
    # Intentar obtener los registros A
    try:
        ansA = dns.resolver.resolve(dominio, 'A')
        print("\nA Records:")
        print(ansA.response.to_text())
    except dns.resolver.NoAnswer:
        print("\nNo se encontraron registros A.")

    # Intentar obtener los registros MX
    try:
        ansMX = dns.resolver.resolve(dominio, 'MX')
        print("\nMX Records:")
        print(ansMX.response.to_text())
    except dns.resolver.NoAnswer:
        print("\nNo se encontraron registros MX.")

    # Intentar obtener los registros NS
    try:
        ansNS = dns.resolver.resolve(dominio, 'NS')
        print("\nNS Records:")
        print(ansNS.response.to_text())
    except dns.resolver.NoAnswer:
        print("\nNo se encontraron registros NS.")

    # Intentar obtener los registros AAAA
    try:
        ansAAAA = dns.resolver.resolve(dominio, 'AAAA')
        print("\nAAAA Records:")
        print(ansAAAA.response.to_text())
    except dns.resolver.NoAnswer:
        print("\nNo se encontraron registros AAAA.")
        
    # Intentar hacer una transferencia de zona
    consulta_zona(dominio)

except Exception as e:
    print(f"Error en la consulta DNS: {e}")
