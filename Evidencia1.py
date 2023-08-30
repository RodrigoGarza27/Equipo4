import datetime
class Servicio:
  def _init_(self, nombre, costo):
    self.nombre=nombre
    self.costo=costo
    class Nota:
      folio_counter=1
      def _init_(self, cliente, servicios):
        self.folio=nota.folio_counter
        Nota.folio_counter +=1
        self.cliente=cliente
        self.servicios=servicios
        self.monto_pagar=sum(servicio.costo
