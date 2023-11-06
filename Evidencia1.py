import random
import datetime
import csv

class Servicio:
    def _init_(self, descripcion, costo):
        self.descripcion = descripcion
        self.costo = costo

class Nota:
    def _init_(self, cliente, fecha, detalle):
        self.folio = random.randint(1000, 9999)
        self.cliente = cliente
        self.fecha = fecha
        self.detalle = detalle
        self.cancelada = False

    def calcular_costo_total(self):
        return sum([servicio.costo for servicio in self.detalle])

class TallerMecanico:
    def _init_(self):
        self.notas = []
        self.load_data()

    def load_data(self):
        try:
            with open("taller_mecanico_data.csv", mode="r", newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    detalle = [Servicio(descripcion, float(costo)) for descripcion, costo in zip(row['descripciones'].split('|'), row['costos'].split('|'))]
                    nota = Nota(row['cliente'], datetime.datetime.strptime(row['fecha'], '%Y-%m-%d %H:%M:%S'), detalle)
                    nota.cancelada = row['cancelada'] == 'True'
                    self.notas.append(nota)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open("taller_mecanico_data.csv", mode="w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['cliente', 'fecha', 'descripciones', 'costos', 'cancelada'])
            writer.writeheader()
            for nota in self.notas:
                descripciones = '|'.join(servicio.descripcion for servicio in nota.detalle)
                costos = '|'.join(str(servicio.costo) for servicio in nota.detalle)
                writer.writerow({'cliente': nota.cliente, 'fecha': nota.fecha.strftime('%Y-%m-%d %H:%M:%S'), 'descripciones': descripciones, 'costos': costos, 'cancelada': str(nota.cancelada)})

    def crear_nota_servicio(self, cliente):
        detalle = []
        print("\nAgregar servicios a la nota de servicio:")
        while True:
            descripcion = input("Ingrese la descripción del servicio: ")
            costo = float(input("Ingrese el costo del servicio: "))
            detalle.append(Servicio(descripcion, costo))
            if input("¿Desea agregar otro servicio? (S/N): ").lower() != 's':
                break
        nota = Nota(cliente, datetime.datetime.now(), detalle)
        self.notas.append(nota)
        print("Nota de servicio creada exitosamente.")
        self.save_data()

    def listar_notas(self):
        for nota in self.notas:
            print("\nFolio:", nota.folio)
            print("Cliente:", nota.cliente)
            print("Fecha:", nota.fecha.strftime('%Y-%m-%d %H:%M:%S'))
            print("Costo total:", nota.calcular_costo_total())
            print("Detalle:")
            for servicio in nota.detalle:
                print("\tDescripción:", servicio.descripcion)
                print("\tCosto:", servicio.costo)

    def consultar_por_periodo(self):
        fecha_inicio = datetime.datetime.strptime(input("Ingrese la fecha de inicio (YYYY-MM-DD): "), '%Y-%m-%d')
        fecha_fin = datetime.datetime.strptime(input("Ingrese la fecha de fin (YYYY-MM-DD): "), '%Y-%m-%d')
        notas_encontradas = [nota for nota in self.notas if fecha_inicio <= nota.fecha <= fecha_fin]
        if notas_encontradas:
            for nota in notas_encontradas:
                print("\nFolio:", nota.folio)
                print("Cliente:", nota.cliente)
                print("Fecha:", nota.fecha.strftime('%Y-%m-%d %H:%M:%S'))
                print("Costo total:", nota.calcular_costo_total())
        else:
            print("No se encontraron notas de servicio en el período especificado.")

    def consultar_por_folio(self, folio):
        nota_encontrada = next((nota for nota in self.notas if nota.folio == folio), None)
        if nota_encontrada:
            print("\nFolio:", nota_encontrada.folio)
            print("Cliente:", nota_encontrada.cliente)
            print("Fecha:", nota_encontrada.fecha.strftime('%Y-%m-%d %H:%M:%S'))
            print("Costo total:", nota_encontrada.calcular_costo_total())
            print("Detalle:")
            for servicio in nota_encontrada.detalle:
                print("\tDescripción:", servicio.descripcion)
                print("\tCosto:", servicio.costo)
        else:
            print("No se encontró ninguna nota de servicio con el folio especificado.")

    def recuperar_nota_cancelada(self, folio):
        nota_encontrada = next((nota for nota in self.notas if nota.folio == folio), None)
        if nota_encontrada and nota_encontrada.cancelada:
            nota_encontrada.cancelada = False
            print("Nota de servicio recuperada exitosamente.")
            self.save_data()
        else:
            print("No se encontró ninguna nota de servicio cancelada con el folio especificado.")

def main():
    taller = TallerMecanico()
    while True:
        print("\nMenú de opciones:")
        print("1. Crear nota de servicio")
        print("2. Listar todas las notas de servicio")
        print("3. Consultar notas de servicio por período")
        print("4. Consultar nota de servicio por folio")
        print("5. Recuperar nota de servicio cancelada")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            cliente = input("Ingrese el nombre del cliente: ")
            taller.crear_nota_servicio(cliente)
        elif opcion == '2':
            taller.listar_notas()
        elif opcion == '3':
            taller.consultar_por_periodo()
        elif opcion == '4':
            folio = int(input("Ingrese el folio de la nota de servicio: "))
            taller.consultar_por_folio(folio)
        elif opcion == '5':
            folio = int(input("Ingrese el folio de la nota de servicio: "))
            taller.recuperar_nota_cancelada(folio)
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if _name_ == "_main_":
    main()
