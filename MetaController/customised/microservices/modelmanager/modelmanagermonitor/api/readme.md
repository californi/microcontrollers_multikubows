# Building and deploying in docker hub
docker build -t modelmanagermonitor .
docker tag modelmanagermonitor californibrs/modelmanagermonitor
docker push californibrs/modelmanagermonitor

