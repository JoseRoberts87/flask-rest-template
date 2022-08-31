#!/bin/sh

export FLASK_APP=src
export FLASK_ENV=development
export FLASK_DEBUG=True

python -m flask run