docker run \
    --name evennia \
    -it \
    -p 4000:4000 \
    -p 4001:4001 \
    -p 4002:4002 \
    -v $PWD:/usr/src/game \
    --workdir /usr/src/game/pq4 \
    --network=peppercon \
    --rm \
    harbor.squid-ink.us/politeauthority/evennia/evennia:v0.9

