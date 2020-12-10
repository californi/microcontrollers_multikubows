# Building and deploying in docker hub
docker build -t architectureevaluator .
docker tag architectureevaluator californibrs/architectureevaluator
docker push californibrs/architectureevaluator

