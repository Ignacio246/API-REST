function deleteCliente(){
    //var id_clientes = window.location.search.substring(1);
    let id_clientes = document.getElementById("id_clientes");
    let nombre = document.getElementById("nombre");
    let email = document.getElementById("email");

    let payload = {
        "id_clientes": id_clientes.value,
        "nombre": nombre.value,
        "email": email.value
    }

    console.log("id_clientes: " + id_clientes.value);
    console.log("nombre: " + nombre.value);
    console.log("email: " + email.value);

    var request = new XMLHttpRequest();
    request.open('DELETE', 'https://8000-ignacio246-apirest-gznbfv3i6l3.ws-us53.gitpod.io/clientes/'+id_clientes, true);
    request.setRequestHeader("Content-Type","application/json");
    request.setRequestHeader("Accept","application/json");

    request.onload = () =>{
        const response = request.responseText;
        const json = JSON.parse(response);
        const status = request.status;

        console.log("Response " + response);
        console.log("Json " +  json);
        console.log("Status: " + status);

        if(status == 200){
            alert(json.message);
            window.location.replace("/get_clientes.html");
        }
    };

    request.send(JSON.stringify(payload));

};