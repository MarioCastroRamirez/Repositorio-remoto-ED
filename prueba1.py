#HE HECHO UNA MODIFICACIÓN @MAIKEL_RICH

import random

def adivinar_numero():
    num = random.randint(1, 10)
    num_usuario = 0
    vidas = 0
    print("PEDREROL CHURRERO")
    while num_usuario != num:
        num_usuario = str(input("Escribe un número (del 1 al 10) -->"))

        while not num_usuario.isdigit():
            num_usuario = str(input("No es un número, escribe un número (del 1 al 10) -->"))

        num_usuario = int(num_usuario)

        if vidas != 2:
            if num_usuario > num:
                print("El numero a adivinar es menor")
                vidas += 1
            elif num_usuario < num:
                print("El numero a adivinar es mayor")
                vidas += 1
            elif num_usuario == num:
                print(f"Correcto! el número es el {num}")
                print(f"Numero de intentos {vidas + 1}")
        else:
            print(f"Perdiste, no lo adivinaste en 3 intentos, el numero era {num}")
            break

advinar_numero()
