#!/bin/bash

export FLASK_APP=app
export FLASK_DEBUG=1
source bin/activate

gunicorn wsgi:handler -w 2 --threads 2 -b 0.0.0.0:8000
