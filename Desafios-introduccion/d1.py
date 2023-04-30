#Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de sus ventas totales y el departamento comercial te solicita que ayudes a los vendedores a calcular sus comisiones creando un programa que les pregunte su nombre y cuánto han vendido en éste mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le corresponde por las comisiones.
nombre = input("Ingresa tu nombre: ")
ventas_mes = float(input("Ingresa tus ventas del mes: "))

comision = ventas_mes * 0.06

print("Hola", nombre + ", tus comisiones por este mes son de:", comision, "pesos.")