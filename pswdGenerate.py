import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
simbols = "()?*.-_,"

print("\033[1;31m" + "\nEL ESCRIPT SOLO PERMITE UN MAXIMO DE 70 CARACTERES!!!\n PD : SE RECOMIENDA QUE LA CONTRASEÑA TENGA UN MINIMO DE 12 CARACTERES PARA QUE SEA UN 99" + '% ' + "SEGURA" + "\033[0;m")
print("\nINTRODUCE LA CANTIDAD DE CARACTERES QUE QUIERES")
numero_caracteres = int(input(">>>> "))

all = lower + upper + numbers + simbols
length = (numero_caracteres)
password = "".join(random.sample(all, length))
print("\nEsta Es Tu Contraseña : " + "\033[1;31m" + password + "\033[0;m")