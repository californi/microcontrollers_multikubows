# Building and deploying in docker hub
docker build -t activatedeploymenteffector .
docker tag activatedeploymenteffector californibrs/activatedeploymenteffector
docker push californibrs/activatedeploymenteffector