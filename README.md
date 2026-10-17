# Website & API Health Checker

A small Python script that checks whether websites and APIs are responding. For each address in a list, it prints the status code, how long the response took, and what kind of result it was.

## What it does
- Sends a request to each address in a list
- Prints the status code and the response time
- Sorts the result into three groups:
  - Success (2xx): the site answered normally
  - Client error (4xx): the request was wrong, such as a bad URL
  - Server error (5xx): the site's server failed
- Gives up after 5 seconds if a site does not answer
- Reports a network error if the site cannot be reached at all

## How to run
1. Install Python and the `requests` library:
```
pip install requests
```
2. Run the script:
```
python health_check.py
```

## Example output
```
Checking: https://httpbin.org/status/200
Response time: 0.83s
Success! Status Code: 200

Checking: https://httpbin.org/status/404
Response time: 0.76s
Client Error! Status Code: 404

Checking: https://httpbin.org/status/500
Response time: 0.85s
Server Error! Status Code: 500
```
The test addresses come from httpbin.org, a free service made for testing. Response times will vary.

## Limitations
- It checks each address once and then stops. It does not run on a schedule or keep a log.
- Only test websites and APIs that you own or have permission to test.

## Ideas for next steps
- Repeat the checks on a timer
- Save the results to a log file
- Read the list of addresses from a file

Written while learning Python and API testing.
