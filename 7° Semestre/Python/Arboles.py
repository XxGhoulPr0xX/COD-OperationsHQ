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

    def neg(self, items):
        return ['-', items[0]]

    def number(self, items):
        return float(items[0])

    def identifier(self, items):
        return items[0]

class ExpressionTree:
    def __init__(self, grammar, start='start', parser='lalr'):
        self.grammar = grammar
        self.parser = Lark(grammar, start=start, parser=parser, transformer=TreeBuilder())

    def build_tree(self, expression):
        return self.parser.parse(expression)

    def print_tree(self, tree, level=0):
        if isinstance(tree, list):
            self.print_tree(tree[0], level + 1)
            print("   " * level + str(tree[1]))
            self.print_tree(tree[2], level + 1)
        else:
            print("   " * level + str(tree))

expresion = input("Ingrese una expresión matemática: ")

grammar = '''
    ?start: sum

    ?sum: product
        | sum "+" product   -> add
        | sum "-" product   -> sub

    ?product: atom
        | product "*" atom  -> mul
        | product "/" atom  -> div

    ?atom: NUMBER          -> number
        | IDENTIFIER      -> identifier
        | "-" atom        -> neg
        | "(" sum ")"

    %import common.NUMBER
    %import common.LETTER
    %import common.WS_INLINE
    %ignore WS_INLINE

    IDENTIFIER: LETTER+
'''
expression_tree = ExpressionTree(grammar)
arbol = expression_tree.build_tree(expresion)
print("Árbol de expresiones:")
expression_tree.print_tree(arbol)
