/*
TODO:
Revisar este link: https://www.html5rocks.com/en/tutorials/cors/
En él se habla sobre como ser capaz de que los permisos de seguridad nos permitan enviar el mensaje al servidor.
Esto es necesario, porque hasta el momento, aunque en la variable dataToBeSent no se encuentra el texto que debería he probado a establecer la conexión con el servidor y me da información de que no tiene permisos para establecerla.
Investigando pone que es porque los navegadores por motivos de seguridad deniegan esos permisos y hay que hacerlo de una forma concreta, tal y como se explica en el link de arriba.
                    
Trata de readaptarlo usando lo mencionado en ese link.
*/
/*
$('document').ready(function() {
    $('input[type=submit]').click(function(a) {
        url = 'http://localhost:8080/ogame/espionage';
        // TODO: Hacer que sea capaz de coger el texto (el alert lo hace pero sin hacer nada
        var dataToBeSent = $("form").html();
        alert(dataToBeSent);
        $.ajax({
            url : url,
            data : dataToBeSent,
            success : function(response) {
                alert('Success');
            },
            error : function(request, textStatus, errorThrown) {
                alert('Something bad happened');
            }
        });
        a.preventDefault();
    });
});
*/