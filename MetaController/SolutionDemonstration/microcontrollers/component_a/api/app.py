import logging
import time
import datetime

url_host = 'http://<service>:<port>'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}


def main():

    while True:
        logging.warning("Loop - Component a - " +
                        str(datetime.datetime.today()))

        time.sleep(10)


if __name__ == '__main__':
    main()
