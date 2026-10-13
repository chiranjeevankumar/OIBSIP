
import socket
import threading
from datetime import datetime

HOST = "0.0.0.0"
PORT = 12345
clients = {}
lock = threading.Lock()


def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def send_message(sock, message):
    try:
        sock.sendall((message + "\n").encode("utf-8"))
    except OSError:
        pass


def broadcast(message):
    with lock:
        connected = list(clients.keys())

    for sock in connected:
        send_message(sock, message)


def handle_client(sock, address):
    username = None
    reader = None

    try:
        sock.sendall(b"Enter your username: ")
        reader = sock.makefile("r", encoding="utf-8")
        username = reader.readline().strip()

        if not username:
            return

        with lock:
            clients[sock] = username

        print(f"[{timestamp()}] {username} connected from {address}")
        broadcast(f"[{timestamp()}] {username} joined the chat!")
        send_message(sock, f"[{timestamp()}] Welcome, {username}!")

        for line in reader:
            message = line.strip()

            if message.lower() == "/quit":
                break

            if message:
                formatted = f"[{timestamp()}] {username}: {message}"
                print(formatted)
                broadcast(formatted)

    except (ConnectionError, OSError):
        pass
    finally:
        if username:
            with lock:
                clients.pop(sock, None)

            notice = f"[{timestamp()}] {username} disconnected."
            print(notice)
            broadcast(notice)

        try:
            if reader:
                reader.close()
        except OSError:
            pass

        try:
            sock.close()
        except OSError:
            pass


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Chat server listening on port {PORT}...")

        while True:
            sock, address = server.accept()
            threading.Thread(
                target=handle_client,
                args=(sock, address),
                daemon=True
            ).start()

    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        server.close()


if __name__ == "__main__":
    start_server()
