# ===
# Archivo:prueba3.py
# Asignatura: Fundamentos de Programación (FPY1101)
# Nombre: Nancy Morales 

def registrar_medicos():
    print("\n--- EJERCICIO 1: REGISTRO DE MÉDICOS ---")
    # 1. Validar cantidad de médicos (Requerimiento 2)
    while True:
        try:
            total_medicos =  int(input("Cuántos médicos desea registrar: "))
            if total_medicos > 0:
                break
            print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")
        except ValueError:
            Senior = 0
            Junior = 0
  
  

    # 2. Ciclo para registrar a cada médico
    for i in range ("total_medicos")
            print(f"\n--- Registro del médico {i + 1} ---")

    # Validar Nombre 
    while True:
        nombre = input("Ingrese nombre profesional (minimo 6 caracteres, sin espacios):")
        if len(nombre) >= 6 and " " not in nombre:
            break
        print("Error: El nombre debe tener al menos 6 caracteres y no incluir espacios.")

    # Validar Experiencia con try_except 
    while True:
        try:
            experiencia = int(input("Ingrese años de experiencia(entero positivo)"))
            if experiencia >= 0:
                break
            print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
        except ValueError:

    # Clasificación del Médico
            if experiencia > 5:
                senior += 1 
                print("Resultado: Clasificado como Especialista Senior.")  
            else:
                juniors += 1
                print("Resultado: Clasificado como Residente Junior.") 

    # 6. Salida Final (Resumen)
    print(f"\n--- RESUMEN FINAL ---")
    print(f"¡El hospital cuenta con [seniors] Especialistas Senior y  {juniors} Residentes junior! ¡Sistema listo para operar!")

def sistema_biblioteca():
    stock_actual = 120
    historial_prestamos = 0
    
    
    print("\n¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Libros disponibles")
        print("2. Realizar pr+estamo")
        print("3. Devolver préstamo")
        print("4. Historial de préstamo")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

            if opcion == input(f"Cantidad actual de libros disponibles: {stock_actual}")

            elif opcion == "2":
        try:
        
            cantidad = int(input("Ingrese cantidad de libros a prestar:"))
            if 0 < cantidad <= stock_actual:
                stock_actual -= cantidad
                historial_préstamo += cantidad
                print("Préstamo registrado exitosamente.")
            else:
                print("Error: Cantidad no válida o supera la capacidad máxima (120).")
        except ValueError:
            print("Error : Debe ingresar un número entero.")

            elif opcion == "3":
        try:
            cantidad = int(input("Ingrese cantidad de Libros a devolver:"))
            if cantidad > 0 and (stock_actual + cantidad) <= 120:
                  stock_actual += cantidad
                  historial_prestamos += cantidad
                  print("Devolución registrada exitosamente.")
            else:
                print("Error: Cantidad no válida o supera la capacidad máxima (120).")
        except ValueError:
            print(f"Total de préstamo/devoluciones realizados en la sesión: {historia_prestamos}")

            elif opcion == "5":
            print ("Gracias por utilizar nuestro software, hasta la próxima.")
             break
            else:
                print("opcion inválida, intente de nuevo.")

    # --- MENÚ PRINCIPAL DEL ARCHIVO ---
def main():
        while True:
            print("\n=== EVALUACIÓN PARCIAL 3 ===")
            print("1. Ejercicio 1: Registro de Médicos")
            print("2. Ejercicio 2. Sistema de Biblioteca")
            print("3. Salir del programa")
            sel = input("Seleccione que ejercicio ejecutar: ")

            if sel == "1": regristrar_medicos()
            elif sel == "2": sistema_biblioteca()
            elif sel: print("opcion no válida.")

            if __name__ == "__main__":

    



    
                  
         


        
        
        
                                 

 



                                                    
                                            
             
        
        
            