#!/bin/bash
DATA=$(cat)
source /home/eifinger/maintenance/venv/bin/activate
python /home/eifinger/maintenance/ubuntu_notifier.py -m "$DATA"
