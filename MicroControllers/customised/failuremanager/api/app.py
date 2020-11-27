from fastapi import FastAPI, Request, Response
from kubernetes import client, config, watch
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


Instrumentator().instrument(app).expose(app)

# config.load_kube_config()
# config.load_incluster_config()
#apps_v1 = client.AppsV1Api()

config.load_incluster_config()
v1 = client.CoreV1Api()


@app.get("/hello")
def hello_world():
    return "Testing prometheus"


def main():

    w = watch.Watch()

    for event in w.stream(v1.list_event_for_all_namespaces):
        if event['object'].type == "Warning":

            print("Name: %s -- Type Event: %s -- Message: %s -- Datetime: %s" % (
                event['object'].metadata.name,
                event['object'].type,
                event['object'].message,
                event['object'].metadata.creation_timestamp
            ))

    print("Finished pod stream.")


if __name__ == '__main__':
    main()
