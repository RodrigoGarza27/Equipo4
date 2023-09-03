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
