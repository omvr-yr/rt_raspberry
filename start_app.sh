#!/bin/bash
# This script is to be set up and used inside the Raspberry Pi at startup

# Wait for a few seconds to ensure that the desktop has started properly
sleep 10

# Launch the Flask application in the background
cd /home/Renew-Tech/renew-tech-gen-display-v3
python app.py &

# Launch Chromium in kiosk mode (full screen)
chromium-browser --kiosk --incognito http://127.0.0.1:5000