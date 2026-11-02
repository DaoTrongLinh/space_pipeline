import requests
import json

url = "https://api.nasa.gov/neo/rest/v1/feed"
my_params = {
    "api_key": "f6CtKQJgdqNJKWB969wHRCrwRqJ7JqkFbbgRbNKL",
    "start_date": "2026-10-24",
    "end_date": "2026-10-30"
}


response = requests.get(url, params = my_params)
obj = response.json()
result = json.dumps(obj, sort_keys = True, indent = 4)

print(result)
print(response.status_code)
