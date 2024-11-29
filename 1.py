#sistema de reservas para
#un restaurante

class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.disponible = True
        
class Reserva:
    def __init__(self, cliente, mesa, fecha, hora):
        self.cliente = cliente
        self.mesa = mesa
        self.fecha = fecha
        self.hora = hora


class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesas = []
        self.reservas = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)

    def hacer_reserva(self, cliente, fecha, hora):
        for mesa in self.mesas:
            if mesa.disponible:
                reserva = Reserva(cliente, mesa, fecha, hora)
                self.reservas.append(reserva)
                mesa.disponible = False
                return reserva
        return None

    def cancelar_reserva(self, reserva):
        if reserva in self.reservas:
            reserva.mesa.disponible = True
            self.reservas.remove(reserva)

#el nombre del restaurante
REST = Restaurante("el comino")

#agregar mesas al restaurante
REST.agregar_mesa(Mesa(1,4))
REST.agregar_mesa(Mesa(5,8))
REST.agregar_mesa(Mesa(4,7))

#este es el cliente 
CLI = Cliente("este es su nombre: Luis Patersini", "este es su numero: 04128225279")

#crear reserva
RE = REST.hacer_reserva(CLI, "10-11.2006", "20:00" )
if RE:
    print(f"Reserva realizada para {RE.cliente.nombre} en la mesa {RE.mesa.numero}")
else:
    print("No hay mesas disponibles.")
    
    # Cancelar reserva
REST.cancelar_reserva(RE)
print("Reserva cancelada.")




