import re

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class AnalizadorLexico:
    def __init__(self):
        self.patrones = [
            (r'[0-9]+', 'ENTERO'),
            (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFICADOR'),
            (r'\+', 'SUMA'),
            (r'-', 'RESTA'),
            (r'\*', 'MULTIPLICACION'),
            (r'/', 'DIVISION')
        ]

    def analizar(self, entrada):
        # Eliminar espacios en blanco
        entrada = entrada.replace(" ", "")
        tokens = []
        while entrada:
            for patron, etiqueta in self.patrones:
                match = re.match(patron, entrada)
                if match:
                    valor = match.group(0)
                    tokens.append(Token(etiqueta, valor))
                    entrada = entrada[len(valor):]
                    break
            else:
                raise ValueError(f"No se pudo analizar: {entrada}")
        return tokens

analizador = AnalizadorLexico()
entrada = input()
tokens = analizador.analizar(entrada)
for token in tokens:
    print(f"Tipo: {token.tipo}, Valor: {token.valor}")
