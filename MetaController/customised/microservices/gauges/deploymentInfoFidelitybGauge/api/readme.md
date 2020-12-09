# Building and deploying in docker hub
docker build -t deploymentinfofidelitybgauge .
docker tag deploymentinfofidelitybgauge californibrs/deploymentinfofidelitybgauge
docker push californibrs/deploymentinfofidelitybgauge