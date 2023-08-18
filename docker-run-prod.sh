#!/bin/bash
# PepperQuest4 docker run.
# This script will create the Docker network, the evennia container and postgres container.
#
#
#  Set the following vars
# SECRET_KEY: Session handling secret - Should be random 40 chars
# DB_PASS: Postgres database password
# LOCAL_POSTGRES_DATA_DIR: Dir for postgres data persistence

# MAYBE CHANGE THESE
DB_HOST="pepper-postgres"
DB_NAME="evennia"
DB_USER="the_reaper"

mkdir -p ${LOCAL_POSTGRES_DATA_DIR}

docker network create peppercon

docker rm -f ${DB_HOST}
docker run \
	--name ${DB_HOST} \
	-d \
	-e POSTGRES_PASSWORD=${DB_PASS} \
	-e POSTGRES_USER=${DB_USER} \
	-e POSTGRES_DB=${DB_NAME} \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
        -p 5432:5432 \
	-v ${LOCAL_POSTGRES_DATA_DIR}:/var/lib/postgresql/data \
        --network=peppercon \
	--restart=always \
	postgres:latest

echo "Created Postgres container"

docker rm -f evennia
docker run \
    --name evennia \
    -it \
    -p 4000:4000 \
    -p 4001:4001 \
    -p 4002:4002 \
    --user $UID:$GID \
    -e SECRET_KEY=${SECRET_KEY} \
    -e DB_HOST=${DB_HOST} \
    -e DB_NAME=${DB_NAME} \
    -e DB_USER=${DB_USER} \
    -e DB_PASS=${DB_PASS} \
    --workdir /usr/src/game/pq4 \
    --network=peppercon \
    --rm \
    harbor.squid-ink.us/peppercon/pq4:v.01 \
    tail -f /dev/null
