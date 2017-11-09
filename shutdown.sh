#!/bin/bash
now=$(date +"%Y-%m-%d.%H:%M:%S")
hostname=$(hostname)
source /home/eifinger/maintenance/venv/bin/activate
python /home/eifinger/maintenance/ubuntu_notifier.py -m "$hostname going down at $now"
