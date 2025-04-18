NAME = $(shell basename $(CURDIR))
PYNAME = $(subst -,_,$(NAME))

check:
	ruff check $(PYNAME).py
	mypy $(PYNAME).py
	vermin -vv --exclude importlib.metadata --no-tips -i $(PYNAME).py

build:
	rm -rf dist
	uv build

upload: build
	uv-publish

doc:
	update-readme-usage

clean:
	@rm -vrf *.egg-info .venv/ build/ dist/ __pycache__/
