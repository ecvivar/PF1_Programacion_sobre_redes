import socket
import sqlite3
import datetime

# Configuración del servidor
HOST = "localhost"  # Dirección del servidor
PORT = 5000         # Puerto de comunicación


def inicializar_base_datos():
    """Inicializa la base de datos SQLite y crea la tabla de mensajes."""
    try:
        # Intentar conectarse a la base de datos SQLite
        conn = sqlite3.connect("chat.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS mensajes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contenido TEXT,
        fecha_envio TEXT,
        ip_cliente TEXT
        )
        """)

        conn.commit()
        print("Conexión a la base de datos establecida.")

        return conn, cursor

    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None, None


def inicializar_socket():
    """Crea, configura y pone a escuchar el socket del servidor."""
    try:
        # Intentar crear socket TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Asociar socket a host y puerto
        s.bind((HOST, PORT))

        # Escuchar conexiones entrantes
        s.listen(1)

        print(f"Servidor escuchando en {HOST}:{PORT}...")

        return s

    except OSError as e:
        print(f"Error al crear el socket: {e}")
        return None


def guardar_mensaje(cursor, conn, mensaje, timestamp, ip_cliente):
    """Guarda un mensaje recibido en la base de datos."""
    try:
        # Guardar mensaje en la base de datos
        cursor.execute(
            "INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?, ?, ?)",
            (mensaje, timestamp, ip_cliente)
        )

        conn.commit()

    except sqlite3.Error as e:
        print(f"Error al guardar el mensaje en la base de datos: {e}")


def aceptar_conexion_y_recibir_mensajes(s, cursor, conn):
    """Acepta una conexión y recibe mensajes del cliente."""
    try:
        # Aceptar conexión entrante
        conn_cliente, addr = s.accept()

        with conn_cliente:
            print(f"Conexión establecida desde {addr}")

            while True:
                try:
                    # Recibir mensajes del cliente
                    mensaje = conn_cliente.recv(1024).decode("utf-8")

                    if not mensaje or mensaje.lower() == "éxito":
                        break

                    print(f"Cliente envió: {mensaje}")

                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Guardar mensaje en la base de datos
                    guardar_mensaje(cursor, conn, mensaje, timestamp, addr[0])

                    # Responder al cliente con confirmación
                    respuesta = f"Mensaje recibido: {timestamp}"
                    conn_cliente.sendall(respuesta.encode("utf-8"))

                except Exception as e:
                    print(f"Error al procesar el mensaje: {e}")
                    break

        print("Conexión cerrada.")

    except OSError as e:
        print(f"Error al aceptar la conexión: {e}")


def main():
    """Función principal del servidor."""
    conn, cursor = inicializar_base_datos()

    # Verificar si la base de datos pudo inicializarse correctamente
    if conn is None:
        return

    s = inicializar_socket()

    # Verificar si el socket pudo inicializarse correctamente
    if s is None:
        conn.close()
        return

    try:
        aceptar_conexion_y_recibir_mensajes(s, cursor, conn)

    finally:
        s.close()
        conn.close()


# Ejecutar el servidor
if __name__ == "__main__":
    main()