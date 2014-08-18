# Sample HTTP Check

This sample shows how to turn any shell script into a Service Check
that Datadog can consume and monitor. The aim is simplicity and
time-to-value.

## Python implementation

This python implementation uses CURL under the covers for maximum
flexibility.

To install dependencies:

    make build

To run it:

    DATADOG_API_KEY=(...) DATADOG_APP_KEY=(...) make run my-url



