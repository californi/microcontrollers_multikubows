module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };

define boolean hasCpufailure = M.failureManagerS.cpufailure >= 1;
define boolean hasNoCpufailure = M.failureManagerS.cpufailure < 1;

tactic scalingDownMicrocontroller() {
  condition {
    hasNoCpufailure;
  }
  action {
    M.scaleUp(M.kubeZnnD, 1);
  }
  effect @[10000]{
    hasNoCpufailure;
  }
}

tactic scalingUpMicrocontroller() {
  condition {
    hasCpufailure;
  }
  action {
    M.scaleDown(M.kubeZnnD, 1);
  }
  effect @[10000]{
    hasCpufailure;
  }
}