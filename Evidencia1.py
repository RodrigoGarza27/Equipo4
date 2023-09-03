import random
import datetime

class TallerMecanico:
    def __init__(self):
        self.notas = []
    
    def generar_folio(self):
        # Generar un folio aleatorio único
        folio = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8))
        while any(nota['folio'] == folio for nota in self.notas):
            folio = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8))
        return folio
    
    def crear_nota(self, cliente):
        folio = self.generar_folio()
        fecha = datetime.datetime.now()
        detalle = []
        
        while True:
            descripcion = input("Ingrese el nombre del servicio realizado (o 'fin' para terminar): ")
            if descripcion.lower() == 'fin':
                break
            costo = None
            while costo is None:
                try:
                    costo = float(input("Ingrese el costo del servicio (mayor que 0): "))
                    if costo <= 0:
                        raise ValueError
                except ValueError:
                    print("El costo debe ser un número mayor que 0.")
            detalle.append({'descripcion': descripcion, 'costo': costo})
        
        # Calcular el costo total a partir del detalle de servicios
        costo_total = sum(servicio['costo'] for servicio in detalle)
        
        nota = {
            'folio': folio,
            'cliente': cliente,
            'detalle': detalle,
            'costo_total': costo_total,
            'fecha': fecha,
            'cancelada': False
        }
        self.notas.append(nota)
        print(f"Nota creada con folio: {folio}, fecha: {fecha.strftime('%Y-%m-%d %H:%M:%S')}, cliente: {cliente}, costo total: {costo_total:.2f}")
    
    def listar_notas(self):
        if not self.notas:
            print("No hay notas registradas.")
        else:
            print("Notas registradas:")
            for nota in self.notas:
                print(f"Folio: {nota['folio']}, Cliente: {nota['cliente']}, Costo Total: {nota['costo_total']:.2f}, Fecha: {nota['fecha'].strftime('%Y-%m-%d %H:%M:%S')}")
                if nota['cancelada']:
                    print("Nota Cancelada")
                else:
                    print("Detalle de Servicios:")
                    for servicio in nota['detalle']:
                        print(f"  - Descripción: {servicio['descripcion']}, Costo: {servicio['costo']:.2f}")


if nota_recuperar:
                    print("\nDetalle de la nota cancelada a recuperar:")
                    print(f"Folio: {nota_recuperar['folio']}, Cliente: {nota_recuperar['cliente']}, Costo Total: {nota_recuperar['costo_total']:.2f}, Fecha: {nota_recuperar['fecha'].strftime('%Y-%m-%d %H:%M:%S')}")
                    print("Detalle de Servicios:")
                    for servicio in nota_recuperar['detalle']:
                        print(f"  - Descripción: {servicio['descripcion']}, Costo: {servicio['costo']:.2f}")
                    
                    confirmacion = input("¿Desea recuperar esta nota cancelada? (S/N): ")
                    if confirmacion.lower() == 's':
                        nota_recuperar['cancelada'] = False
                        print("Nota recuperada correctamente.")
                else:
                    print("El folio ingresado no corresponde a una nota cancelada.")
            else:
                print("Operación de recuperación de nota cancelada cancelada.")










# Crear una instancia del taller mecánico
taller = TallerMecanico()

while True:
    print("\nMenú:")
    print("1. Crear una nueva nota de servicio")
    print("2. Listar todas las notas de servicio")
    print("3. Consultas y Reportes")
    print("4. Recuperar una nota cancelada")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        cliente = input("Ingrese el nombre del cliente: ")
        taller.crear_nota(cliente)
    elif opcion == '2':
        taller.listar_notas()
    elif opcion == '3':
        while True:
            print("\nSubmenú de Consultas y Reportes:")
            print("1. Consulta por período")
            print("2. Consulta por folio")
            print("3. Volver al menú principal")
            
            subopcion = input("Seleccione una opción del submenú: ")
            
            if subopcion == '1':
                taller.consultar_por_periodo()
            elif subopcion == '2':
                folio_consulta = input("Ingrese el folio de la nota a consultar: ")
                taller.consultar_por_folio(folio_consulta)
            elif subopcion == '3':
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
    elif opcion == '4':
        taller.recuperar_nota_cancelada()
    elif opcion == '5':
        confirmacion_salir = input("¿Desea salir de la solución? (S/N): ")
        if confirmacion_salir.lower() == 's':
            break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")




