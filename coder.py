def iniciar_sesion(base_datos):
    usuario_nuevo = input("Ingrese el usuario registrado:")
    if usuario_nuevo in base_datos:
        print("Usuario correcto.")
        contraseña_nueva = input ("Ingrese la contraseña: ")
        if contraseña_nueva == base_datos[usuario_nuevo]:
            print("Contraseña Correcta")
            print("Bienvenido usuario!")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no valido.")

base_datos = {
    "primerUsuario": "contraseña1",
    "segundoUsuario": "contraseña2",
}

if __name__ == "__main__":
    iniciar_sesion(base_datos)