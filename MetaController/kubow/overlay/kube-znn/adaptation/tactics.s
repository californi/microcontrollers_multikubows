module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };

define boolean NoFailureRate = M.failureManagerS.cpufailure == 0.0;
define boolean LowFailureRate = M.failureManagerS.cpufailure > 0.0 && M.failureManagerS.cpufailure <= 0.5;
define boolean HighFailureRate = M.failureManagerS.cpufailure > 0.5;


tactic activatingscalabilitya() {
  int replicasScalabilityaAdd = M.scalabilityaMcKubowD.desiredReplicas;
  condition {
    (NoFailureRate);
  }
  action {
    M.scaleDown(M.scalabilitybMcKubowD, 1);
    M.scaleUp(M.scalabilityaMcKubowD, 1);    
  }
  effect @[10000]{
    (replicasScalabilityaAdd' + 1 == M.scalabilityaMcKubowD.desiredReplicas);
  }
}

tactic activatingscalabilityb() {
  int replicasScalabilitybAdd = M.scalabilitybMcKubowD.desiredReplicas;
  condition {
    (LowFailureRate || HighFailureRate);
  }
  action {
    M.scaleDown(M.scalabilityaMcKubowD, 1);
    M.scaleUp(M.scalabilitybMcKubowD, 1);    
  }
  effect @[10000]{
    (replicasScalabilitybAdd' + 1 == M.scalabilitybMcKubowD.desiredReplicas);
  }
}

tactic activatingfidelitya() {
  int replicasFidelityaAdd = M.fidelityaMcKubowD.desiredReplicas;
  condition {
    (NoFailureRate || LowFailureRate);
  }
  action {
    M.scaleDown(M.fidelitybMcKubowD, 1); 
    M.scaleUp(M.fidelityaMcKubowD, 1);             
  }
  effect @[10000]{
    (replicasFidelityaAdd' + 1 == M.fidelityaMcKubowD.desiredReplicas);
  }
}

tactic activatingfidelityb() {
  int replicasFidelitybAdd = M.fidelitybMcKubowD.desiredReplicas;
  condition {
    (HighFailureRate);
  }
  action {
    M.scaleDown(M.fidelityaMcKubowD, 1);
    M.scaleUp(M.fidelitybMcKubowD, 1);
  }
  effect @[10000]{
    replicasFidelitybAdd' + 1 == M.fidelitybMcKubowD.desiredReplicas;
  }
}