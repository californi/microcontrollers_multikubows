import datetime
import requests
import logging
import time
import httpx

PROMETHEUS = 'http://prometheus:9090/'

url_host = 'http://cpufailuregauge:5030'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}


class CpuFailure:
    rate = 0.0


def main():

    while True:
        logging.warning("Loop: " + str(datetime.datetime.today()))

        response = requests.get(PROMETHEUS + '/api/v1/query', params={
                                'query': 'sum (rate(http_requests_total{handler="/insufficientcpu"}[30s]))'})

        results = response.json()['data']['result']

        for result in results:
            CpuFailure.rate = float('{value[1]}'.format(**result))

        data = {"name": "rate",
                "type": "failure",
                "value": CpuFailure.rate,
                "dateevent": str(datetime.datetime.today())}

        response = httpx.post(f"{url_host}/setcpufailuregauge",
                              headers=headers,
                              json=data)

        logging.warning("cpuFailureRate: " + str(CpuFailure.rate))

        time.sleep(5)


if __name__ == '__main__':
    main()
