git pull origin main

sudo docker-compose --env-file ./envs/.env.production up --build -d

docker image rm -f $(docker images -q --filter "dangling=true");

docker container prune -f;

docker network prune -f;
