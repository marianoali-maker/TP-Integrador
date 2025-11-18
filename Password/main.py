# Encoding: utf-8
import secrets
import string
import sys
import os

# DICCIONARIO DE CARACTERES PARA GENERAR CONTRASEÑAS
diccionario = {
    'letras': string.ascii_letters,
    'numeros': string.digits,
    'caracteres': string.punctuation
}

# FUNCION PARA GENERAR CONTRASEÑAS
def generar_contrasena(opcion):
    longitud = 10  # Longitud de la contraseña 10 caracteres

    if opcion == "1":
        caracteres = diccionario['letras']
    elif opcion == "2":
        caracteres = diccionario['numeros']
    elif opcion == "3":
        caracteres = diccionario['letras'] + diccionario['numeros']
    elif opcion == "4":
        caracteres = diccionario['letras'] + \
            diccionario['numeros'] + diccionario['caracteres']
    else:
        return None

    return ''.join(secrets.choice(caracteres) for _ in range(longitud))

# MENU PRINCIPAL DEL SISTEMA DE CONTRASEÑAS
def menu_contrasenas():
    try:
        while True:
            os.system("cls") # Para Windows
            print("\n*-------------BIENVENIDO-------------*")
            print("     Generador de Contraseñas V1.0")
            print("*------------------------------------*\n")
            print("Seleccione una de las siguientes opciones:\n")
            print("» 1. Generar contraseña solo de Letras.")
            print("» 2. Generar contraseña solo de Números.")
            print("» 3. Generar contraseña Letras y Números.")
            print("» 4. Generar contraseña Letras, Números y Caracteres.")
            print("» 0. Salir.\n")

            opcion = input("» Escriba la opción seleccionada: ") # Muestra el menú y solicita una opción

            if opcion == "0":
                print("\n===========================================")
                print("        ¿Está seguro que desea salir?")
                print("===========================================\n")
                confirmar = input("(s/n): ")
                if confirmar.lower() == "s": # Confirma la salida
                    print("\n===========================================")
                    print("   ¡Gracias por usar el generador de contraseñas!")
                    print("           Programa finalizado.")
                    print("===========================================\n")
                    sys.exit(0)  # Salida exitosa
            elif opcion in ["1", "2", "3", "4"]:
                contrasena = generar_contrasena(opcion) # Genera la contraseña según la opción seleccionada
                print("\n===========================================")
                print("       Contraseña generada con éxito")
                print("===========================================\n")
                print(f"Su contraseña es: {contrasena}\n") # Muestra la contraseña generada
                input("Presione Enter para continuar...")
            else:
                print("\nOpción inválida, intente nuevamente.") # Maneja opción inválida
                input("Presione Enter para continuar...")
    except KeyboardInterrupt: # Maneja interrupción por teclado
        print("\n\n¡Programa interrumpido por el usuario!")
        sys.exit(1)  # Salida por interrupción

# EJECUTA EL PROGRAMA
if __name__ == "__main__":
    menu_contrasenas()
