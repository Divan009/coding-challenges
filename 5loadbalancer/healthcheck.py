import requests
from settings import PORTS
import logging
import time
from collections import defaultdict 

port_list = PORTS
session = requests.Session()
port_status = defaultdict(bool)

logging.basicConfig(
    level=logging.INFO,
    filename='health_check.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)


def health_check(port_list):

    global port_status
    
    for port in port_list:

        url = f'http://localhost:{port}'
        try:
            response = session.get(url)

            print(response.status_code)
            if response.status_code != 200:
                logging.error(f"HC failed for {port}. Status Code: {response.status_code}")
                port_status[port] = False
            else:
                port_status[port] = True
                
                logging.info(f"HC successful for {port}. Status Code: {response.status_code}")

        except Exception as e:
            print(e)
            port_status[port] = False
            logging.error(f"HC failed for {port}. Status: {e}")


if __name__ == '__main__':
    import argparse
    

    msg = 'Health check'
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument('--tries', default=10, help='add a period')
    args = parser.parse_args()


    while True:
        health_check(port_list)
        print(port_status)
        time.sleep(int(args.tries))