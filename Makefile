dir=bot
testcmd=python -m pytest

development:
	ENVIRONMENT=development python -m $(dir)

production:
	ENVRIONMENT=production python -m $(dir)

test:
	$(testcmd)

test_debug:
	$(testcmd) --pdb

coverage:
	$(testcmd) --cov=$(dir) tests
