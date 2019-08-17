dir=bot

development:
	ENVIRONMENT=development python -m $(dir)

production:
	ENVRIONMENT=production python -m $(dir)

test:
	pytest

coverage:
	pytest --cov=$(dir) tests
