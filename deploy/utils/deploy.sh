#!/usr/bin/env bash

##
## Workflow for deploying docker containers.
##

dc="docker-compose"

# Pull latest changes.
$dc pull

# Stop existing containers.
$dc stop -t 1

# Remove existing volumes.
$dc rm -fv

# Recreate and start containers.
$dc up -d
