const lengthSlider = document.getElementById("length")
const lengthValue = document.getElementById("lengthValue")


lengthSlider.oninput = () => {

    lengthValue.innerText = lengthSlider.value

}


function generarPassword() {

    let length = document.getElementById("length").value

    let numbers = document.getElementById("numbers").checked

    let symbols = document.getElementById("symbols").checked


    fetch(
        `/api/password?length=${length}&numbers=${numbers}&symbols=${symbols}`
    )

        .then((res) => res.json())

        .then((data) => {

            document.getElementById("password").value = data.password

            evaluarSeguridad(data.password)

        })

}


function copiar() {

    let pass = document.getElementById("password")

    pass.select()

    document.execCommand("copy")

    alert("Contraseña copiada")

}


function evaluarSeguridad(password) {

    let barra = document.getElementById("barra")

    let score = password.length


    if (score < 12) {

        barra.style.width = "30%"

    }

    else if (score < 20) {

        barra.style.width = "60%"

    }

    else {

        barra.style.width = "100%"

    }

}