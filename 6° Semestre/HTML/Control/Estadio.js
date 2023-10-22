class Estadio{
    constructor() {
        this.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; // Letras del alfabeto
        this.circulos = []
        this.total = parseFloat(sessionStorage.getItem('total')) || 0;
        this.asientos = [];
        for (let letra = 'A'.charCodeAt(0); letra <= 'L'.charCodeAt(0); letra++) {
            for (let numero = 1; numero <= 18; numero++) {
                this.asientos.push(String.fromCharCode(letra) + numero);
            }
        }
    }

    createCircles()
    {
        var container = document.getElementById("circleContainer");
        container.innerHTML = '';
        this.CrearBotones(container);
        this.Circulos(container);
    }
    Circulos(container) {
        var estadioCreado = false;
        for (var i = 0; i <= 11; i++) {
            var circleRow = document.createElement("div");
            circleRow.className = "circle-row";
            var letter = document.createElement("div");
            letter.className = "Label";
            letter.innerText = this.alphabet[i];
            circleRow.appendChild(letter);
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
                    if (!estadioCreado) {
                        var estadio = document.createElement("img");
                        estadio.src = "estadio.png";
                        estadio.alt = "Estadio";
                        estadio.style.width = "180px";
                        estadio.style.height = "180px";
                        circle.appendChild(estadio);
                        estadioCreado = true;
                    }
                } else if (j >= 12 && j <= 13) {
                    circle.className = "circle blue";
                } else if (j >= 14 && j <= 16) {
                    circle.className = "circle orange";
                } else if (j === 17) {
                    circle.className = "circle yellow";
                }
                if (i >= 0 && i <= 5) {
                    if (j < 6 || (j >= 12)) {
                        var numeros = document.createElement("div");
                        numeros.className = "numeros";
                        numeros.innerText = (j < 6 || j >= 12) ? j + 1 : '';
                        circle.appendChild(numeros);
                    }
                }
                if (i >= 6 && i <= 11) {
                    if (j >= 6 && j <= 11) {
                        var numeros = document.createElement("div");
                        numeros.className = "numeros";
                        numeros.innerText = j + 1;
                        circle.appendChild(numeros);
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
                this.circulos.push(circle); // Agregar el círculo al arreglo
            }
            container.appendChild(circleRow);
        }

        // Crear el botón "Comprar"
        var btnComprar = document.createElement("button");
        btnComprar.innerText = "Comprar";
        btnComprar.className = "boton";
        btnComprar.onclick = this.ComprarAsientos.bind(this);
        container.appendChild(btnComprar);
    }
    CrearBotones(container)
    {
           // Agregar "Número de asientos que desea comprar" y una caja de texto
            var lblCantidad = document.createElement("div");
            lblCantidad.className = "Label";
            lblCantidad.innerText = "Cantidad de Asientos que desea comprar";
            container.appendChild(lblCantidad);

            var txtCantidad = document.createElement("input");
            txtCantidad.type = "text";
            txtCantidad.className = "txtCantidad";
            txtCantidad.min = 0; // Establecer el mínimo como 1
            txtCantidad.max = 5; // Establecer el máximo como 5
            txtCantidad.addEventListener('input', function() {
                // Utilizar una expresión regular para eliminar caracteres no numéricos
                this.value = this.value.replace(/[^0-9]/g, '');
                // Verificar si el valor está dentro del rango permitido
                if (this.value < 0) {
                    this.value = 1; // Establecer el valor mínimo si es menor que 1
                } else if (this.value > 5) {
                    this.value = 5; // Establecer el valor máximo si es mayor que 5
                }
            });
            container.appendChild(txtCantidad); // Asegúrate de que txtCantidad se adjunte al contenedor

            // Agregar "Categoría" y un menú desplegable
            var lblCategoria = document.createElement("div");
            lblCategoria.className = "Label";
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
            lblLugares.className = "Label";
            lblLugares.innerText = "Lugares que desea comprar";
            container.appendChild(lblLugares);

            var txtLugares = document.createElement("input");
            txtLugares.type = "text";
            txtLugares.className = "txtLugar";
            container.appendChild(txtLugares);
    }

    ComprarAsientos() {
        const txtCantidad = document.querySelector('.txtCantidad');
        const lbCategoria = document.querySelector('.category-select');
        const txtLugares = document.querySelector('.txtLugar');
        const cantidad = parseInt(txtCantidad.value);
        const categoria = lbCategoria.value;
        const lugares = txtLugares.value.split(",").map(lugar => lugar.trim());
    
        if (cantidad && categoria && lugares.length > 0) {
            let validCategory = true;
    
            if (categoria === "Azul 150") {
                validCategory = lugares.every(lugar => /^[A-F][56]$|^[A-F](1[34])$|^[G-L][78]$/.test(lugar));
            } else if (categoria === "Naranja 100") {
                validCategory = lugares.every(lugar => /^[A-F][234]$|^[A-F](1[567])$|^[G-L]9$|^[G-L]11$|^[G-L]10$/.test(lugar));
            } else if (categoria === "Amarrillo 70") {
                validCategory = lugares.every(lugar => /^[A-F]1$|^[A-F]18$|^[G-L]12$/.test(lugar));
            }
    
            if (validCategory) {
                // Determinar el precio por categoría
                let precioPorCategoria = 0;
    
                if (categoria === "Azul 150") {
                    precioPorCategoria = 150;
                } else if (categoria === "Naranja 100") {
                    precioPorCategoria = 100;
                } else if (categoria === "Amarrillo 70") {
                    precioPorCategoria = 70;
                }
    
                // Calcular el costo total
                const costoTotal = cantidad * precioPorCategoria;
                this.total = costoTotal + this.total;

                console.log(this.total);
                // Imprimir la lista de asientos comprados
                const listaAsientos = [];
    
                for (let lugar of lugares) {
                    listaAsientos.push(lugar);
                    for (let i = 0; i < cantidad; i++) {
                        const posicion = this.asientos.indexOf(lugar);
    
                        if (posicion !== -1) {
                            // Usar la posición para acceder al círculo correspondiente y cambiar su color
                            const circulo = this.circulos[posicion];
                            circulo.className = "circle gray";
                        }
                    }
                }
                sessionStorage.setItem('total', this.total);

                // Generar el contenido del archivo de texto
                const lista = listaAsientos.join('\n');
    
                // Crear un objeto Blob con el contenido del archivo
                const blob = new Blob(['Los asientos comprados son: \n',lista,
                '\nCon un costo total de: \n',costoTotal], { type: 'text/plain' });
                // Crear un objeto URL para el Blob
                const blobURL = URL.createObjectURL(blob);
                // Crear un enlace para descargar el archivo
                const enlaceDescarga = document.createElement('a');
                enlaceDescarga.href = blobURL;
                enlaceDescarga.download = 'Venta.txt';
                // Simular un clic en el enlace para iniciar la descarga
                enlaceDescarga.click();
            } else {
                window.confirm('Los lugares seleccionados no coinciden con la categoría.');
            }
        } else {
            window.confirm('Por favor, complete todos los campos requeridos.');
        }
    }
    actualizarTotal() {
        var totalElement = document.getElementById('total');
        var ventaTotal = this.total; // Asegúrate de que this.total tenga el valor correcto
        console.log(ventaTotal);
        totalElement.value = ventaTotal;
    }
    cargarArchivos() {
        const input = document.createElement('input');
        input.type = 'file';
        input.setAttribute('webkitdirectory', true);
        input.setAttribute('directory', true);
        input.setAttribute('multiple', true);
        input.accept = '.txt';
        input.addEventListener('change', (event) => {
            const fileList = event.target.files;
            const archivosDiv = document.querySelector('.archivos');
            archivosDiv.innerHTML = ''; // Limpiamos el contenido anterior
            for (const file of fileList) {
                if (file.type === 'text/plain') {
                    const nombreArchivo = document.createElement('p');
                    nombreArchivo.textContent = file.name;
                    archivosDiv.appendChild(nombreArchivo);
                } else {
                    console.log('El archivo seleccionado no es un archivo de texto.');
                }
            }
        });
    
        input.click();
    }
    leerArchivo(file) {
        const reader = new FileReader();
        reader.onload = (event) => {
            const contenido = event.target.result;
            console.log('Contenido del archivo:', contenido);
        };
        reader.readAsText(file);
    }
    cargarArchivos() {
        const input = document.createElement('input');
        input.type = 'file';
        input.setAttribute('webkitdirectory', true);
        input.setAttribute('directory', true);
        input.setAttribute('multiple', true);
        input.accept = '.txt';
        input.addEventListener('change', (event) => {
            const fileList = event.target.files;
            const archivosDiv = document.querySelector('.archivos');
            archivosDiv.innerHTML = ''; // Limpiamos el contenido anterior
            for (const file of fileList) {
                if (file.type === 'text/plain') {
                    const nombreArchivo = document.createElement('p');
                    nombreArchivo.textContent = file.name;
                    archivosDiv.appendChild(nombreArchivo);
                } else {
                    console.log('El archivo seleccionado no es un archivo de texto.');
                }
            }
        });
    
        input.click();
    }
    cargarArchivosDerecho() {
        const input = document.createElement('input');
        input.type = 'file';
        input.setAttribute('webkitdirectory', true);
        input.setAttribute('directory', true);
        input.setAttribute('multiple', true);
        input.accept = '.txt';
        let confirmacionHabilitada = true; // Variable de estado para habilitar la confirmación
        input.addEventListener('change', (event) => {
            const fileList = event.target.files;
            const reportesDerecho = document.querySelector('.ReportesDerecho');
            const reportesIzquierdo = document.querySelector('.ReportesIzquierdo');
            reportesDerecho.innerHTML = ''; // Limpiamos el contenido anterior
            reportesIzquierdo.innerHTML = ''; // Limpiamos el contenido anterior
            for (const file of fileList) {
                if (file.type === 'text/plain') {
                    const nombreArchivo = document.createElement('p');
                    nombreArchivo.textContent = file.name;
                    nombreArchivo.style.cursor = 'pointer';
                    nombreArchivo.style.color = 'blue';
                    nombreArchivo.addEventListener('click', () => {
                        if (confirmacionHabilitada && window.confirm(`¿Deseas eliminar "${file.name}"?`)) {
                            nombreArchivo.style.color = 'black';
                            reportesDerecho.removeChild(nombreArchivo);
                            reportesIzquierdo.appendChild(nombreArchivo);
                            confirmacionHabilitada = false;
                            setTimeout(() => {
                                confirmacionHabilitada = true;
                            }, 5000); // Habilita la confirmación después de 5 segundos
                        }
                    });
                    reportesDerecho.appendChild(nombreArchivo);
                } else {
                    console.log('El archivo seleccionado no es un archivo de texto.');
                }
            }
        });
        input.click();
    }
    leerArchivo(file) {
        const reader = new FileReader();
        reader.onload = (event) => {
            const contenido = event.target.result;
            console.log('Contenido del archivo:', contenido);
        };
        reader.readAsText(file);
    }
    cambiarTema(tema) {
        const elementosCSS = document.querySelectorAll('link[rel="stylesheet"]');
        elementosCSS.forEach(elemento => {
            if (elemento.getAttribute('href').includes('View/')) {
                // Verifica si el enlace al estilo está dentro de la carpeta "css"
                if (tema === 'tema1') {
                    elemento.setAttribute('href', 'View/Tema1.css');
                    alert("Tema seleccionado",tema);
                } else if (tema === 'tema2') {
                    elemento.setAttribute('href', 'View/Tema2.css');
                    alert("Tema seleccionado",tema);
                } else if (tema === 'tema3') {
                    elemento.setAttribute('href', 'View/Tema3.css');
                    alert("Tema seleccionado",tema);
                }
            }
        });
    }
}