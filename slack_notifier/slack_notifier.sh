#!/bin/bash
DATA=$(cat)
scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")
cd $scriptDir
source ../venv/bin/activate
python slack_notifier.py -m "$DATA"
