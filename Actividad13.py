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
                nombre = input("Ingrese el nombre del repartidor: ")
                existe = False
                for repartidor in self.repartidores:
                    if repartidor._nombre.upper() == nombre.upper():
                        existe = True
                        break
                if existe:
                    print("Error, este repartidor ya existe. Ingrese un nombre diferente.")
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
        def busqueda_secuencial(lista, objetivo):
            for i in range(len(lista)):
                if lista[i].upper() == objetivo.upper():
                    return i
            return None
        buscar = input("Ingrese el nombre del repartidor que desea buscar: ")
        repas = [repartidor._nombre for repartidor in self.repartidores]
        lupa = busqueda_secuencial(repas, buscar)
        if lupa is not None:
            encontrado = self.repartidores[lupa]
            print(f"Repartidor: {encontrado._nombre} | {encontrado._paquetes} paquetes | Zona: {encontrado._zona}")
        else:
            print("Repartidor no encontrado o inexistente")
    def listado(self):
        print("------Lista de repartidores------")
        for repartidor in self.repartidores:
            print(repartidor)
        print("------Lista descendente------")
        ordenado = self.quick_sort(self.repartidores)
        for repartidor in ordenado:
            print(repartidor)
    def estadisticas(self):
        total_paquetes = 0
        promedio = 0
        for repartidor in self.repartidores:
            total_paquetes += repartidor._paquetes
            promedio = total_paquetes / (len(repartidor._nombre)-1)
        print("------ESTADISTICAS------")
        print(f"El total de paquetes entregados es de: {total_paquetes}")
        print(f"El promedio de paquetes entregados es de: {promedio}")
def main():
    empresa = Empresa()
    empresa.registrar_repartidor()
    while True:
        print("======MENÚ======")
        print("1. Listado de repartidores.")
        print("2. Buscar repartidor.")
        print("3. Estadisticas.")
        print("4. Salir.")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                empresa.listado()
            case "2":
                empresa.buscar_repartidor()
            case "3":
                empresa.estadisticas()
            case "4":
                print("Saliendo del programa...")
                exit()
            case _:
                print("Error, no existe la operacion")
if __name__ == "__main__":
    main()
