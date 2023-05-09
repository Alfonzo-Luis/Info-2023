#Desafío 3: Adivina el número
#Requisitos técnicos:
#- Operadores lógicos.
#- Operadores de comparación.
#- Control de flujo - Condicionales.
#- Control de Flujo - Repetitivas.
#Vamos a crear un juego completamente funcional.
#Para ello el programa debe:
#* Pedir al usuario que ingrese su nombre.
#* Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
#* Generar aleatoriamente un número entero entre 1 y 100.
#tip 1: importar de la biblioteca random la función randint (Tu profe te explicará en clase cómo hacerlo)
#* Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número.
#El "número" ingresado por el usuario puede:
#* No ser un número entero, en éste caso avisarle que no es un número entero el que ingresó.
#tip 2: con el método isdigit() puedes saber si es posible convertir a entero
#* Ser menor al que tiene que adivinar, en éste caso informarle que el número a adivinar es mayor.
#* Ser mayor al que tiene que adivinar, en éste caso informarle que el número a adivinar es menor.
#* Igual al que tiene que adivinar, en éste caso informarle que ha ganado y decirle en cuál intento lo adivinó.
#* Si el usuario no ingresa un número entero no debes descontarle un intento, en los demás casos si debes descontarle un intento.
#* En cada intento debes informarle al usuario los intentos que le quedan disponibles y solicitarle que ingrese otro número.
#* Si el usuario no acierta en los 8 intentos, debes informarle que se agotaron los intentos y cuál era el número que tenía que adivinar.
