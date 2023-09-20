import socket
import logging
from round_robbin import RoundRobbinLB


from utils import check_python_script_running

if check_python_script_running("health_check.py"):
    from healthcheck import port_status


LB_HOST = "localhost"
LB_PORT = 1111
BACKEND_HOST = "localhost"
BACKEND_PORT = [8003, 8001, 8002, 8004]
load_balancers = RoundRobbinLB(BACKEND_PORT)

# Create and configure logger
logging.basicConfig(
    level=logging.DEBUG,
    filename="load_balancer.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)

# def load_balancer():
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as lb_sock:
    lb_sock.bind((LB_HOST, LB_PORT))
    lb_sock.listen()
    print(f"Load balancer listening on port {LB_PORT}")
    logging.info(f"Load balancer listening on port {LB_PORT}")

    while True:
        conn, addr = lb_sock.accept()
        with conn:
            print(f"Received request from {addr}")

            logging.info(f"Received request from {addr}")
            data = conn.recv(1024)

            # Forward the request to the backend server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as be_sock:
                lb_port = load_balancers.get_next_server()
                logging.info(f"Message sent to server running in {lb_port}")

                if check_python_script_running("health_check.py"):
                    if port_status[lb_port]:
                        be_sock.connect((BACKEND_HOST, lb_port))
                        be_sock.sendall(data)
                    else:
                        continue
                else:
                    try:
                        be_sock.connect((BACKEND_HOST, lb_port))
                    except ConnectionRefusedError:
                        logging.error(f"server in port {lb_port} is not running.")
                        lb_port = load_balancers.get_next_server()
                        be_sock.connect((BACKEND_HOST, lb_port))
                        logging.info(f"Therefore, connecting to a new port {lb_port}.")
                    be_sock.sendall(data)

                # Receive response from backend
                response = be_sock.recv(1024)
                print("Response from server:")
                print(response.decode("utf-8"))

                # Forward the backend response to the client
                conn.sendall(response)
