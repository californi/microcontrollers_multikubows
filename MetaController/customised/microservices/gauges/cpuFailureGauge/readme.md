# Building and deploying in docker hub
docker build -t cpufailuregauge .
docker tag cpufailuregauge californibrs/cpufailuregauge
docker push californibrs/cpufailuregauge