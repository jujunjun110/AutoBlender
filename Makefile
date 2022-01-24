.PHONY: init, run, test, rest

ANGLE_STEP?=90
CAM_DISTANCE?=10
FILE?=./assets/default.fbx


init:
	PIPENV_VENV_IN_PROJECT=true	pipenv install --dev

run:
	blender --background --python main.py -- --angleStep ${ANGLE_STEP} --file ${FILE} --camDistance ${CAM_DISTANCE}

test:
	pipenv run python -m unittest tests/*

reset:
	rm -rf result
	rm -rf rendered
