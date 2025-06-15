kill $(lsof -t -i:8000)
. .venv/bin/activate
python main.py