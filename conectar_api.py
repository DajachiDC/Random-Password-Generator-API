import requests

URL = "https://random-password-generator-api-qa1j.onrender.com/api/password"

# Puedes cambiar los parametros según quieras
parametros = {
    "length": "50",         # 10, 50, 43, etc
    "numbers": "false",     # true o false
    "symbols": "false"      # true o false
}

response = requests.get(URL, params=parametros)
contrasena = response.json()["password"]

print(f"Contraseña Generada: {contrasena}")