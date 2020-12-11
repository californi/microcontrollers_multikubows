module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };

tactic addComponentaRemoveComponentc() {
  int futureReplicasComponenta = M.componentaD.desiredReplicas + 1;
  int futureReplicasComponentc = M.componentcD.desiredReplicas - 1;
  condition {
    M.componentaD.maxReplicas > M.componentaD.desiredReplicas && M.componentcD.minReplicas < M.componentcD.desiredReplicas;
  }
  action {
    M.scaleUp(M.componentaD, 1);
    M.scaleDown(M.componentcD, 1);
  }
  effect {
    futureReplicasComponenta == M.componentaD.desiredReplicas && futureReplicasComponentc == M.componentcD.desiredReplicas;
  }
}

tactic addComponentcRemoveComponenta() {
  int futureReplicasComponentc = M.componentcD.desiredReplicas + 1;
  int futureReplicasComponenta = M.componentaD.desiredReplicas - 1;
  condition {
    M.componentcD.maxReplicas > M.componentcD.desiredReplicas && M.componentaD.minReplicas < M.componentaD.desiredReplicas;
  }
  action {
    M.scaleUp(M.componentcD, 1);
    M.scaleDown(M.componentaD, 1);
  }
  effect {
    futureReplicasComponentc == M.componentcD.desiredReplicas && futureReplicasComponenta == M.componentaD.desiredReplicas;
  }
}
