module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };
import lib "tactics.s";

define boolean NoFailureRate = M.failureManagerS.cpufailure == 0.0;
define boolean HighFailureRate = M.failureManagerS.cpufailure > 0.5;

strategy dealingNoFailureRate [ NoFailureRate ] {
  t0: (NoFailureRate) -> addComponentaRemoveComponentc() @[20000 /*ms*/] {
    t0a: (success) -> done;
  }   
  t1: (default) -> TNULL;
}

strategy dealingHighFailureRate [ HighFailureRate ] {
  t0: (HighFailureRate) -> addComponentcRemoveComponenta() @[20000 /*ms*/] {
    t0a: (success) -> done;
  }   
  t1: (default) -> TNULL;
}