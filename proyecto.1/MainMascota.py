from os import system
from mascota import Mascota

class MenuMascota:
    @staticmethod
    def main():
        try:
            while True:
                mascota = Mascota()
                print('***************MENU MASCOTAS********************')
                print('1 - Registrar nueva mascota')
                print('2 - Buscar una mascota')
                print('3 - Actualizar mascota')
                print('4 - Eliminar una mascota')
                print('5 - Listar todas las mascotas')
                print('6 - Salir del sistema')
                print('***************MENU MASCOTAS********************')

                while True:
                    try:
                        opcion = int(input('Seleccione una opción: '))
                        if 1 <= opcion <= 6:
                            break
                        else:
                            print('Opción no válida. Ingrese un número entre 1 y 6.')
                    except ValueError:
                        print('Opción no válida. Ingrese un número.')

                if opcion == 6:
                    print('Gracias por usar nuestra app.')
                    break
                
                elif opcion == 1:
                    system("cls")
                    print('                   1. REGISTRAR MASCOTA                        ')
                    print('****************************************************************')
                    mascota.registrar_mascota()
                    system("pause")
                    system("cls")
                    
                elif opcion == 2:
                    system('cls')
                    while True:
                        print('                      2.BUSCAR MASCOTAS                         ')
                        print('****************************************************************')
                        opciones = [
                            "Buscar por código de mascota",
                            "Buscar por nombre de mascota",
                            "Volver al menú principal"
                        ]
                        
                        print("\nSelecciona una opción:")
                        for i, opcion_menu in enumerate(opciones, 1):
                            print(f"{i}. {opcion_menu}")
                        
                        opcion_busqueda = input("Ingrese el número de la opción deseada: ")
                        
                        if opcion_busqueda == '1':
                            print('             CONSULTAR MASCOTAS POR CODIGO                      ')
                            print('****************************************************************')
                            try:
                                codigo = int(input("Ingresa el código de la mascota: "))
                                resultados = mascota.buscar_mascota(codigo)
                                if resultados is None:
                                    print("No se encontraron mascotas.")
                            except ValueError:
                                print("Error: El código debe ser un número entero.")
                            system("pause")
                        elif opcion_busqueda == '2':
                            print('               CONSULTAR MASCOTA POR NOMBRE                    ')
                            print('****************************************************************')
                            nombre = input("Ingresa el nombre de la mascota: ")
                            resultados = mascota.buscar_mascota_por_nombre(nombre)
                            if not resultados:
                                print("No se encontraron mascotas.")
                            system("pause")
                        elif opcion_busqueda == '3':
                            break
                        else:
                            print("Opción no válida. Intente de nuevo.")
                            system("pause")
                        
                        system("cls")
                        
                elif opcion == 3:
                    system('cls')
                    print('                    3.ACTUALIZAR MASCOTA                       ')
                    print('****************************************************************')
                    try:
                        codigo = int(input("Escriba el código de la mascota a actualizar: "))
                        mascota.actualizar_mascota(codigo)
                    except ValueError:
                        print("Error: El código debe ser un número entero.")
                    system("pause")

                elif opcion == 4:
                    system('cls')
                    print('         4. Eliminar Mascotas')
                    print('****************************************************************')
                    try:
                        codigo = int(input("Escriba el código de la mascota a eliminar: "))
                        mascota.eliminar_mascota(codigo)
                    except ValueError:
                        print("Error: El código debe ser un número entero.")
                    system("pause")
                    system("cls")
                    
                elif opcion == 5:
                    system('cls')
                    print('              5.LISTAR TODAS LAS MASCOTAS                      ')
                    print('****************************************************************')
                    mascotas = mascota.buscar_mascotas()
                    if mascotas:
                        for masc in mascotas:
                            print(f"Código: {masc.get_codigo()}, Nombre: {masc.get_nombre()}, Especie: {masc.get_especie()}")
                    else:
                        print("No se encontraron mascotas.")
                    system("pause")
                    system("cls")
        
        except KeyboardInterrupt:
            print('El usuario ha cancelado la ejecución, por favor continúe')
        except Exception as error:
            print(f'Ha ocurrido un error no codificado: {error}')
        finally:
            print('Intente de nuevo')

if __name__ == "__main__":
    MenuMascota.main()