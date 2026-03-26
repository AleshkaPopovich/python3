"""Problem 02: POST request to JSONPlaceholder.

Task:
1. Send POST to https://jsonplaceholder.typicode.com/posts
2. Send JSON payload with fields: title, body, userId
3. Print:
   - status code
   - raw body
   - parsed JSON
4. Confirm response includes your data + id

Note: JSONPlaceholder simulates writes; data is not truly persisted.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def main() -> None:
    payload = {
        "title": "Learn requests",
        "body": "Practice POST requests with JSONPlaceholder",
        "userId": 1,
    }
    response = requests.post(URL, json=payload, timeout=10)
    response.raise_for_status()
    data = response.json()

    print("Status code:", response.status_code)
    print("Raw body:", response.text)
    print("Parsed JSON:", data)


if __name__ == "__main__":
    main()
