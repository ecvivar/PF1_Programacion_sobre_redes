# TP - Chat Cliente-Servidor con Sockets y SQLite

## Descripción

Este proyecto implementa un sistema básico de comunicación **cliente-servidor** desarrollado en Python utilizando **sockets TCP/IP** y una base de datos **SQLite**.

El servidor recibe mensajes enviados por el cliente, registra cada mensaje en una base de datos y devuelve una confirmación indicando la fecha y hora en que fue recibido.

El cliente permite establecer la conexión con el servidor y enviar múltiples mensajes hasta que el usuario ingresa la palabra `éxito`.

## Objetivos

* Implementar comunicación cliente-servidor mediante sockets TCP/IP.
* Configurar un servidor que escuche conexiones en `localhost:5000`.
* Enviar y recibir mensajes entre cliente y servidor.
* Almacenar los mensajes recibidos en una base de datos SQLite.
* Registrar la fecha y hora de cada mensaje.
* Registrar la dirección IP del cliente.
* Implementar manejo básico de errores.
* Aplicar modularización mediante funciones.

## Tecnologías utilizadas

* **Python 3**
* **Socket TCP/IP**
* **SQLite**
* Módulo `socket`
* Módulo `sqlite3`
* Módulo `datetime`

## Estructura del proyecto

```text
PFO1/
│
├── server.py
├── client.py
├── chat.db
└── README.md
```

> El archivo `chat.db` se genera automáticamente al ejecutar el servidor por primera vez.

## Funcionamiento

### Servidor

El servidor:

1. Inicializa la base de datos SQLite.
2. Crea la tabla `mensajes` si todavía no existe.
3. Inicializa un socket TCP/IP.
4. Escucha conexiones en `localhost:5000`.
5. Acepta la conexión de un cliente.
6. Recibe los mensajes enviados.
7. Guarda cada mensaje en la base de datos.
8. Envía una confirmación al cliente.
9. Finaliza la conexión cuando recibe `éxito`.

### Cliente

El cliente:

1. Crea un socket TCP/IP.
2. Se conecta al servidor en `localhost:5000`.
3. Permite ingresar mensajes desde la consola.
4. Envía cada mensaje al servidor.
5. Muestra la respuesta recibida.
6. Finaliza cuando el usuario ingresa `éxito`.

## Base de datos

El servidor utiliza SQLite y crea automáticamente la tabla `mensajes`:

| Campo         | Tipo    | Descripción                     |
| ------------- | ------- | ------------------------------- |
| `id`          | INTEGER | Identificador único del mensaje |
| `contenido`   | TEXT    | Contenido del mensaje           |
| `fecha_envio` | TEXT    | Fecha y hora en que se recibió  |
| `ip_cliente`  | TEXT    | Dirección IP del cliente        |

El campo `id` utiliza `AUTOINCREMENT` para generar un identificador automáticamente.

## Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/ecvivar/PF1_Programacion_sobre_redes.git
```

Ingresar a la carpeta del proyecto:

```bash
cd PF1_Programacion_sobre_redes
```

### 2. Ejecutar el servidor

Abrir una terminal y ejecutar:

```bash
python server.py
```

Debería aparecer:

```text
Conexión a la base de datos establecida.
Servidor escuchando en localhost:5000...
```

### 3. Ejecutar el cliente

Abrir una segunda terminal, ubicarse en la carpeta del proyecto y ejecutar:

```bash
python client.py
```

Debería aparecer:

```text
Conectado al servidor en localhost:5000
Escribe tu mensaje (o 'éxito' para salir):
```

### 4. Enviar mensajes

Por ejemplo:

```text
Escribe tu mensaje (o 'éxito' para salir): Hola
Servidor respondió: Mensaje recibido: 2026-09-20 19:30:15

Escribe tu mensaje (o 'éxito' para salir): Segundo mensaje
Servidor respondió: Mensaje recibido: 2026-09-20 19:30:25
```

Para finalizar:

```text
Escribe tu mensaje (o 'éxito' para salir): éxito
```

## Manejo de errores

El proyecto contempla errores relacionados con:

* Conexión con la base de datos SQLite.
* Creación y configuración del socket.
* Puerto ocupado.
* Conexión rechazada porque el servidor no está iniciado.
* Errores durante el procesamiento de mensajes.
* Errores al recibir respuestas del servidor.

## Modularización

El servidor está dividido en funciones según las responsabilidades principales:

```text
inicializar_base_datos()
inicializar_socket()
guardar_mensaje()
aceptar_conexion_y_recibir_mensajes()
main()
```

El cliente también utiliza funciones para separar sus responsabilidades:

```text
conectar_servidor()
enviar_mensajes()
main()
```

Esta organización permite separar las distintas tareas del programa y facilita su comprensión y mantenimiento.

## Prueba local

Para realizar la prueba se deben utilizar dos terminales:

```text
Terminal 1                 Terminal 2
-----------                -----------
server.py                  client.py
    │                          │
    │◄────── conexión ─────────│
    │                          │
    │◄────── mensaje ──────────│
    │                          │
    │────── respuesta ────────►│
    │                          │
    │◄────── mensaje ──────────│
    │                          │
    │────── respuesta ────────►│
```

## Autor

**Cristian Vivar**