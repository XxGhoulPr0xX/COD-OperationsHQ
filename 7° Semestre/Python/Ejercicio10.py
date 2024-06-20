""" 
    Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones 
    por las tres ventas realizadas en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
"""
class Ejercicio10:

    def calcular_comision(self, ventas):
        return ventas * 0.10  # 10% de comisión por cada venta

    def comision_de_ventas(self, ventas):
        comision_por_venta = self.calcular_comision(ventas)
        return comision_por_venta

    def total_mes(self, sueldo, ventas):
        comision_total = self.comision_de_ventas(ventas) * 3  # Comisiones por las tres ventas
        total_mes = sueldo + comision_total
        return total_mes

    def main(self, sueldo, ventas):
        comision_por_venta = self.comision_de_ventas(ventas)
        total_mes = self.total_mes(sueldo, ventas)
        return  f"El vendedor recibirá un total de ${comision_por_venta} por comisiones por cada venta realizada.\n" \
                f"El total que recibirá en el mes, considerando su sueldo base y comisiones, es de ${total_mes}\n"


if __name__ == "__main__":
    sueldo_base = float(input("Ingresa el sueldo base del vendedor: "))
    ventas_mes = float(input("Ingresa el total de ventas realizadas en el mes: "))
    alpha = Ejercicio10()
    print(alpha.main(sueldo_base, ventas_mes))
