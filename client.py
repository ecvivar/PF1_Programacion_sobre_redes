import socket

# Configuración del servidor
HOST = "localhost"  # Dirección del servidor
PORT = 5000         # Puerto de comunicación


def conectar_servidor():
    """Crea el socket y establece la conexión con el servidor."""
    try:
        # Intentar crear socket TCP/IP y conectar
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))  # Conexión al servidor

        print(f"Conectado al servidor en {HOST}:{PORT}")

        return s

    except ConnectionRefusedError:
        print(
            f"No se pudo conectar al servidor en {HOST}:{PORT}. "
            "Asegúrate de que el servidor esté en ejecución."
        )

    except OSError as e:
        print(f"Error de socket: {e}")

    return None


def enviar_mensajes(s):
    """Permite ingresar y enviar múltiples mensajes al servidor."""
    while True:
        # Enviar mensaje al servidor
        mensaje = input("Escribe tu mensaje (o 'éxito' para salir): ")
        s.sendall(mensaje.encode("utf-8"))

        # Finalizar la conexión si el usuario escribe "éxito"
        if mensaje.lower() == "éxito":
            break

        try:
            # Recibir respuesta del servidor
            respuesta = s.recv(1024).decode("utf-8")
            print(f"Servidor respondió: {respuesta}")

        except Exception as e:
            print(f"Error al recibir respuesta del servidor: {e}")
            break


def main():
    """Función principal del cliente."""
    s = conectar_servidor()

    if s is None:
        return

    try:
        enviar_mensajes(s)

    finally:
        s.close()


# Ejecutar el cliente
if __name__ == "__main__":
    main()