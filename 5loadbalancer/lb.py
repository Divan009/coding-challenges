import socket

LB_HOST = 'localhost'
LB_PORT = 8081
BACKEND_HOST = 'localhost'
BACKEND_PORT = 8082

def load_balancer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as lb_sock:
        lb_sock.bind((LB_HOST, LB_PORT))
        lb_sock.listen()
        print('Load balancer listening on port 8081')

        while True:
            conn, addr = lb_sock.accept()
            with conn:
                print(f'Received request from {addr}')
                data = conn.recv(1024)
                print(data.decode('utf-8'))

                # Forward the request to the backend server
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as be_sock:
                    be_sock.connect((BACKEND_HOST, BACKEND_PORT))
                    be_sock.sendall(data)

                    # Receive response from backend
                    response = be_sock.recv(1024)
                    print('Response from server:')
                    print(response.decode('utf-8'))

                    # Forward the backend response to the client
                    conn.sendall(response)

if __name__ == '__main__':
    load_balancer()