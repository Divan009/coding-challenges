import socket


HOST = "localhost"
PORT = 6379

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Redis Server is listening on port {PORT}")

    while True:
        conn, addr = s.accept()
        print(f"Received request from {addr}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                decoded_data = data.decode('utf-8').strip()
                print(decoded_data)
                conn.sendall(b"OK")


