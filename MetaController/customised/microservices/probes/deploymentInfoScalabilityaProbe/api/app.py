from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException
import datetime
import requests
import logging
import time
import httpx


url_host = 'http://deploymentinfoscalabilityagauge:5050'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}


def main():

    while True:
        logging.warning("Loop: " + str(datetime.datetime.today()))
        config.load_incluster_config()
        apps_v1 = client.AppsV1Api()

        data = {}
        try:
            deployment = apps_v1.read_namespaced_deployment(
                "scalabilitya-mc-kubow", "default")

            data = {"name": "deploymentInfoScalabilityaProbe.desiredReplicas",
                    "type": "deploymentInfo",
                    "value": deployment.spec.replicas,
                    "dateevent": str(datetime.datetime.today())}

            response = httpx.post(f"{url_host}/setdeploymentinfoscalabilityagauge",
                                  headers=headers,
                                  json=data)

            logging.warning("Response: " + str(response))
        except ApiException as e:
            if e.status != 404:
                print("Deployment not found: %s" % e)
                break

        time.sleep(5)


if __name__ == '__main__':
    main()
