#! /bin/bash

# creating poetry venv
cd /app && poetry install

# Capture arguments
channel_id="$1"
bot_name="$2"
file_name="$3"

# Build the command based on available parameters
CMD="poetry run python3 /app/send_slack_alert.py --channel_id \"$channel_id\" --bot_name \"$bot_name\" --file_name \"$file_name"\"

# Print and execute the command
echo "Executing command: $CMD"
eval "$CMD"