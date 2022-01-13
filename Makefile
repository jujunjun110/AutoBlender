.PHONY: run

init:
	PIPENV_VENV_IN_PROJECT=true	pipenv install

run:
	blender --background --python main.py
