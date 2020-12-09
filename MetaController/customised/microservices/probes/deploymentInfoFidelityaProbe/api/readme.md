# Building and deploying in docker hub
docker build -t deploymentinfofidelityaprobe .
docker tag deploymentinfofidelityaprobe californibrs/deploymentinfofidelityaprobe
docker push californibrs/deploymentinfofidelityaprobe