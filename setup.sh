#!/usr/bin/env bash
#USAGE: bash setup.sh <image name> <container name>
#   e.g., bash setup.sh bootcamp bootcamp

#Clone bootcamp repository
git clone https://github.com/jmportilla/Complete-Python-Bootcamp.git

#Build the docker image
docker build -t $1 .
#Run a container
docker run -it -v $PWD:/work -p 8888:8888 --name $2 $1
