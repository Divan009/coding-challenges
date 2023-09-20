import requests
from settings import PORTS
import logging
import time


port_list = PORTS
session = requests.Session()

logging.basicConfig(
    level=logging.INFO,
    filename='health_check.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

def health_check(port):
    url = f'http://localhost:{port}'
    try:
        response = session.get(url)

        print(response.status_code)
        if response.status_code != 200:
            logging.error(f"HC failed for {port}. Status Code: {response.status_code}")
            return response.status_code
        else:
            logging.info(f"HC successful for {port}. Status Code: {response.status_code}")
            return response.status_code

    except Exception as e:
        print(e)
        logging.error(f"HC failed for {port}. Status: {e}")
        return 500


if __name__ == '__main__':
    import argparse

    msg = 'Health check'
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument('--tries', default=10, help='add a period')
    args = parser.parse_args()


    while True:
        for port in port_list:
            health_check(port)
        
        time.sleep(int(args.tries))