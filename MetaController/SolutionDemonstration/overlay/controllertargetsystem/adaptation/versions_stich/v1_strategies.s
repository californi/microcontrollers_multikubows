module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };
import lib "tactics.s";

define boolean NoFailureRate = M.failureManagerS.cpufailure == 0.0;
define boolean HighFailureRate = M.failureManagerS.cpufailure > 0.5;

define boolean canRemoveComponenta = M.componentaD.desiredReplicas > 0;
define boolean canRemoveComponentc = M.componentcD.desiredReplicas > 0;

strategy dealingWithFailure [ NoFailureRate || HighFailureRate ] {
  t0: (NoFailureRate) -> addComponenta() @[2500 /*ms*/] {
    t0a: (success) -> done;
  }   
  t1: (HighFailureRate) -> addComponentc() @[2500 /*ms*/] {
    t1a: (success) -> done;
  }   
  t2: (default) -> TNULL;
}


strategy cleaningComponent [ canRemoveComponenta || canRemoveComponentc ] {
  t0: (NoFailureRate && canRemoveComponentc) -> removeComponentc() @[2500 /*ms*/] {
    t0a: (success) -> done;
  } 
  t1: (NoFailureRate && canRemoveComponenta) -> removeComponenta() @[2500 /*ms*/] {
    t1a: (success) -> done;
  }   
  t2: (default) -> TNULL;
}