class Repartidor:
    def __init__(self, nombre, paquetes, zona):
        self._nombre = nombre
        self._paquetes = paquetes
        self._zona = zona
    def __str__(self):
        return f" Repartidor: {self._nombre} | Paquetes entregados:{self._paquetes}  | Zona: {self._zona}"
class Empresa:
    def __init__(self):
        self.repartidores = []
    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x._paquetes < pivote._paquetes]
        iguales = [x for x in lista if x._paquetes == pivote._paquetes]
        mayores = [x for x in lista[1:] if x._paquetes > pivote._paquetes]
        return self.quick_sort(mayores) + iguales + self.quick_sort(menores)
    def registrar_repartidor(self):
        cont = int(input("Ingrese cuantos repartidores trabajaron hoy: "))
        for i in range(cont):
            print(f"Repartidor #{i + 1}")
            while True:
                nombre = input("Ingrese el nombre del repartidor: ").upper()
                for repartidor in self.repartidores:
                    if repartidor.nombre.upper() == nombre.upper():
                        print("Error, este repartidor ya existe")
                    else:
                        break
            while True:
                paquetes_entregados = int(input("Ingrese la cantidad de paquetes entregados: "))
                if paquetes_entregados < 0:
                    print("Error, los paquetes entregados deben de ser números positivos")
                else:
                    break
            while True:
                zona = input("Ingrese la zona asignada: ")
                if not zona:
                    print("Error,campo requerido")
                else:
                    break
            nuevo_repartidor = Repartidor(nombre, paquetes_entregados, zona)
            self.repartidores.append(nuevo_repartidor)
            print(f"Repartidor: {nombre} agregado exitosamente")
    def buscar_repartidor(self):
        buscar = input("Ingrese el nombre del repartidor que desea buscar: ")
        for repartidor in self.repartidores:
            if repartidor.nombre.upper() == buscar.upper():
                print(repartidor)
                return
            else:
                print("Error, el repartidor no existe")
