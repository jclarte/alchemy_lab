# alchemy_lab
a SQL Alchemy 2.0 playground lab

## Requirements

docker (built with version 24.0.2)

python (version 3.11)

poetry (version 1.6.0)

## Usage

1. Setup env with poetry : poetry install
2. Launch jupytar lab in poetry : poetry run jupyter lab
3. Take a notebook and start playing with the API
4. There is a module called "alchemy_lab" with some shortcuts and configuration to play with the db
5. A simple way to launch the lab : `run_lab.sh` that launch db container and jupyter lab service

## When things go wrong

To reinitialize all stuff (containers, volume) from scratch, you should :

1. Stop the container
2. Delete the container
3. Delete the volume
4. Rebuild and up the container