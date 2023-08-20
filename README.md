CD into project directory

For registration smoke tests run:
pytest -m smoke tests/registration/login_tests.py --browser firefox

For shopping cart smoke tests run:
pytest -m smoke tests/shopping/shopping_tests.py --browser firefox
pytest -m regression tests/shopping/shopping_tests.py --browser firefox