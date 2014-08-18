# Sample HTTP Check

This sample shows how to turn any shell script into a Service Check
that Datadog can consume and monitor. The aim is simplicity and
time-to-value.

## Python implementation

This python implementation uses CURL under the covers for maximum
flexibility.

It is packaged with `make` as an example.

To install dependencies:

    make build

To run it:

    make run MY_URL=(...) DATADOG_API_KEY=(...) DATADOG_APP_KEY=(...)

If you don't want to us `make`, you can run it from the command line:

    DATADOG_API_KEY=... DATADOG_APP_KEY=... venv/bin/python sample.py my-url


