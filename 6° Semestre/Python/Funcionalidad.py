class Funcionalidad:
    def __init__(self):
        self.def_value = 0  # Declarar 'def' como variable de instancia
    # Valida el código de la tarjeta prepago
    def validarCodigo(self, codigo):
        if len(codigo) != 6:
            return False  # El código debe tener exactamente 6 caracteres
        a = codigo[0]
        bc = codigo[1:3]
        d = codigo[3]
        self.def_value = int(codigo[3:6])

        if (a in ['2', '4', '6']) and (d in ['0', '1']):
            if bc in ['10', '20', '40', '86', '78', '30']:
                return True
        elif (a in ['0', '1', '3']) and (d == '0'):
            return True
        return False

    # Realiza la recarga del saldo
    def recargarSaldo(self,codigo, monto_recarga):
        resultado = codigo
        if self.validarCodigo(codigo):
            if self.def_value <= 199:
                nuevo_saldo = self.def_value + monto_recarga
                if nuevo_saldo <= 199:
                    resultado = codigo[:3] + f"{nuevo_saldo:03d}"
                else:
                    resultado = codigo[:3] + "199"  # Limitar el saldo máximo a 199
            if resultado[0] in ['0', '1', '3']:
                resultado = '2' + resultado[1:]
        else:
            resultado = "CODIGO INVALIDO"
        return resultado