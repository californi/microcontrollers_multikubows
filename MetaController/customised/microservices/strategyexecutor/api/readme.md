# Building and deploying in docker hub
docker build -t stratetyexecutor .
docker tag stratetyexecutor californibrs/stratetyexecutor
docker push californibrs/stratetyexecutor