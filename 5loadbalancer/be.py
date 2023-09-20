import socket

HOST = 'localhost'
PORT = 8082

def backend_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f'Backend server listening on {HOST}:{PORT}')

        while True:
            conn, addr = s.accept()
            with conn:
                print(f'Received request from {addr}')
                data = conn.recv(1024)
                print(data.decode('utf-8'))
                conn.sendall(b'HTTP/1.1 200 OK\n\nHello From Backend Server')

if __name__ == '__main__':
    backend_server()