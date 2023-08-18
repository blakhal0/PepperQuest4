FROM evennia/evennia:v0.9
ENV DB_USER=''
ENV DB_PASS=''
ENV DB_HOST=''
ENV DB_PORT='5432'
RUN apk -U update
RUN apk add --no-cache \
    postgresql-dev gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip install pip --upgrade \
    pip install psycopg2==2.8.6 syllables==0.1.0
ADD pq4 /usr/src/game
RUN mkdir -p /usr/src/game/server/logs

CMD evennia start -l
