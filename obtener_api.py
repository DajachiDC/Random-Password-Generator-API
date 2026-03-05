import requests

# URL de tu API
url = "http://127.0.0.1:5000/api/password"

# parámetros de la API
parametros = {
    "length": 50,
    "numbers": "false",
    "symbols": "false"
}

# hacer petición a la API
respuesta = requests.get(url)

# convertir respuesta a JSON
datos = respuesta.json()

# mostrar contraseña
print("Contraseña generada:")
print(datos["password"])