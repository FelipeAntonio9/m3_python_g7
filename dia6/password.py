# crear un script de ingreso de password
# donde el largo minimo es de 6 caracteres
import getpass
# password=input("Ingrese su contraseña: ")
password = getpass.getpass("Ingrese su contraseña: ")

print("\n")
if password == "12345":
    print("El password es incorrecto")
elif len(password) < 6:
    print("El password es demasiado corto")
