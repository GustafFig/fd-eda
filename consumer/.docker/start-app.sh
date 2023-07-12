#!/bin/bash

python -m pdm install
dockerize -wait tcp://kafka:29092 -timeout 30s
python -m pdm run start
