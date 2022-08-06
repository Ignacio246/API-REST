function login(token){
    token = JSON.parse(token);
    sessionStorage.setItem("token", token.token);

    var request = new XMLHttpRequest();
    request.open('GET', 'https://8000-ignacio246-apirest-gznbfv3i6l3.ws-us59.gitpod.io/users/', true);
    request.setRequestHeader("Autorization", "Bearer " + token.token);
    request.setRequestHeader("Content-Type","application/json");
    request.setRequestHeader("Accept","application/json");

    request.onload = () =>{
        const status = request.status;
        console.log("Status: " + status);

        if(status == 200){
            json = JSON.parse(request.responseText);
            sessionStorage.setItem("token",token);
            window.location.replace("/bienvenida.html");
        }
    };

    request.send();

}

function getToken(){
    let email = document.getElementById("email");
    let password = document.getElementById("password");
    let payload = {
        "email" : email.value,
        "password" : password.value
    }

    console.log("email: " + email.value);
    console.log("password: " + password.value);
    console.log(payload);

    var request = new XMLHttpRequest();
    request.open('GET', 'https://8000-ignacio246-apirest-gznbfv3i6l3.ws-us59.gitpod.io/users/token/',true);
    request.setRequestHeader("Autorization", "Basic " + btoa(email.value + ":" + password.value));
    request.setRequestHeader("Content-Type","application/json");
    request.setRequestHeader("Accept","application/json");

    request.onload = () => {
        const status = request.status;

        if (status === 200){
            login(request.responseText);
        }
    }

    request.send();
}