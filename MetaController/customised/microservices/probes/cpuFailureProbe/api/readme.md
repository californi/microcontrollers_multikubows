# Building and deploying in docker hub
docker build -t cpufailureprobe .
docker tag cpufailureprobe californibrs/cpufailureprobe
docker push californibrs/cpufailureprobe