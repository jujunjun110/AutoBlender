.PHONY: init, run, test, rest

init:
	PIPENV_VENV_IN_PROJECT=true	pipenv install --dev

run:
	blender --background --python main.py -- --angleStep 60

test:
	pipenv run python -m unittest tests/*

reset:
	rm -rf result
	rm -rf rendered
