module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };
import lib "tactics.s";

define boolean highTraffic = M.kubeZnnS.traffic >= 1;
define boolean lowTraffic = M.kubeZnnS.traffic < 1;

strategy activateMicrocontroller [ lowTraffic || highTraffic ] {
  t0: (highTraffic) -> scalingUpMicrocontroller() @[10000 /*ms*/] {
    t0a: (success) -> done;
  }
  t1: (lowTraffic) -> scalingDownMicrocontroller() @[10000 /*ms*/] {
    t1a: (success) -> done;
  }
  t2: (default) -> TNULL;
}
