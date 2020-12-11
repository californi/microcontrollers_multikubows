module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };
import lib "tactics.s";

define boolean NoFailureRate = M.failureManagerS.cpufailure == 0.0;
define boolean HighFailureRate = M.failureManagerS.cpufailure > 0.5;

strategy dealingWithFailure [ NoFailureRate || HighFailureRate ] {
  t0: (NoFailureRate) -> addComponentaRemoveComponentc() @[2500 /*ms*/] {
    t0a: (success) -> done;
  }   
  t1: (HighFailureRate) -> addComponentcRemoveComponenta() @[2500 /*ms*/] {
    t1a: (success) -> done;
  }   
  t2: (default) -> TNULL;
}