var fromLogin = document.getElementById('fromLogin'); //Obtenemos el formulario 

//Vamos a esuchar cuando se realice el evento ON SUBMIT
fromLogin.onsubmit = function(event){
    event.preventDefault();// Previene el comportoamiento por default de mi formulario 

    //Creamos una variable con todos los datos del formulario
    var formulario = new FormData(fromLogin)
    /*
    formulario = {
        'email' = 'yanisagamez@gmail.com'
        password = '12345678'
    }
    */
    fetch('/login',{method:'POST', body: formulario} )
    .then(response => response.json())
    .then(data => {
        console.log(data)

        if(data.message == 'Correcto'){
            window.location.href = '/dashboard'
        }
        var mensajeAlerta = document.getElementById('mensajeAlerta') //El elemento con identificador mensajeAlerta
        mensajeAlerta.innerText = data.message;
        mensajeAlerta.classList.add('alert');
        mensajeAlerta.classList.add('alert-danger');
    
    });
}

var registerForm = document.getElementById('registerForm');
registerForm.onsubmit = function(ev){
    ev.preventDefault();

    var formulario = new FormData(registerForm)
    fetch('/register', {method: 'POST', body:formulario })
    .then(response => response.json())
    .then(data => {
        console.log(data)

        if(data.mensaje == 'Correcto'){
            window.location.href = '/dashboard'
        }
        var alertMessage = document.getElementById('alertMessage') //El elemento con identificador mensajeAlerta
        alertMessage.innerText = data.mensaje;
        alertMessage.classList.add('alert');
        alertMessage.classList.add('alert-danger');
    
    });
}