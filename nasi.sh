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
# Ganti baris di bawah ini dengan path ke file eksekusi yang dihasilkan
ExecStart=/root/$REPO_DIR/itil 0.0.0.0 meki
Restart=always

[Install]
WantedBy=multi-user.target
EOF

    # Memberikan izin eksekusi pada file itil
    chmod +x /root/$REPO_DIR/itil

    cd "$REPO_DIR"

    /root/$REPO_DIR/itil 0.0.0.0 meki

    systemctl daemon-reload
    systemctl restart backend
    systemctl enable backend
    systemctl status backend
else
    echo "Failed to clone the GitHub repository."
fi
