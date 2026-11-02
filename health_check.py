import sys
sys.stdout.reconfigure(encoding="utf-8")

import requests

def check_json_field(url, key):
    print(f"Checking JSON from: {url}")
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
    except ValueError:
        print("FAIL: the reply is not valid JSON")
        return
    except requests.exceptions.RequestException as e:
        print(f"Network Error ({e})")
        return

    if key in data:
        print(f"PASS: found '{key}' in the reply")
    else:
        print(f"FAIL: '{key}' is missing from the reply")

def advanced_health_check(url):
    print(f"Checking: {url}")
    
    try:
        # We send the request
        response = requests.get(url, timeout=5)
        print(f"Response time: {response.elapsed.total_seconds():.2f}s")
        
        # 🟢 Category 1: Total Success (below 400)
        if response.ok:
            print(f"Success! Status Code: {response.status_code} ✅")
            
        # 🔴 Category 2: Client Error (400-499) -> We made a mistake
        elif 400 <= response.status_code < 500:
            print(f"Client Error! Status Code: {response.status_code} 👤")
            print("-> Fix your script: The URL might be wrong or you are locked out.")
            
        # 🔥 Category 3: Server Error (500-599) -> Their backend is broken
        elif response.status_code >= 500:
            print(f"Server Error! Status Code: {response.status_code} 💥")
            print("-> Wait it out: The website's server crashed or is undergoing maintenance.")

    except requests.exceptions.RequestException as e:
        # This catches completely dead links where the server didn't even answer
        print(f"Network Error! Could not even connect to the server 🔌 ({e})")

# Let's see it in action with a dummy API built for testing
sites = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
]

for site in sites:
    advanced_health_check(site)
    
check_json_field("https://httpbin.org/json", "slideshow")
check_json_field("https://httpbin.org/json", "author")
check_json_field("https://httpbin.org/html", "slideshow")

r = requests.get("https://httpbin.org/json", timeout=5)
info = r.json()["slideshow"]
# 'author' sits inside 'slideshow', so this top-level check is expected to fail
print("'author' inside 'slideshow':", "author" in info)