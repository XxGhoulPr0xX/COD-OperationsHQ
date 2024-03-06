class EPJS {
    constructor() {

    }
    HolaMundo() {
        return document.write("Hola Mundo");
    }
    SumaSimple() {
        var a = 10;
        var b = 5;
        var resultado = a + b;
        return alert("La suma de " + a + " + " + b + " es: " + resultado);
    }
    Presentacion() {
        alert("A continuacion hago una presentacion mia");
        var name = "Javier";
        var edad = "21";
        this.SumaSimple();
        return alert("Soy " + name + " y tengo " + edad + " años");
    }
    Ejercicio4() {
        const a = "Hola";
        let b = "mundo";
        document.write("La constante a contiene la cadena: " + a);
        document.write("<br>")
        document.write("La variable b contiene la candena: " + b);
        document.write("<br>")
        document.write(a +" "+ b);
    }
    IngresarUsuario() {
        let dato, resultado;
        dato = window.prompt("ola");
        resultado = "Hola como estas " + dato;
        document.write(resultado);

    }
    ParseInt() {
        let dato, num;
        dato = window.prompt("Introduce un numero: ");
        num = parseInt(dato);
        num = num * 2;
        document.write("<p>Los números por teclado son Strings que tienen que convertise. La instrucción parseInt transforma un string a int</p>")
        document.write("Resultado: " + num);
    }
    OperacionMulti() {
        var num1 = 2;
        var num2 = 8;
        var num3 = num1 * num2;
        document.write("La constante a contiene la cadena: " + num1);
        document.write("<br>")
        document.write("La variable b contiene la candena: " + num2);
        document.write("<br>")
        document.write("el producto de a * b es: " + num3);
    }
    SumarPorUsuario(){
        let dato1,dato2;
        dato1=parseInt(window.prompt("Introduce un primer número: "));
        dato2=parseInt(window.prompt("Introduce un segundo número: "));
        let resultado=dato1+dato2;
        document.write("La suma es: "+resultado);
    }
    SumaCondicional(){
        var numMa="";
        this.SumarPorUsuario();
        if(this.dato1>this.dato2){
            numMa="el primero";
        }
        else{
            numMa="el segundo";
        }
        document.write("<br>")
        document.write("El mayor es: "+numMa);
    }
};
