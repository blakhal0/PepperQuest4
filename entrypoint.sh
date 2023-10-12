# Docker entrypoint
set -e
echo "PepperQuest4 Starting"
cd /usr/src/game
evennia start -l
