import pickle
import os
import random
import sys

# ===============================#
# FUNCIÓN PRINCIPAL DEL PROGRAMA #
# ===============================#


def sistema_tickets():
    """
    Función principal del programa. 
    Maneja el menú principal y opciones (Alta, Leer, Salir).
    """
    # ----------------------------------------#
    # CONFIGURACIÓN DEL DIRECTORIO DE TICKETS #
    # ----------------------------------------#
    TICKETS_DIR = "Tickets"
    # Crea la carpeta 'Tickets' si no existe. 'exist_ok=True' evita errores.
    os.makedirs(TICKETS_DIR, exist_ok=True)

    # SE INICIA EL BUCLE PRINCIPAL HASTA QUE EL USUARIO DECIDA SALIR
    while True:
        # LIMPIAR PANTALLA
        os.system("cls")

        # MENÚ PRINCIPAL
        print("=" * 50)
        print("      HOLA, BIENVENIDOS AL SISTEMA DE TICKETS   ")  # Título
        print("=" * 50)
        print("1 - Generar un Nuevo Ticket:")
        print("2 - Leer un Ticket:")
        print("3 - Salir")
        print("-" * 50)

        opcion = input("Seleccione: ")

        # --------------------------------#
        # OPCIÓN 1: GENERAR NUEVO TICKET  #
        # --------------------------------#
        if opcion == '1':
            crear_otro = 's'  # Bucle interno

            while crear_otro == 's':
                os.system("cls")
                print("=" * 50)
                print(" " * 15 + "GENERAR NUEVO TICKET" + " " * 15)  # Título
                print("=" * 50)

                # 1 INGRESO Y VALIDACIÓN DE LA INFORMACIÓN

                # NOMBRE Y VALIDACIÓN
                nombre = input("Ingrese su Nombre: ")
                while not nombre.replace(' ', '').isalpha() or not nombre.strip():
                    print(
                        "¡ERROR! El nombre solo puede contener letras y no puede estar vacío.")
                    nombre = input("Ingrese su Nombre: ")

                # SECTOR Y VALIDACIÓN
                sector = input("Ingrese su Sector: ")
                while not sector.strip():
                    print("¡ERROR! El sector no puede estar vacío.")
                    sector = input("Ingrese su Sector: ")

                # ASUNTO  Y VALIDACIÓN
                asunto = input("Ingrese Asunto: ")
                while not asunto.strip():
                    print("¡ERROR! El asunto no puede estar vacío.")
                    asunto = input("Ingrese Asunto: ")

                # MENSAJE Y VALIDACIÓN
                mensaje = input("Ingrese un Mensaje: ")
                while not mensaje.strip():
                    print("¡ERROR! El mensaje no puede estar vacío.")
                    mensaje = input("Ingrese un Mensaje: ")

                # 2 GENERAR NUMERO DE TICKET RANDOM
                numero_ticket = random.randrange(1000, 9999)

                # 3 CREAR EL DICCIONARIO DEL TICKET
                ticket = {
                    'nombre': nombre,
                    'sector': sector,
                    'asunto': asunto,
                    'mensaje': mensaje,
                    'numero': numero_ticket
                }

                # 4 GUARDAR EL TICKET EN UN ARCHIVO (PICKLE)
                nombre_archivo = TICKETS_DIR + "/" + \
                    str(ticket['numero']) + ".pck"
                with open(nombre_archivo, "wb") as f:
                    pickle.dump(ticket, f)

                # 5 MOSTRAR EL TICKET GENERADO
                os.system("cls")
                print("=" * 50)
                print(" " * 15 + "TICKET GENERADO" + " " * 15)  # Título
                print("=" * 50)
                print(f"Nombre: {ticket['nombre']}")
                print(f"Sector: {ticket['sector']}")
                print(f"Asunto: {ticket['asunto']}")
                print("-" * 50)
                print(f"N°Ticket: {ticket['numero']}")
                print(f"Mensaje: {ticket['mensaje']}")
                print("-" * 50)
                print(" " * 15 + "RECUERDE SU NÚMERO" + " " * 15)  # Título
                print("-" * 50)

                # 6 PREGUNTAR SI DESEA CREAR OTRO TICKET
                print("\n" + "-" * 50)
                respuesta = input(
                    "Desea generar un nuevo Ticket? (s/n): ").lower()

                if respuesta == 'n':
                    crear_otro = 'n'

        # ------------------------#
        # OPCIÓN 2: LEER TICKET   #
        # ------------------------#
        elif opcion == '2':
            leer_otro = 's'  # Bucle interno

            while leer_otro == 's':
                os.system("cls")
                print("=" * 50)
                print(" " * 15 + "CONSULTAR TICKET" + " " * 15)  # Título
                print("=" * 50)

                # 1 PEDIR NÚMERO DE TICKET Y CREAR RUTA
                num_a_buscar = input("Ingrese el número de ticket: ")
                ruta_archivo = TICKETS_DIR + "/" + num_a_buscar + ".pck"

                # 2 BUSCAR Y CARGAR EL TICKET
                if os.path.isfile(ruta_archivo):
                    # El archivo existe, ¡lo cargamos!
                    with open(ruta_archivo, "rb") as f:
                        ticket_cargado = pickle.load(f)
                    # UTF-8 se decodifica automáticamente

                    # MUESTRAR EL TICKET CARGADO
                    os.system("cls")
                    print("=" * 50)
                    print(" " * 15 + "TICKET CONSULTADO" + " " * 15)  # Título
                    print("=" * 50)
                    print(f"Nombre: {ticket_cargado['nombre']}")
                    print(f"Sector: {ticket_cargado['sector']}")
                    print(f"Asunto: {ticket_cargado['asunto']}")
                    print("-" * 50)
                    print(f"N°Ticket: {ticket_cargado['numero']}")
                    print(f"Mensaje: {ticket_cargado['mensaje']}")
                    print("-" * 50)

                else:
                    # EL ARCHIVO NO EXISTE, MOSTRAR ERROR
                    print("¡ERROR!")
                    print("No existe un ticket con el número:", num_a_buscar)
                    input("Presione Enter para continuar y vuelva a intentar!")

                # 3 PREGUNTA SI DESEA LEER OTRO TICKET
                print("\n" + "-" * 50)
                respuesta = input("Desea leer otro Ticket? (s/n): ").lower()

                if respuesta == 'n':
                    leer_otro = 'n'

        # -----------------#
        # OPCIÓN 3: SALIR  #
        # -----------------#
        elif opcion == '3':
            os.system("cls")
            confirmacion = input(
                "¿Está seguro que desea salir del sistema? (s/n): ").lower()
            if confirmacion == 's':
                print("¡Gracias por utilizar el sistema de Tickets! ¡Hasta pronto!")
                sys.exit()  # Cierra el programa

        # ------------------#
        # OPCIÓN INVALIDA   #
        # ------------------#
        else:
            print("Opción invalida. Presione Enter para volver al menú principal.")
            input()


# FUNCION PARA EJECUTAR EL PROGRAMA
if __name__ == "__main__":
    sistema_tickets()
