# EXAMEN TRANSVERSAL FPY1101 - FITPASS

def validar_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor: return valor
        print("Error: El campo no puede estar vacio.")

def validar_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0: return valor 
            print("Error: El número debe ser mayor a cero.")
        except ValueError:
         print("Error:Ingrese un número entero válido.")

def convertir_a_booleano(mensaje):
    while True:
        valor = input(f"{mensaje} (s/n): ").lower()
        if valor == 's': return True
        elif valor == 'n': return False
        print("Error: Ingrese 's' o 'n'.")

def registrar_plan(dicc_planes, dicc_cupos):
    print("\n--- Registro de Plan ---")
    codigo = validar_no_vacio("Ingrese nombre del plan: ")
    if codigo in dicc_planes:
        print("Error: El código ya existe.")
        return
    nombre = validar_no_vacio("Ingrese nombre del plan: ")
    while True:
        tipo = input("Tipo (mensual/trimestral/anual) ").lower()
        if tipo in ['mensual', 'trimestral', 'anual']: break
        print("Error: Tipo no válido.")
    duración = validar_entero_positivo("Duración (meses): ")
    piscina = convertir_a_booleano("¿Acceso a piscina?")
    clases = convertir_a_booleano("¿Clases grupales?")
    horario = validar_no_vacio("Franja horaria:")
    dicc_planes[codigo] = [nombre, tipo, duración, piscina, clases, horario]
    dicc_cupos[codigo] = validar_entero_positivo("Cantidad de cupos iniciales: ")
    print("Plan registrado.")

def inscribir_cliente(dicc_planes, dicc_cupos):
    codigo = input("Ingrese código de plan para inscribir: ")
    if codigo in dicc_cupos:
        if dicc_cupos[codigo] > 0:
            dicc_cupos[codigo] -= 1 # OPERACIÓN ARITMETICA (IE 2.2.1)
            print(f"Inscripición exitosa. Cupos restantes: {dicc_cupos[codigo]}")
        else:
            print("Error: No quedan cupos para este plan.")
    else:
        print("Error: Código no encontrado.")

def mostrar_planes(dicc_planes, dicc_cupos):
    if not dicc_planes:
           print("No hay planes.")
           return
    print("\n" + "="*30)
    for codigo, info in dicc_planes.items():
        print(f"Cod: {codigo} | Plan: {info[0]} | Cupos: [dicc_cupos[codigoi]]")
    print("="*30)

def main():
    planes, cupos = {}, {}
    while True:
        print("\n1. Registrar | 2. Mostrar | 3.Inscribir | 4.Salir")
        opc = input("Seleccione: ")
        if opc == '1': registrar_plan(planes, cupos)
        elif opc == '2': mostrar_planes(planes, cupos)
        elif opc == '3': inscribir_cliente(planes, cupos)
        elif opc == '4': break
        else: print("Opción no válida.")

if __name__ == "__main__":
   main()
        



