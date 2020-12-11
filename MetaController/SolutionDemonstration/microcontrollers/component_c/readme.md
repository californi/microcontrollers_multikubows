# Building and deploying in docker hub
docker build -t componentc .
docker tag componentc californibrs/componentc
docker push californibrs/componentc
