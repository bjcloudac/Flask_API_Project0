venv:
	python3.10 -m venv .venv
activate:
	. .venv/bin/activate # or source .venv/bin/activate
install:
	pip install -r requirements.txt
run:
	flask run
all: venv activate install run