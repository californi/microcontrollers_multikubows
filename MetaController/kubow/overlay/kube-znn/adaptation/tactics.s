module kubow.strategies;
import model "KubeZnnSystem:Acme" { KubeZnnSystem as M, KubernetesFam as K };

define boolean highTraffic = M.kubeZnnS.traffic >= 1;
define boolean lowTraffic = M.kubeZnnS.traffic < 1;


/* acho que o problema tá na execucao continua dessa tatica */
tactic scalingDownMicrocontroller() {
  condition {
    lowTraffic;
  }
  action {
    M.scaleUp(M.fidelityMcKubowD, 1);
    M.scaleUp(M.scalabilityMcKubowD, 1); 
    M.scaleUp(M.kubeZnnD, 1);
  }
  effect @[10000]{
    lowTraffic;
  }
}

/*Quando esta zero, nao da scaleUp*/
tactic scalingUpMicrocontroller() {
  condition {
    highTraffic;
  }
  action {
    M.scaleUp(M.fidelityMcKubowD, 1);
    M.scaleUp(M.scalabilityMcKubowD, 1);
    M.scaleUp(M.kubeZnnD, 1);
  }
  effect @[10000]{
    highTraffic;
  }
}
