#!/bin/bash

REPO_URL="https://github.com/AutoFtBot/Kopi.git"
REPO_DIR="Hitam"

git clone "$REPO_URL" "$REPO_DIR"

if [ $? -eq 0 ]; then
    cat >/etc/systemd/system/backend.service <<EOF
[Unit]
Description=backend
After=network.target

[Service]
WorkingDirectory=/root/$REPO_DIR
ExecStart=python3.8 itil.py 0.0.0.0 meki
Restart=always

[Install]
WantedBy=multi-user.target
EOF

    cd "$REPO_DIR"

    python3.8 itil.py 0.0.0.0 meki

    systemctl daemon-reload
    systemctl restart backend
    systemctl enable backend
    systemctl status backend
else
    echo "Failed to clone the GitHub repository."
fi
