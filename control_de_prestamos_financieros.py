class Prestamo:
    def __init__(self, cliente, monto, cuotas):
        self.cliente = cliente
        self.monto = monto
        self.cuotas = cuotas
        self.cuota_valor = monto / cuotas
        self.saldo = monto
        self.pagos_realizados = 0
    def registrar_pago(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            self.pagos_realizados += cantidad
            print(f"pago de ${cantidad} registrado, saldo pendiente: ${self.saldo:.2f}\n")
        else:
            print("el pago excede el saldo pendiente.\n")
    def mostrar_estado(self):
        print(f"cliente: {self.cliente}")
        print(f"monto total: ${self.monto:.2f}")
        print(f"cuotas: {self.cuotas} | valor por cuota: ${self.cuota_valor:.2f}")
        print(f"pagos realizados: ${self.pagos_realizados:.2f} | saldo pendiente: ${self.saldo:.2f}\n")
def menu():
    prestamos = []
    while True:
        print("control de prestamos financieros")
        print("1. registrar nuevo prestamo")
        print("2. registrar pago")
        print("3. consultar estado de préstamo")
        print("4. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            cliente = input("nombre del cliente: ")
            try:
                monto = float(input("monto del prestamo: "))
                cuotas = int(input("numero de cuotas: "))
                prestamo = Prestamo(cliente, monto, cuotas)
                prestamos.append(prestamo)
                print(f"prestamo registrado para {cliente}.\n")
            except ValueError:
                print("monto o cuotas invalidas.\n")
        elif opcion == "2":
            cliente = input("nombre del cliente: ")
            prestamo = next((p for p in prestamos if p.cliente.lower() == cliente.lower()), None)
            if prestamo:
                try:
                    cantidad = float(input("monto a pagar: "))
                    prestamo.registrar_pago(cantidad)
                except ValueError:
                    print("monto invalido.\n")
            else:
                print("prestamo no encontrado.\n")
        elif opcion == "3":
            cliente = input("nombre del cliente: ")
            prestamo = next((p for p in prestamos if p.cliente.lower() == cliente.lower()), None)
            if prestamo:
                prestamo.mostrar_estado()
            else:
                print("prestamo no encontrado.\n")
        elif opcion == "4":
            print("saliendo del sistema...")
            break
        else:
            print("opcion invalida.\n")
menu()