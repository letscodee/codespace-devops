install:
	pip install --upgrade pip &&\
        pip install -r Requirements.txt
lint:
	pylint --disable=R,C hello.py . py

format:
	black *.py

test:
	python -m pytest -vv --cov=hello test_hello.py
