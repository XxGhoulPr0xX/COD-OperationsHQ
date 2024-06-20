import java.util.*;

class Triple {
    public String operation;
    public String operand1;
    public String operand2;
    public String result;

    public Triple(String operation, String operand1, String operand2, String result) {
        this.operation = operation;
        this.operand1 = operand1;
        this.operand2 = operand2;
        this.result = result;
    }

    public String toString() {
        //String triple=operand1 + ", " + operand2 + ", " + operation;
        String Cuadropolos=result+","+ operand1 + ", " + operand2 + ", " + operation;
        return "Cuadropolo "+Cuadropolos;
    }
}

public class Triplets {
    public Triplets() {
        super();
    }

    private static int tempVarCount = 1;

    public static List<Triple> generateTriples(String expression) {
        Stack<String> operators = new Stack<>();
        Stack<String> operands = new Stack<>();
        List<Triple> triples = new ArrayList<>();

        String[] tokens = expression.split(" ");

        for (String token : tokens) {
            if (isOperator(token)) {
                while (!operators.isEmpty() && precedence(token) <= precedence(operators.peek())) {
                    String operator = operators.pop();
                    String operand2 = operands.pop();
                    String operand1 = operands.pop();
                    String result = "Temp" + tempVarCount++;
                    Triple triple = new Triple(operator, operand1, operand2, result);
                    triples.add(triple);
                    operands.push(result);
                }
                operators.push(token);
            } else {
                operands.push(token);
            }
        }
        while (!operators.isEmpty()) {
            String operator = operators.pop();
            String operand2 = operands.pop();
            String operand1 = operands.pop();
            String result = "Temp" + tempVarCount++;
            Triple triple = new Triple(operator, operand1, operand2, result);
            triples.add(triple);
            operands.push(result);
        }
        return triples;
    }
    public static boolean isOperator(String token) {
        return token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/");
    }
    public static int precedence(String operator) {
        if (operator.equals("+") || operator.equals("-")) {
            return 1;
        } else if (operator.equals("*") || operator.equals("/")) {
            return 2;
        } else {
            return 0;
        }
    }

    public static void main(String[] args) {
        String expression = "3 + (5 * 2) - (4 / 2)";
        List<Triple> triples = generateTriples(expression);
        System.out.println(expression);
        System.out.println("Cuadroplos generados:");
        for (int i = 0; i < triples.size(); i++) {
            System.out.println(triples.get(i));
        }
    }
}

