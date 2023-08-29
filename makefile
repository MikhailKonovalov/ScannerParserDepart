VENV = env
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
REQUIREMENTS = requirements.txt

all: create_env activate install

create_env:
	python3 -m venv $(VENV)

install: $(VENV) activate
	$(PIP) install -r $(REQUIREMENTS)

activate: $(VENV)
	. $(VENV)/bin/activate

clean: $(VENV)
	rm -r env

.PHONY: create_env activate install