# Building and deploying in docker hub
docker build -t deploymentinfofidelityagauge .
docker tag deploymentinfofidelityagauge californibrs/deploymentinfofidelityagauge
docker push californibrs/deploymentinfofidelityagauge