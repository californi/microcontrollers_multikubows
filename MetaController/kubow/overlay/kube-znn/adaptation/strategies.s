module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };
import lib "tactics.s";


define boolean hasCpufailure = M.failureManagerS.cpufailure >= 1;
define boolean hasNoCpufailure = M.failureManagerS.cpufailure < 1;

strategy activateMicrocontroller [ hasCpufailure || hasNoCpufailure ] {
  t0: (hasNoCpufailure) -> scalingUpMicrocontroller() @[10000 /*ms*/] {
    t0a: (success) -> done;
  }
  t1: (hasCpufailure) -> scalingDownMicrocontroller() @[10000 /*ms*/] {
    t1a: (success) -> done;
  }
  t2: (default) -> TNULL;
}