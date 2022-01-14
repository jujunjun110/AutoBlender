.PHONY: run

init:
	PIPENV_VENV_IN_PROJECT=true	pipenv install --dev

run:
	blender --background --python main.py
