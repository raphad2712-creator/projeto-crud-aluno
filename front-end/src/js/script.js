function enviarDados() {
    const nome = document.getElementById("nome").value
    const email = document.getElementById("email").value

    fetch("192.168.1.133 3000", {
        nome, email
    })

}