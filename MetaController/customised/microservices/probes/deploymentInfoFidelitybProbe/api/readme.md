# Building and deploying in docker hub
docker build -t deploymentinfofidelitybprobe .
docker tag deploymentinfofidelitybprobe californibrs/deploymentinfofidelitybprobe
docker push californibrs/deploymentinfofidelitybprobe