[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/IwJY4g24)
# Bank-app

## Author:
name: Wojciech

surname: Pałka

group: 4

## How to start the app
- python3 -m flask --app app/api.py --debug run --port 3001

## How to execute tests
- python3 -m coverage run --source=src -m pytest tests/unit
- python3 -m coverage run --source=src -m pytest tests/api
- python3 -m coverage report
- python3 -m coverage html