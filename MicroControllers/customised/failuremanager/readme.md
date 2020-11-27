# Building and deploying in docker hub
docker build -t failuremanager .
docker tag failuremanager californibrs/failuremanager
docker push californibrs/failuremanager


# Only to vallid environemtn docker (problem with k8s api)
docker run -d --name failuremanager -p 8000:5002 californibrs/failuremanager