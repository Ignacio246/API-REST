function getClientes(){
    var query = window.location.search.substring(1);
    console.log("Query: " + query)

    //Conectar con el backend
    const request = new XMLHttpRequest();


    request.open('GET', 'https://8000-ignacio246-apirest-gznbfv3i6l3.ws-us53.gitpod.io/clientes/', true);
    request.setRequestHeader("Accept", "application/json");

    const  tabla   = document.getElementById("tabla_clientes");
    const  thead   = document.getElementById("thead_clientes");

    request.onload = () => {
        const response = request.responseText;
        const json = JSON.parse(response);
        console.log("Response " + response);
        console.log("JSON: " +typeof json);

        var tbody = document.getElementById("tbody_clientes");

        for(let row=0; row<json.length; row++){
            var tr = document.createElement('tr');

            var td_detalle = document.createElement("td")
            var td_id_clientes = document.createElement('td');
            var td_nombre = document.createElement('td');
            var td_email = document.createElement('td');

            td_detalle.innerHTML = "<a href='\get_cliente.html?"+json[row].id_clientes+"'>Detalle</a>";
            td_id_clientes.innerHTML = json[row].id_clientes;
            td_nombre.innerHTML = json[row].nombre;
            td_email.innerHTML = json[row].email;

            tr.appendChild(td_detalle);
            tr.appendChild(td_id_clientes);
            tr.appendChild(td_nombre);
            tr.appendChild(td_email);

            tbody.appendChild(tr);

        }
        tabla.appendChild(tbody);
    
    };
    request.send();
};