module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };

tactic addComponenta() {
  int futureReplicas = M.componentaD.desiredReplicas + 1;
  condition {
    M.componentaD.maxReplicas > M.componentaD.desiredReplicas;
  }
  action {
    M.scaleUp(M.componentaD, 1);
  }
  effect {
    futureReplicas' == M.componentaD.desiredReplicas;
  }
}

tactic removeComponenta() {
  int futureReplicas = M.componentaD.desiredReplicas - 1;
  condition {
    M.componentaD.minReplicas < M.componentaD.desiredReplicas;
  }
  action {
    M.scaleDown(M.componentaD, 1);
  }
  effect {
    futureReplicas' == M.componentaD.desiredReplicas;
  }
}

tactic addComponentc() {
  int futureReplicas = M.componentcD.desiredReplicas + 1;
  condition {
    M.componentcD.maxReplicas > M.componentcD.desiredReplicas;
  }
  action {
    M.scaleUp(M.componentcD, 1);
  }
  effect {
    futureReplicas' == M.componentcD.desiredReplicas;
  }
}

tactic removeComponentc() {
  int futureReplicas = M.componentcD.desiredReplicas - 1;
  condition {
    M.componentcD.minReplicas < M.componentcD.desiredReplicas;
  }
  action {
    M.scaleDown(M.componentcD, 1);
  }
  effect {
    futureReplicas' == M.componentcD.desiredReplicas;
  }
}