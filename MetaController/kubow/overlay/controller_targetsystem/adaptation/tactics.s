module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };

tactic addLowScalabilityLowQuality() {
  int futureReplicasScalabilityb = M.scalabilitybD.desiredReplicas + 1;
  int futureReplicasScalabilitya = M.scalabilityaD.desiredReplicas - 1;
  int futureReplicasFidelityb = M.fidelitybD.desiredReplicas + 1;
  int futureReplicasFidelitya = M.fidelityaD.desiredReplicas - 1;  
  condition {
    (M.scalabilitybD.maxReplicas > M.scalabilitybD.desiredReplicas && M.scalabilityaD.minReplicas < M.scalabilityaD.desiredReplicas && M.fidelitybD.maxReplicas > M.fidelitybD.desiredReplicas && M.fidelityaD.minReplicas < M.fidelityaD.desiredReplicas);
  }
  action {
    M.scaleUp(M.scalabilitybD, 1);
    M.scaleDown(M.scalabilityaD, 1);
    M.scaleUp(M.fidelitybD, 1);
    M.scaleDown(M.fidelityaD, 1);    
  }
  effect {
    ((futureReplicasScalabilityb == M.scalabilitybD.desiredReplicas && futureReplicasScalabilitya == M.scalabilityaD.desiredReplicas) && (futureReplicasFidelityb == M.fidelitybD.desiredReplicas && futureReplicasFidelitya == M.fidelityaD.desiredReplicas));
  }
}

tactic addHighScalabilityHighQuality() {
  int futureReplicasScalabilitya = M.scalabilityaD.desiredReplicas + 1;
  int futureReplicasScalabilityb = M.scalabilitybD.desiredReplicas - 1;
  int futureReplicasFidelitya = M.fidelityaD.desiredReplicas + 1;
  int futureReplicasFidelityb = M.fidelitybD.desiredReplicas - 1;  
  condition {
    (M.scalabilityaD.maxReplicas > M.scalabilityaD.desiredReplicas && M.scalabilitybD.minReplicas < M.scalabilitybD.desiredReplicas && M.fidelityaD.maxReplicas > M.fidelityaD.desiredReplicas && M.fidelitybD.minReplicas < M.fidelitybD.desiredReplicas);
  }
  action {
    M.scaleUp(M.scalabilityaD, 1);
    M.scaleDown(M.scalabilitybD, 1);
    M.scaleUp(M.fidelityaD, 1);
    M.scaleDown(M.fidelitybD, 1);    
  }
  effect {
    ((futureReplicasScalabilitya == M.scalabilityaD.desiredReplicas && futureReplicasScalabilityb == M.scalabilitybD.desiredReplicas) && (futureReplicasFidelitya == M.fidelityaD.desiredReplicas && futureReplicasFidelityb == M.fidelitybD.desiredReplicas));
  }
}