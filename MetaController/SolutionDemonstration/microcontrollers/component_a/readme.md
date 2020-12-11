# Building and deploying in docker hub
docker build -t componenta .
docker tag componenta californibrs/componenta
docker push californibrs/componenta
