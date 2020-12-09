from pydantic import BaseModel


class DataKnowledge(BaseModel):
    cpuFailureRate: str
    scalabilityaDesiredReplicas: str
    fidelityaDesiredReplicas: str
    scalabilitybDesiredReplicas: str
    fidelitybDesiredReplicas: str
