# PepperQuest4

## Create the Dev Docker Environment
 - Create a `SECRET_KEY`, a 40 character unique string used for session management.
 - Create a `DB_PASS` used for Evennia and Postgres.
 - Run the (docker-run.sh)[docker-run.sh] file. This should create the Docker network `peppercon` and 2 containers. One Postgres and one for Evevnnia.
 - @Note: This will hang the prompt on the evennia container, once you've run the database import come back to this.
 - Run the database import
   ```bash
   DB_USER="the_reaper"
   DB_NAME="evennia"
   SQL_IMPORT="pq4/pq4.072323.sql"
   psql -h 127.0.0.1 -U ${DB_USER} ${DB_NAME} -W < ${SQL_IMPORT}
   ```
 - Run `evennia start -l` in the hanging evennia container shell.
