#!/bin/bash

set -e

python3 -m pip install -r requirements.txt

sudo cp systemd/chiron_tft.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable chiron_tft

mkdir -p ~/printer_data/logs/chiron_tft

echo "Installation complete"
