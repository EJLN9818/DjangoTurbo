#!/usr/bin/env bash
set -euo pipefail

pnpm install
pnpm compile
pnpm build

pip-sync --user

python3.8 manage.py migrate --noinput
python3.8 manage.py collectstatic --noinput
find ./static/img/ -name "*.webp" -delete
sudo systemctl reload gunicorn

find . -name "*.pyc" -delete
sudo systemctl reload huey

find static/ -type f -and \( -iname "*.jpg" -o -iname "*.jpeg" \) -exec bash -c '
  for result; do
    webp_path=$(sed '\''s/\.[^.]*$/.webp/'\'' <<< "$result");
    if [ ! -f "$webp_path" ]; then
      cwebp "$result" -o "$webp_path";
    fi;
  done
' _ {} +
find static/ -type f -and -iname "*.png" -exec bash -c '
  for result; do
    webp_path=$(sed '\''s/\.[^.]*$/.webp/'\'' <<< "$result");
    if [ ! -f "$webp_path" ]; then
      cwebp -lossless "$result" -o "$webp_path";
    fi;
  done
' _ {} +
find static/ -type f -and -iname "*.gif" -exec bash -c '
  for result; do
    webp_path=$(sed '\''s/\.[^.]*$/.webp/'\'' <<< "$result");
    if [ ! -f "$webp_path" ]; then
      gif2webp "$result" -mixed -o "$webp_path";
    fi;
  done
' _ {} +
