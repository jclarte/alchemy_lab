#!/bin/bash
# simple bash script to launch both the db container and the jupyter lab service
echo "Starting db container"
docker compose up -d
echo "Starting jupyetr lab"
poetry run jupyter lab
