#!/bin/bash
scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")
cd $scriptDir
now=$(date +"%Y-%m-%d.%H:%M:%S")
hostname=$(hostname)
source venv/bin/activate
python slack_notifier/slack_notifier.py -m "$hostname going down at $now"
