
import socket
import threading

HOST = input("Server address (press Enter for 127.0.0.1): ").strip()
if not HOST:
    HOST = "127.0.0.1"

PORT = 12345


def receive_messages(sock):
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                print("\nServer disconnected.")
                break
            print(data.decode("utf-8"), end="", flush=True)
    except OSError:
        pass


def start_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((HOST, PORT))
        print("Connected to chat server.")

        threading.Thread(
            target=receive_messages,
            args=(sock,),
            daemon=True
        ).start()

        username = input()
        sock.sendall((username + "\n").encode("utf-8"))

        print("Chat started. Type /quit to leave.")

        while True:
            message = input()
            sock.sendall((message + "\n").encode("utf-8"))

            if message.strip().lower() == "/quit":
                break

    except ConnectionRefusedError:
        print("Cannot connect. Start the server first.")
    except (ConnectionError, OSError):
        print("Connection closed.")
    except KeyboardInterrupt:
        print("\nLeaving chat.")
    finally:
        sock.close()


if __name__ == "__main__":
    start_client()
