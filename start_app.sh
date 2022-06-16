#!/bin/bash

export FLASK_APP=project
export FLASK_DEBUG=1
source bin/activate

flask run
