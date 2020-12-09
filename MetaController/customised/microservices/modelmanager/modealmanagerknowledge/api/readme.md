# Building and deploying in docker hub
docker build -t modelmanagerknowledge .
docker tag modelmanagerknowledge californibrs/modelmanagerknowledge
docker push californibrs/modelmanagerknowledge