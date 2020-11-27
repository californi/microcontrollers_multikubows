from kubernetes import client, config, watch
import logging
from pydantic import BaseModel
import httpx

# melhorar essa mensagem


class Message(BaseModel):
    id: int
    content: str


url_host = 'http://failuremanager:5001'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}


def main():

    config.load_incluster_config()
    v1 = client.CoreV1Api()
    w = watch.Watch()

    for event in w.stream(v1.list_event_for_all_namespaces):
        if event['object'].type == "Warning":

            logging.warning(("Name: %s -- Type Event: %s -- Message: %s -- Datetime: %s" % (
                event['object'].metadata.name,
                event['object'].type,
                event['object'].message,
                event['object'].metadata.creation_timestamp
            )))

            mensage = {"id": 1, "content": event['object'].message}

            httpx.post(f"{url_host}/failuremanageroperation",
                       headers=headers,
                       json=mensage)

    logging.info("Finished pod stream.")


if __name__ == '__main__':
    main()
