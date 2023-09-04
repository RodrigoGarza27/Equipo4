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
            




