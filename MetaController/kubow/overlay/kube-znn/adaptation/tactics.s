module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };

define boolean hasCpufailure = M.failureManagerS.cpufailure > 0;
define boolean hasNoCpufailure = M.failureManagerS.cpufailure == 0.0;

tactic scalingUpMicrocontroller() {
  condition {
    hasCpufailure;
  }
  action {
    M.scaleUp(M.fidelityMcKubowD, 1);
    M.scaleUp(M.scalabilityMcKubowD, 1);
  }
  effect @[10000]{
    hasCpufailure;
  }
}

tactic scalingDownMicrocontroller() {
  condition {
    hasNoCpufailure;
  }
  action {
    M.scaleDown(M.fidelityMcKubowD, 1);
    M.scaleDown(M.scalabilityMcKubowD, 1);
  }
  effect @[10000]{
    hasNoCpufailure;
  }
}