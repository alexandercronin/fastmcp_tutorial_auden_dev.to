curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install .
npm install