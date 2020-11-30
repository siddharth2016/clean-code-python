# Just a makefile to make sure the types, lint and tests are fine in continuous integration pipeline.

typecheck:
	mypy src/ tests/

tests:
	pytest tests/

lint:
	pylint src/ tests/

checklist: lint typecheck tests

.PHONY: typecheck tests lint checklist