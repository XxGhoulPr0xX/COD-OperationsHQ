import PreInPost
import Arboles

if __name__ == "__main__":
    expresion = "{[3+5^10]}^(x-y*2)"
    alpha = PreInPost.GeneracionCodigoIntermedio()
    beta = Arboles.ExpressionTree()
    arbol = beta.build_tree(expresion)
    print("Árbol de expresiones:")
    beta.print_tree(arbol)
    print("Expresión: ",expresion,"\nPreorden: ",alpha.prefijo(expresion),"\nInorden: ",alpha.infijo(expresion),"\nPostorden: ",alpha.postfijo(expresion))

