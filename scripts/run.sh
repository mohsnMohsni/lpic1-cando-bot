source "${BASH_SOURCE%/*}/active_venv.sh"

git pull origin main

python -m app
