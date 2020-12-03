from kubernetes import client, config, watch
import datetime
import requests
import logging
import time

PROMETHEUS = 'http://prometheus:9090/'


def activate_deployment(api, deployment_name, activate):
    deployment = api.read_namespaced_deployment(
        deployment_name, "default")

    if(activate):
        deployment.spec.replicas = 1
    else:
        deployment.spec.replicas = 0

    # Update the deployment
    api_response = api.patch_namespaced_deployment(
        name=deployment_name,
        namespace="default",
        body=deployment)
    # logging.warning("Deployment updated. status='%s'" %
    # str(api_response.status))
    # logging.warning("Updated.")


def main():

    while True:
        logging.warning("Loop: " + str(datetime.datetime.today()))

        response = requests.get(PROMETHEUS + '/api/v1/query', params={
                                'query': 'sum (rate(http_requests_total{handler="/insufficientcpu"}[30s]))'})

        results = response.json()['data']['result']
        cpuFailureRate = 0.0

        for result in results:
            cpuFailureRate = float('{value[1]}'.format(**result))

        logging.warning("cpuFailureRate: " + str(cpuFailureRate))

        NoFailureRate = cpuFailureRate == 0.0
        LowFailureRate = cpuFailureRate > 0.0 and cpuFailureRate <= 0.5
        HighFailureRate = cpuFailureRate > 0.5

        # config.load_kube_config()  # de fora cluster K8s
        config.load_incluster_config()  # de dentro do cluster K8s
        apps_v1 = client.AppsV1Api()

        if NoFailureRate:
            logging.warning("activating Scalability a and Fidelity a...")

            activate_deployment(apps_v1, "scalabilitya-mc-kubow", True)
            activate_deployment(apps_v1, "fidelitya-mc-kubow", True)
            activate_deployment(apps_v1, "scalabilityb-mc-kubow", False)
            activate_deployment(apps_v1, "fidelityb-mc-kubow", False)

        elif LowFailureRate:
            logging.warning("activating Scalability b and Fidelity a...")

            activate_deployment(apps_v1, "scalabilitya-mc-kubow", False)
            activate_deployment(apps_v1, "fidelitya-mc-kubow", True)
            activate_deployment(apps_v1, "scalabilityb-mc-kubow", True)
            activate_deployment(apps_v1, "fidelityb-mc-kubow", False)

        else:
            logging.warning("activating Scalability b and Fidelity b...")

            activate_deployment(apps_v1, "scalabilitya-mc-kubow", False)
            activate_deployment(apps_v1, "fidelitya-mc-kubow", False)
            activate_deployment(apps_v1, "scalabilityb-mc-kubow", True)
            activate_deployment(apps_v1, "fidelityb-mc-kubow", True)

        time.sleep(10)


if __name__ == '__main__':
    main()
