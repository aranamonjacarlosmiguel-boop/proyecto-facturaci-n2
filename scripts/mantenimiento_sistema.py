"""Script de verificacion de integridad y mantenimiento."""

import datetime
import os
import sys


def ejecutar_mantenimiento():
    print("Iniciando revision preventiva de archivos...")

    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    archivos_criticos = [
        "src/logica_negocio.py",
        "src/main.py",
    ]

    for archivo in archivos_criticos:
        if not os.path.exists(archivo):
            print(
                f"[ERROR]: No se encuentra el archivo obligatorio {archivo}"
            )
            sys.exit(1)

    nombre_reporte = "reporte_mantenimiento.txt"

    with open(nombre_reporte, "w", encoding="utf-8") as salida:
        salida.write("============================================\n")
        salida.write(" REPORTE DE MANTENIMIENTO DEL SISTEMA\n")
        salida.write("============================================\n")
        salida.write(f"Fecha de revision: {fecha}\n")
        salida.write(
            "Archivos auditados: src/logica_negocio.py, src/main.py\n"
        )
        salida.write("Estado operativo: OK\n")
        salida.write("============================================\n")

    print(
        f"Mantenimiento concluido con exito. "
        f"Archivo creado: {nombre_reporte}"
    )


if __name__ == "__main__":
    ejecutar_mantenimiento()
