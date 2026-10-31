import requests

url = "https://api.nasa.gov/neo/rest/v1/feed"
my_params = {
    "api_key": "f6CtKQJgdqNJKWB969wHRCrwRqJ7JqkFbbgRbNKL",
    "start_date": "2026-10-28",
    "end_date": "2026-10-30"
}

response = requests.get(url, params = my_params)
print(response.json())


