import logging
import httpx
import datetime
import time
import json
import architectureEvaluator

url_host_modelmanagerknowledge = 'http://modelmanagerknowledge:5071'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}


def main():

    while True:
        logging.warning("Loop: " + str(datetime.datetime.today()))

        try:

            # retrieving knowledge
            response = httpx.get(
                f"{url_host_modelmanagerknowledge}/getknowledge", headers=headers)
            currentKnowledge = response.json()

            isOk = architectureEvaluator.isArchitectureOK(
                currentKnowledge)

            if isOk:
                logging.warning("Archirecture is OK.")
                time.sleep(10)
                continue
            else:
                logging.error("Archirecture is not OK.")

        except httpx.RequestError as exc:
            logging.error(exc)
            time.sleep(10)
            continue

        time.sleep(10)


if __name__ == '__main__':
    main()
