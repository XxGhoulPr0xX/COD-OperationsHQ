document.addEventListener('DOMContentLoaded', function () {
    alert('¡Bienvenido! Al examen de la unidad 1 de Programacion Web.');
    
    var mainContainer = document.querySelector('.Main');
    mainContainer.addEventListener('mouseover', function (event) {
        var hoveredElement = event.target;
        if (mainContainer.contains(hoveredElement) && hasAcceptedClass(hoveredElement)) {
            console.log('Elemento seleccionado:', hoveredElement.textContent);
            hoveredElement.style.transform = 'scale(2.5)';
            flashWhite(hoveredElement);
        }
    });

    mainContainer.addEventListener('mouseout', function (event) {
        var hoveredElement = event.target;
        if (mainContainer.contains(hoveredElement) && hasAcceptedClass(hoveredElement)) {
            hoveredElement.style.transform = 'scale(1)';
            clearInterval(hoveredElement.flashInterval);
            hoveredElement.style.backgroundColor = ''; // Restablecer el color de fondo
        }
    });

    function hasAcceptedClass(element) {
        var acceptedClasses = [
            'elementAlkaliMetal',
            'elementAlkalineEarthMetal',
            'elementLanthanide',
            'elementActinide',
            'elementTransition',
            'elementOther',
            'elementHalogens',
            'elementNobleGases',
            'elementMetalloids',
            'NoMetal',
            'MetalBloqueP'
        ];
        for (var i = 0; i < acceptedClasses.length; i++) {
            if (element.classList.contains(acceptedClasses[i])) {
                return true;
            }
        }
        return false;
    }

    function flashWhite(element) {
        var flashColor = 'white';
        var flashInterval = setInterval(function () {
            if (flashColor === 'white') {
                flashColor = 'black';
            } else if (flashColor === 'black') {
                flashColor = 'white';
            } else {
                flashColor = 'black';
            }
            element.style.backgroundColor = flashColor;
        }, 200); // Cambia de color cada 200 milisegundos
        element.flashInterval = flashInterval; // Guardar el intervalo en la propiedad flashInterval del elemento
    }

    mainContainer.addEventListener('click', function (event) {
        var clickedElement = event.target;
        if (mainContainer.contains(clickedElement) && hasAcceptedClass(clickedElement)) {
            var info = clickedElement.dataset.info;
            if (info) {
                alert('Información del elemento:\n' + info);
            }
        }
    });
});
