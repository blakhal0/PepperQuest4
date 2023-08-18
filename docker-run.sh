docker run \
    --name evennia \
    -it \
    -p 4000:4000 \
    -p 4001:4001 \
    -p 4002:4002 \
    -v $PWD/pq4:/usr/src/game \
    --user $UID:$GID \
    --rm \
    harbor.squid-ink.us/politeauthority/evennia/evennia:v0.9
