# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Uses watch to print the stream of events from list namespaces and list pods.
The script will wait for 10 events related to namespaces to occur within
the `timeout_seconds` threshold and then move on to wait for another 10 events
related to pods to occur within the `timeout_seconds` threshold.
"""

from kubernetes import client, config, watch
import logging
import re
from pydantic import BaseModel


class Failure(BaseModel):
    name: str
    type: str
    message: str
    datetime: str


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()

    v1 = client.CoreV1Api()
    #count = 10
    w = watch.Watch()

    for event in w.stream(v1.list_event_for_all_namespaces):
        if event['object'].type == "Warning":
            failure = {"name": event['object'].metadata.name,
                       "type": event['object'].type,
                       "message": event['object'].message,
                       "datetime": event['object'].metadata.creation_timestamp}

            resultNamePod = re.search(
                'kube-znn', str(failure["name"]), re.IGNORECASE)
            resultMessageCPU = re.search(
                'Insufficient cpu', str(failure["message"]), re.IGNORECASE)

            if resultNamePod and resultMessageCPU:
                print("falha encontrada")
                logging.warning(failure)
            else:
                print("falha não encontrada")

    print("Finished pod stream.")


if __name__ == '__main__':
    main()
