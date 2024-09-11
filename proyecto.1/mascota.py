#from historial_medico import HistorialMedico
from conexion10 import BaseDatos
import re

class Mascota:
    def __init__(
            self,
            codigo_mascota: int = None,
            nombre: str = None,
            especie: str = None,
            sexo: str = None, 
            raza: str = None,
            edad: float = None,
            peso: float = None,
            usuario: int = None,
            historial_medico= None
            ):
        self.__codigo_mascota = codigo_mascota        
        self.__nombre = nombre
        self.__especie = especie
        self.__sexo = sexo
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__usuario = usuario
        self.__historial_medico = historial_medico if historial_medico is not None else []


    # GET y SET


    def get_codigo_mascota(self):
        return self.__codigo_mascota



    def set_codigo_mascota(self):
        while True:
            try:
                codigo_mascota = int(input('Escriba el código de la mascota: '))
                if (1 <= codigo_mascota <= 1000000000):
                    self.__codigo_mascota = codigo_mascota  # Cambiado de self.__codigo a self.__codigo_mascota
                    break
                else:
                    print('El número debe estar entre 1 y 1000000000')
            except ValueError:
                print('El código debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue

    def get_nombre(self):
        return self.__nombre



    def set_nombre(self):
        while True:
            try:
                nombre = input('Nombre de la mascota: ')
                if len(nombre)>3:
                    self.__nombre = nombre
                    break
                else:
                    print('Nombre incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue



    def get_especie(self):
        return self.__especie


    
    def set_especie(self):
        while True:
            try:
                especie = input('Especie de la mascota (gato, perro...): ')
                if 3 < len(especie) <= 50:
                    self.__especie = especie
                    break
                else:
                    print('Datos incorrectos. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
            
    def get_sexo(self):
        return self.__sexo
    
    def set_sexo(self):
        while True:
            try:
                sexo = input('Genero de la mascota (hembra, macho): ')
                if sexo.lower() in ['hembra','macho']:
                    self.__sexo = sexo
                    break
                else:
                    print('Genero incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue


    def get_raza(self):
        return self.__raza
    


    def set_raza(self):
        while True:
            try:
                raza = input('Raza de la mascota: ')
                # Verificar que solo contenga letras y espacios y que la longitud esté entre 3 y 30 caracteres
                if re.match(r'^[A-Za-z\s]{3,30}$', raza):
                    self.__raza = raza
                    break
                else:
                    print('Datos de raza incorrectos. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue


    
    def get_edad(self):
        return self.__edad



    def set_edad(self):
        while True:
            try:
                edad = float(input('Edad de la mascota (años): '))
                if 0 < edad <= 80.0:
                    self.__edad = edad
                    break
                else:
                    print('Edad no válida')
            except ValueError:
                print('Edad acepta solo números.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue                



    def get_peso(self):
        return self.__peso



    def set_peso(self):
        while True:
            try:
                peso = float(input('Peso en kg: '))
                if (0.1 < peso <= 1000.0):
                    self.__peso = peso
                    break
                else:
                    print('Peso no válido')
            except ValueError:
                print('El peso acepta solo números')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue                 



    def get_usuario(self):
        return self.__usuario



    def set_usuario(self):
        while True:
            try:
                usuario = int(input('Id usuario: '))
                if (0 < usuario <= 1000000000):
                    self.__usuario = usuario
                    break
                else:
                    print('Usuario no válido')
            except ValueError:
                print('Solo se admiten números')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue    



    def get_historial(self):
        return self.__historial_medico



    def agregar_historial_medico(self, entrada: str):
        self.__historial_medico.append(entrada)



    def capturar_datos(self):
            self.set_codigo_mascota()
            self.set_nombre()
            self.set_especie()
            self.set_sexo()
            self.set_raza()
            self.set_edad()
            self.set_peso()
            self.set_usuario()



    def registrar_mascota(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            cursor_mascota = conexion.cursor()
            cursor_mascota.callproc('CrearMascota', [ 
                self.get_codigo_mascota(),
                self.get_nombre(),
                self.get_especie(),
                self.get_sexo(),
                self.get_raza(),
                self.get_edad(),
                self.get_peso(),
                self.get_usuario()
            ])
            conexion.commit()
        print('Mascota registrada correctamente...')
        if conexion:
            BaseDatos.desconectar()



    def buscar_mascota(self, codigo_mascota=None):
        if codigo_mascota is None:
            self.get_codigo()
            codigo_mascota = self.__codigo
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('BuscarMascota', [codigo_mascota])
                print('Búsqueda de mascota completada.')
                for result in cursor_mascota.stored_results():
                    fila = result.fetchone()
                    while fila is not None:
                        print('Resultado:') # Si encontró  datos los imprime
                        print('**********************************************************************************************')
                        print("\033[;36m" +
                                f"| Codigo          :{fila[0]:<20}   | Nombre           :{fila[1]}  \n" +
                                f"| Especie         :{fila[2]:<20}   | Raza             :{fila[3]}  \n" +
                                f"| Edad            :{fila[4]:<20}   | Peso             :{fila[5]}  \n" +
                                f"| Id_usuario      :{fila[6]:<20}  "
                                '\033[0;m')
                        print('**********************************************************************************************')
                        return fila
                    fila = result.fetchall()
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                BaseDatos.desconectar()
        return None



    def actualizar_mascota(self, codigo_mascota):
        conexion = BaseDatos.conectar()
        mascota_encontrada = self.buscar_mascota(codigo_mascota)
        if mascota_encontrada:
            try:
                print('Escriba los nuevos datos de la mascota: ')
                self.set_nombre()
                self.set_especie()
                self.set_sexo()
                self.set_raza()
                self.set_edad()
                self.set_peso()
                
                nuevo_nombre = self.get_nombre()
                nueva_especie = self.get_especie()
                nuevo_sexo = self.get_sexo()
                nueva_raza = self.get_raza()
                nueva_edad = self.get_edad()
                nuevo_peso = self.get_peso()
                
                print(f'Código: {codigo_mascota}')
                print(f'Nuevo nombre: {nuevo_nombre}')
                print(f'Nueva especie: {nueva_especie}')
                print(f'Nuevo genero: {nuevo_sexo}')
                print(f'Nueva raza: {nueva_raza}')
                print(f'Nueva edad: {nueva_edad}')
                print(f'Nuevo peso: {nuevo_peso}')

                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('ActualizarMascota', [
                    codigo_mascota,
                    nuevo_nombre,
                    nueva_especie,
                    nuevo_sexo,
                    nueva_raza,
                    nueva_edad,
                    nuevo_peso
                ])
                conexion.commit()
                cursor_mascota.close()
                print('Mascota actualizada')
            except Exception as error:
                print(f'Error al actualizar la mascota: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()
        else:
            print('Mascota no encontrada. Intente otra vez')



    def buscar_mascotas(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('BuscarMascotas') 
                print('Listado de todas las mascotas completado.')
                mascota_encontrada = False
                for result in cursor_mascota.stored_results():
                    filas = result.fetchall()
                    if filas:
                        mascota_encontrada = True
                        for datos in filas:
                            print('Resultado:')
                            print('****************************************************************************************************')
                            print("\033[;36m" +
                                f"| Codigo          :{datos[0]:<20}   | Nombre           :{datos[1]}  \n" +
                                f"| Especie         :{datos[2]:<20}   | Raza             :{datos[3]}  \n" +
                                f"| Edad            :{datos[4]:<20}   | Peso             :{datos[5]}  \n" +
                                f"| Id_usuario      :{datos[6]:<20}  "
                                '\033[0;m')
                            print('****************************************************************************************************')
                    else:
                        print('No se encontraron resultados.')
                if not mascota_encontrada:
                    print("No se encontró el servicio proporcionado.")
            except Exception as e:
                print(f'Error al buscar servicio: {e}')
            finally:
                BaseDatos.desconectar()
        return None   
                    
    def buscar_mascota_por_nombre(self, nombre_mascota=None):
        if nombre_mascota is None:
            self.set_nombre()
            nombre_mascota = self.__nombre
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('BuscarMascotaNombre', [nombre_mascota])
                print('Búsqueda de mascota completada.')
                mascota_encontrada = False
                for result in cursor_mascota.stored_results():
                    filas = result.fetchall()
                    if filas:
                        mascota_encontrada = True
                        for datos in filas:
                            print('Resultado:')
                            print('****************************************************************************************************')
                            print("\033[;36m" +
                                f"| Codigo          :{datos[0]:<20}   | Nombre           :{datos[1]}  \n" +
                                f"| Especie         :{datos[2]:<20}   | Raza             :{datos[3]}  \n" +
                                f"| Edad            :{datos[4]:<20}   | Peso             :{datos[5]}  \n" +
                                f"| Id_usuario      :{datos[6]:<20}  "
                                '\033[0;m')
                            print('****************************************************************************************************')
                    else:
                        print('No se encontraron resultados.')
                if not mascota_encontrada:
                    print("No se encontró el servicio proporcionado.")
            except Exception as e:
                print(f'Error al buscar servicio: {e}')
            finally:
                BaseDatos.desconectar()
        return None
        

    def eliminar_mascota(self, codigo_mascota):
        conexion = BaseDatos.conectar()
        mascota_encontrada = self.buscar_mascota(codigo_mascota)
        if mascota_encontrada:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('EliminarMascota', [codigo_mascota])
                conexion.commit()
                cursor_mascota.close()
                print('Mascota eliminada')
            except Exception as error:
                print(f'Error al eliminar la mascota: {error}. Intente de nuevo')
            finally:
                BaseDatos.desconectar()

