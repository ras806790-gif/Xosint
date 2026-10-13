#!/data/data/com.termux/files/usr/bin/bash
set -eu
echo "== Xosint Termux setup =="
if ! command -v pkg >/dev/null 2>&1; then
  echo "This installer is intended for Termux."
  exit 1
fi
pkg update
pkg install python -y
chmod +x xosint.py
echo
echo "Setup complete."
echo "Interactive: python xosint.py"
echo "Username:    python xosint.py example_username"
