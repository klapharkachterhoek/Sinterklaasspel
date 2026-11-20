#!/usr/bin/env bash
# Sinterklaas Dobbelspel - starten op Linux Mint (schermvullend / kiosk)
# Afsluiten: Alt+F4
cd "$(dirname "$(readlink -f "$0")")" || exit 1
URL="file://$PWD/index.html"

# Python3 zit standaard in Mint: server starten zodat instellingen in config.json worden bewaard.
if command -v python3 >/dev/null 2>&1; then
  python3 server.py --no-browser &
  SERVER=$!
  trap 'kill "$SERVER" 2>/dev/null' EXIT
  sleep 1
  URL="http://127.0.0.1:8765/"
fi

PROFIEL="${XDG_CACHE_HOME:-$HOME/.cache}/sinterklaasspel"
for b in google-chrome chromium chromium-browser brave-browser microsoft-edge; do
  if command -v "$b" >/dev/null 2>&1; then
    "$b" --kiosk --no-first-run --autoplay-policy=no-user-gesture-required \
         --user-data-dir="$PROFIEL/$b" "$URL"
    exit
  fi
done
if command -v firefox >/dev/null 2>&1; then
  mkdir -p "$PROFIEL/firefox"
  firefox --new-instance --profile "$PROFIEL/firefox" --kiosk "$URL"
  exit
fi
xdg-open "$URL"
wait
