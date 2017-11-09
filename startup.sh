#!/bin/bash
now=$(date +"%Y-%m-%d.%H:%M:%S")
hostname=$(hostname)
source /home/eifinger/maintenance/venv/bin/activate
python /home/eifiger/maintenance/ubuntu_notifier.py -m "$hostname started at $now"
