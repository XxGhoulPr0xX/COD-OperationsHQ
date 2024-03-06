
var boton1 = document.getElementById("boton1");
var boton2 = document.getElementById("boton2");
var demo = document.getElementById("demo");
var demo2 = document.getElementById("demo2");


boton1.addEventListener("click", function () {

    demo.textContent = "Hiciste click!!!!!!!!!!!!!!";
});

boton2.addEventListener("click", function () {
    var nombre = prompt("Por favor, introduce tu nombre:");
    demo2.textContent = "Tu nombre es " + nombre;
});
function sumar() {

    var num1 = parseInt(document.getElementById("num1").value);
    var num2 = parseInt(document.getElementById("num2").value);


    var suma = num1 + num2;


    document.getElementById("resultado").textContent = "La suma es: " + suma;
}
function nombrexd() {
    var name = String(document.getElementById("nombre").value);
    document.getElementById("mimi").textContent = "Tu nombre es: " + name;
}