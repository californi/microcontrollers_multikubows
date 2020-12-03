# Building and deploying in docker hub
docker build -t metacontroller .
docker tag metacontroller californibrs/metacontroller
docker push californibrs/metacontroller