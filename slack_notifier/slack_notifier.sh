#!/bin/bash
TEMP_FILE="tmp.txt"
DATA=$(cat)
scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")
cd $scriptDir
source ../venv/bin/activate
LC_ALL=C
size=$(( ${#DATA} + 1 ))
# Number taken from here https://stackoverflow.com/a/18647755
if [ $size -gt 250 ]; then
  echo $DATA > $TEMP_FILE
  python slack_notifier.py -f "$TEMP_FILE" -m "New large message as file"
else
  python slack_notifier.py -m "$DATA"
fi
