module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };
import lib "tactics.s";

//define boolean canAddReplicaFidelity = M.fidelityMcKubowD.maxReplicas > M.fidelityMcKubowD.desiredReplicas;
//define boolean canAddReplicaScalability = M.scalabilityMcKubowD.maxReplicas > M.scalabilityMcKubowD.desiredReplicas;

define boolean hasCpufailure = M.failureManagerS.cpufailure > 0;
define boolean hasNoCpufailure = M.failureManagerS.cpufailure == 0.0;

strategy activateMicrocontroller [ hasCpufailure || hasNoCpufailure ] {
  t0: (hasCpufailure) -> scalingUpMicrocontroller() @[10000 /*ms*/] {
    t0a: (success) -> done;
  }
  t1: (hasNoCpufailure) -> scalingDownMicrocontroller() @[10000 /*ms*/] {
    t1a: (success) -> done;
  }
  t2: (default) -> TNULL;
}