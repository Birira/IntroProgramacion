'''
Desarrollaremos un sistema de facturas en python, utilizando POO.
Para esto, crearemos dos clases, la clase factura y la clase archivador. La clase archivador almacenará todas las facturas del mes.
La clase factura tiene las propiedades: Folio, Glosa, Monto. El folio es un numero entero arbitrario, la glosa es una descripción de 
lo adquirido, y el Monto es el valor.
La clase archivador tendrá un nombre del archivo de facturas (como por ejemplo "Facturas de Junio") y una lista donde 
se almacenarán las facturas. La clase archivador debe tener los métodos AgregarFactura() que recibe un objeto de la clase Factura 
como argumento; MostrarFacturas() que muestra un informe de todas las facturas; y el método EliminarFactura(glosa) que recibe una 
glosa y elimina la factura con la glosa indicada.
'''
class Factura:
    def __init__(self, folio,nombre, monto):
        self.folio = folio
        self.glosa = nombre
        self.monto = monto
    
    def __str__(self):
        return f"{self.folio} \t {self.glosa} \t {self.monto}"

class Archivador:
    def __init__(self, mes):
        self.mes = mes
        self.lista = []

    def __str__(self):
        return f"{self.lista} tiene {len(self.lista)} facturas"

    def AgregarFactura(self, Factura):
        self.lista.append(Factura)
    def MostrarFactura(self):
        for f in range(len(self.lista)):
            print(self.lista[f])

    def Eliminar(self, glosa):
        for f in range(len(self.lista)):
            if self.lista[f].glosa == glosa:
                del self.lista[f]
                return True
    
if __name__ == "__main__" : 
  arc = Archivador("Facturas Junio")
  f1 = Factura(9868969, "Compra mercaderia", 9999999)

  arc.AgregarFactura(f1) # agrego la factura f1
  arc.AgregarFactura(Factura(87268726, "Compra auto", 9829222) )
  arc.AgregarFactura(Factura(982769282, "Computador", 333333))
  arc.MostrarFactura()

  print(" Despues de elimianr\n\n")
  arc.Eliminar("Compra auto")
  arc.MostrarFactura()




