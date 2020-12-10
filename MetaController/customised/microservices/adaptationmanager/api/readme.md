# Building and deploying in docker hub
docker build -t adaptationmanager .
docker tag adaptationmanager californibrs/adaptationmanager
docker push californibrs/adaptationmanager