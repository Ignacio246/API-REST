function getClientes(){
    var query = window.location.search.substring(1);
    console.log("Query: " + query)

    //Conectar con el backend
    const request = new XMLHttpRequest();


    request.open('GET', 'http://127.0.0.1:8000/clientes/', true);
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

            var td_get = document.createElement("td");
            var td_update = document.createElement("td");
            var td_delete = document.createElement("td");
            var td_id_clientes = document.createElement('td');
            var td_nombre = document.createElement('td');
            var td_email = document.createElement('td');

            td_get.innerHTML = "<a href='/get_cliente.html?"+json[row].id_clientes+"'>Detalle</a>";
            td_update.innerHTML = "<a href='/update_cliente.html?"+json[row].id_clientes+"'>Actualizar</a>";
            td_delete.innerHTML = "<a href='/delete_cliente.html?"+json[row].id_clientes+"'>Borrar</a>";
            td_id_clientes.innerHTML = json[row].id_clientes;
            td_nombre.innerHTML = json[row].nombre;
            td_email.innerHTML = json[row].email;

            tr.appendChild(td_get);
            tr.appendChild(td_update);
            tr.appendChild(td_delete);
            tr.appendChild(td_id_clientes);
            tr.appendChild(td_nombre);
            tr.appendChild(td_email);

            tbody.appendChild(tr);

        }
        tabla.appendChild(tbody);
    
    };
    request.send();
};