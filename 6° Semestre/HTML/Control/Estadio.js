class Estadio{
    constructor(){
        this.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; // Letras del alfabeto
        this.Asientos=[
            [
                ['A',1,2,3,4,5,6],
                ['B',1,2,3,4,5,6],
                ['C',1,2,3,4,5,6],
                ['D',1,2,3,4,5,6],
                ['E',1,2,3,4,5,6],
                ['F',1,2,3,4,5,6]
            ],
            [
                ['A',13,14,15,16,17,18],
                ['B',13,14,15,16,17,18],
                ['C',13,14,15,16,17,18],
                ['D',13,14,15,16,17,18],
                ['E',13,14,15,16,17,18],
                ['F',13,14,15,16,17,18],
            ],
            [
                ['G',7,8,9,10,11,12],
                ['H',7,8,9,10,11,12],
                ['I',7,8,9,10,11,12],
                ['J',7,8,9,10,11,12],
                ['K',7,8,9,10,11,12],
                ['L',7,8,9,10,11,12]
            ]
        ]
    }
    createCircles()
    {
        var container = document.getElementById("circleContainer");
        container.innerHTML = '';
        this.CrearBotones(container)
        this.Circulos(container)
    }
    Circulos(container){
        for (var i = 0; i <= 11; i++) {
            var circleRow = document.createElement("div");
            circleRow.className = "circle-row";
            var letter = document.createElement("div");
            letter.className = "letter";
            letter.innerText = this.alphabet[i];
            circleRow.appendChild(letter);
            // Agregar los círculos de colores
            for (var j = 0; j <= 17; j++) {
                var circle = document.createElement("div");
                if (j < 1) {
                    circle.className = "circle yellow";
                } else if (j >= 1 && j <= 3) {
                    circle.className = "circle orange";
                } else if (j >= 4 && j <= 5) {
                    circle.className = "circle blue";
                } else if (j >= 6 && j <= 11) {
                    circle.className = "square-with-border";
                } else if (j >= 12 && j <= 13) {
                    circle.className = "circle blue";
                } else if (j >= 14 && j <= 16) {
                    circle.className = "circle orange";
                } else if (j === 17) {
                    circle.className = "circle yellow";
                }
                if (i >= 0 && i <= 5) {
                    if (j < 6 || (j >= 12)) {
                        // Agregar números solo si j está en el rango 0-5, 12 o 13
                        var hola = document.createElement("div");
                        hola.className = "number";
                        hola.innerText = (j < 6 || j >= 12) ? j + 1 : ''; // Comenzando desde 1
                        circle.appendChild(hola);
                    }
                }
                if (i >= 6 && i <= 11) {
                    if (j >= 6 && j <= 11) {
                        // Agregar números solo si j está en el rango 6-11
                        var hola = document.createElement("div");
                        hola.className = "number";
                        hola.innerText = j + 1; // Comenzando desde 1
                        circle.appendChild(hola);
                    }
                    circle.className = "square-with-border";
                    if (j >= 6 && j <= 7) {
                        circle.className = "circle blue";
                    }
                    if (j >= 8 && j <= 10) {
                        circle.className = "circle orange";
                    }
                    if (j === 11) {
                        circle.className = "circle yellow";
                    }
                }
                circleRow.appendChild(circle);
            }
            container.appendChild(circleRow);
        }
        // Crear el botón "Comprar"
        var btnComprar = document.createElement("button");
        btnComprar.innerText = "Comprar";
        btnComprar.className = "comprar-button";
        btnComprar.disabled = true; // Deshabilita el botón al principio
        btnComprar.onclick = this.ComprarAsientos.bind(this); // Asignar el evento click
        container.appendChild(btnComprar);
    }
    CrearBotones(container)
    {
           // Agregar "Número de asientos que desea comprar" y una caja de texto
            var lblCantidad = document.createElement("div");
            lblCantidad.className = "seats-text";
            lblCantidad.innerText = "Cantidad de Asientos que desea comprar";
            container.appendChild(lblCantidad);

            var txtCantidad = document.createElement("input");
            txtCantidad.type = "text";
            txtCantidad.className = "seats-input";
            container.appendChild(txtCantidad);

            // Agregar "Categoría" y un menú desplegable
            var lblCategoria = document.createElement("div");
            lblCategoria.className = "category-text";
            lblCategoria.innerText = "Categoría";
            container.appendChild(lblCategoria);

            var lbCategoria = document.createElement("select");
            lbCategoria.className = "category-select";

           // Opciones de categoría
            var categories = ["Azul 150", "Naranja 100", "Amarrillo 70"];
            for (var k = 0; k < categories.length; k++) {
                var option = document.createElement("option");
                option.value = categories[k];
                option.text = categories[k];
                lbCategoria.appendChild(option);
            }
            container.appendChild(lbCategoria);

            var lblLugares = document.createElement("div");
            lblLugares.className = "seats-tex1t";
            lblLugares.innerText = "Lugares que desea comprar";
            container.appendChild(lblLugares);

            var txtLugares = document.createElement("input");
            txtLugares.type = "text";
            txtLugares.className = "seats-input";
            container.appendChild(txtLugares);
            txtCantidad.oninput = this.Checar.bind(this);
            lbCategoria.oninput = this.Checar.bind(this);
            txtLugares.oninput = this.Checar.bind(this);
    }
    ComprarAsientos()
    {
        const cantidad = document.querySelector('.seats-input').value;
        const tipo = document.querySelector('.category-select').value;
        alert(`Has comprado ${cantidad} asientos de la categoría ${tipo}`);
    }
    Checar() {
        var txtCantidad = document.querySelector('.seats-input');
        var lbCategoria = document.querySelector('.category-select');
        var txtLugares = document.querySelector('.seats-input');
        var btnComprar = document.querySelector('.comprar-button');

        // Habilita el botón "Comprar" si todos los campos están completos
        if (txtCantidad.value && lbCategoria.value && txtLugares.value) {
            btnComprar.disabled = false;
            var elemento = Asientos[0][0][0] + Asientos[0][0][1];
            console.log(elemento); // Esto imprimirá "A1"
        } else {
            btnComprar.disabled = true;
        }
    }
}
