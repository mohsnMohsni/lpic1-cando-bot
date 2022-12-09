if ! [ -d "venv" ]; then
  sudo apt install python3-venv
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements/production.txt
else
  source venv/bin/activate
fi
