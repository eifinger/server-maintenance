#!/bin/bash
now=$(date +"%Y-%m-%d.%H:%M:%S")
hostname=$(hostname)
source /home/osmc/maintenance/venv/bin/activate
python /home/osmc/maintenance/ubuntu_notifier.py -m "Heartbeat: $hostname - $now"

