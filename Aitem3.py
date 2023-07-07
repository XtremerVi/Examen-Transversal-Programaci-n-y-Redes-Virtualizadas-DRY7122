import hashlib
import sqlite3
from getpass import getpass


def generar_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


def verificar_password(password, hash_password):
    return generar_hash(password) == hash_password


conn = sqlite3.connect('usuarios.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (nombre TEXT, password_hash TEXT)''')


usuarios = [
    ('Vicente', generar_hash('cisco123!')),
    ('Cain', generar_hash('cisco123!')),
    ('IAugusto', generar_hash('cisco123!'))
]
c.executemany('INSERT INTO usuarios VALUES (?, ?)', usuarios)


conn.commit()
conn.close()


usuario = input("Ingrese su nombre de usuario: ")
contraseña = getpass("Ingrese su contraseña: ")


conn = sqlite3.connect('usuarios.db')
c = conn.cursor()


c.execute("SELECT password_hash FROM usuarios WHERE nombre = ?", (usuario,))
resultado = c.fetchone()

if resultado:
    hash_guardado = resultado[0]
    if verificar_password(contraseña, hash_guardado):
        print("Inicio de sesión exitoso")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no encontrado")


conn.close()