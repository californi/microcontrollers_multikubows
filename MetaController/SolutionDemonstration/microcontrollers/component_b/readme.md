# Building and deploying in docker hub
docker build -t componentb .
docker tag componentb californibrs/componentb
docker push californibrs/componentb
