module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };
import lib "tactics.s";

define boolean NoFailureRate = M.failureManagerS.cpufailure == 0.0;
define boolean LowFailureRate = M.failureManagerS.cpufailure > 0.0 && M.failureManagerS.cpufailure <= 0.5;
define boolean HighFailureRate = M.failureManagerS.cpufailure > 0.5;

strategy activateScalability [ NoFailureRate || LowFailureRate || HighFailureRate ] {
  t0: (NoFailureRate) -> activatingscalabilitya() @[10000 /*ms*/] {
    t0a: (success) -> done;
  }   
  t1: (LowFailureRate) -> activatingscalabilityb() @[10000 /*ms*/] {
    t1a: (success) -> done;
  } 
  t2: (HighFailureRate) -> activatingscalabilityb() @[10000 /*ms*/] {
    t2a: (success) -> done;
  }   
  t3: (default) -> TNULL;
}

strategy activateFidelity [ NoFailureRate || LowFailureRate || HighFailureRate ] {
  t0: (NoFailureRate) -> activatingfidelitya() @[10000 /*ms*/] {
    t0a: (success) -> done;
  }   
  t1: (LowFailureRate) -> activatingfidelitya() @[10000 /*ms*/] {
    t1a: (success) -> done;
  } 
  t2: (HighFailureRate) -> activatingfidelityb() @[10000 /*ms*/] {
    t2a: (success) -> done;
  }   
  t3: (default) -> TNULL;
}

