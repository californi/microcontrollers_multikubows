import logging
import httpx
import datetime
import time
import json

url_host_failuregauge = 'http://cpufailuregauge:5030'
url_host_deploymentinfoscalabilityagauge = 'http://deploymentinfoscalabilityagauge:5050'
url_host_deploymentinfofidelityagauge = 'http://deploymentinfofidelityagauge:5051'
url_host_deploymentinfoscalabilitybgauge = 'http://deploymentinfoscalabilitybgauge:5052'
url_host_deploymentinfofidelitybgauge = 'http://deploymentinfofidelitybgauge:5053'
url_host_modelmanagerknowledge = 'http://modelmanagerknowledge:5071'


headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}


def main():

    while True:
        logging.warning("Loop: " + str(datetime.datetime.today()))

        data = {}
        try:
            # /getcpufailuregauge
            # url_host_failuregauge
            cpuFailureRate = httpx.get(f"{url_host_failuregauge}/getcpufailuregauge",
                                       headers=headers)

            logging.warning("CpuFailureRate: " + str(cpuFailureRate.json()))

            # /getdeploymentinfoscalabilityagauge
            # url_host_deploymentinfoscalabilityagauge
            scalabilityaDesiredReplicas = httpx.get(f"{url_host_deploymentinfoscalabilityagauge}/getdeploymentinfoscalabilityagauge",
                                                    headers=headers)

            logging.warning("scalabilityaDesiredReplicas: " +
                            str(scalabilityaDesiredReplicas.json()))

            # /getdeploymentinfofidelityagauge
            # url_host_deploymentinfofidelityagauge
            fidelityaDesiredReplicas = httpx.get(f"{url_host_deploymentinfofidelityagauge}/getdeploymentinfofidelityagauge",
                                                 headers=headers)

            logging.warning("fidelityaDesiredReplicas: " +
                            str(fidelityaDesiredReplicas.json()))

            # /getdeploymentinfoscalabilitybgauge
            # url_host_deploymentinfoscalabilitybgauge
            scalabilitybDesiredReplicas = httpx.get(f"{url_host_deploymentinfoscalabilitybgauge}/getdeploymentinfoscalabilitybgauge",
                                                    headers=headers)

            logging.warning("scalabilitybDesiredReplicas: " +
                            str(scalabilitybDesiredReplicas.json()))

            # /getdeploymentinfofidelitybgauge
            # url_host_deploymentinfofidelitybgauge
            fidelitybDesiredReplicas = httpx.get(f"{url_host_deploymentinfofidelitybgauge}/getdeploymentinfofidelitybgauge",
                                                 headers=headers)

            logging.warning("fidelitybDesiredReplicas: " +
                            str(fidelitybDesiredReplicas.json()))

            gaugeData = {"cpuFailureRate": cpuFailureRate.json(),
                         "scalabilityaDesiredReplicas": scalabilityaDesiredReplicas.json(),
                         "fidelityaDesiredReplicas": fidelityaDesiredReplicas.json(),
                         "scalabilitybDesiredReplicas": scalabilitybDesiredReplicas.json(),
                         "fidelitybDesiredReplicas": fidelitybDesiredReplicas.json()}

            # Updating Knowledge
            responseKnowledge = httpx.post(f"{url_host_modelmanagerknowledge}/setknowledge",
                                           headers=headers, json=gaugeData)

            logging.warning(str(responseKnowledge))

        except httpx.RequestError as exc:
            logging.error(exc)
            time.sleep(10)
            continue

        time.sleep(10)


if __name__ == '__main__':
    main()
