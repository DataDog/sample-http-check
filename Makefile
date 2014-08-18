.PHONY: build run

build:
	virtualenv venv
	venv/bin/pip install -e .

run:
	venv/bin/python sample.py $(MY_URL) $(DATADOG_API_KEY) $(DATADOG_APP_KEY)
