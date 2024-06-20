from lark import Lark, Transformer

class TreeBuilder(Transformer):
    def add(self, items):
        return ['+', items[0], items[1]]

    def sub(self, items):
        return ['-', items[0], items[1]]

    def mul(self, items):
        return ['*', items[0], items[1]]

    def div(self, items):
        return ['/', items[0], items[1]]
    
    def pow(self, items):  # Método para manejar la potencia
        return ['^', items[0], items[1]]
    
    def sqrt(self, items):  # Método para manejar la raíz cuadrada
        return ['sqrt', items[0],items[1]]

    def neg(self, items):
        return ['-', items[0],items[1]]

    def number(self, items):
        return float(items[0])

    def identifier(self, items):
        return items[0]

class ExpressionTree:
    def __init__(self, start='start', parser='lalr'):
        self.grammar = '''
            ?start: sum

            ?sum: product
                | sum "+" product   -> add
                | sum "-" product   -> sub

            ?product: power
                | product "*" power  -> mul
                | product "/" power  -> div

            ?power: atom
                | atom "^" power  -> pow
                | atom "sqrt" power   -> sqrt

            ?atom: NUMBER          -> number
                | IDENTIFIER      -> identifier
                | "-" atom        -> neg
                | "(" sum ")"
                | "[" sum "]"
                | "{" sum "}"

            %import common.NUMBER
            %import common.LETTER
            %import common.WS_INLINE
            %ignore WS_INLINE

            SQRT: "sqrt"

            IDENTIFIER: LETTER+
        '''
        self.parser = Lark(self.grammar, start=start, parser=parser, transformer=TreeBuilder())

    def build_tree(self, expression):
        return self.parser.parse(expression)

    def print_tree(self, tree, level=0):
        if isinstance(tree, list):
            self.print_tree(tree[0], level + 1)
            print("   " * level + str(tree[1]))
            self.print_tree(tree[2], level + 1)
        else:
            print("   " * level + str(tree))

