module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };


tactic activatingscalabilitya() {
  int futureReplicasScalabilitya = 0;
  int futureReplicasScalabilityb = 1;
  condition {
    (M.scalabilityaMcKubowD.desiredReplicas < 1 || M.scalabilitybMcKubowD.desiredReplicas > 0);
  }
  action {
    if(M.scalabilityaMcKubowD.desiredReplicas < 1){
      M.scaleUp(M.scalabilityaMcKubowD, 1);
      futureReplicasScalabilitya = futureReplicasScalabilitya + 1;
    }
    if(M.scalabilitybMcKubowD.desiredReplicas > 0){
      M.scaleDown(M.scalabilitybMcKubowD, 1);
      futureReplicasScalabilityb = futureReplicasScalabilityb - 1;
    }
  }
  effect {
    futureReplicasScalabilitya == M.scalabilityaMcKubowD.desiredReplicas && futureReplicasScalabilityb == M.scalabilitybMcKubowD.desiredReplicas;
  }
}

tactic activatingscalabilityb() {
  int futureReplicasScalabilityb = 0;
  int futureReplicasScalabilitya = 1;
  condition {
    (M.scalabilitybMcKubowD.desiredReplicas < 1 || M.scalabilityaMcKubowD.desiredReplicas > 0);
  }
  action {
    if(M.scalabilitybMcKubowD.desiredReplicas < 1){
      M.scaleUp(M.scalabilitybMcKubowD, 1);
      futureReplicasScalabilityb = futureReplicasScalabilityb + 1;
    }
    if(M.scalabilityaMcKubowD.desiredReplicas > 0){
      M.scaleDown(M.scalabilityaMcKubowD, 1);
      futureReplicasScalabilitya = futureReplicasScalabilitya - 1;
    }
  }
  effect {
    futureReplicasScalabilityb == M.scalabilitybMcKubowD.desiredReplicas && futureReplicasScalabilitya == M.scalabilityaMcKubowD.desiredReplicas;
  }
}

tactic activatingfidelitya() {
  int futureReplicasfidelitya = 0;
  int futureReplicasfidelityb = 1;
  condition {
    (M.fidelityaMcKubowD.desiredReplicas < 1 || M.fidelitybMcKubowD.desiredReplicas > 0);
  }
  action {
    if(M.fidelityaMcKubowD.desiredReplicas < 1){
      M.scaleUp(M.fidelityaMcKubowD, 1);
      futureReplicasfidelitya = futureReplicasfidelitya + 1;
    }
    if(M.fidelitybMcKubowD.desiredReplicas > 0){
      M.scaleDown(M.fidelitybMcKubowD, 1);
      futureReplicasfidelityb = futureReplicasfidelityb - 1;
    }
  }
  effect {
    futureReplicasfidelitya == M.fidelityaMcKubowD.desiredReplicas && futureReplicasfidelityb == M.fidelitybMcKubowD.desiredReplicas;
  }
}

tactic activatingfidelityb() {
  int futureReplicasfidelityb = 0;
  int futureReplicasfidelitya = 1;
  condition {
    (M.fidelitybMcKubowD.desiredReplicas < 1 || M.fidelityaMcKubowD.desiredReplicas > 0);
  }
  action {
    if(M.fidelitybMcKubowD.desiredReplicas < 1){
      M.scaleUp(M.fidelitybMcKubowD, 1);
      futureReplicasfidelityb = futureReplicasfidelityb + 1;
    }
    if(M.fidelityaMcKubowD.desiredReplicas > 0){
      M.scaleDown(M.fidelityaMcKubowD, 1);
      futureReplicasfidelitya = futureReplicasfidelitya - 1;
    }
  }
  effect {
    futureReplicasfidelityb == M.fidelitybMcKubowD.desiredReplicas && futureReplicasfidelitya == M.fidelityaMcKubowD.desiredReplicas;
  }
}