"""Problem 03: GET request for HTML content.

Task:
1. Send GET to https://example.com
2. Print:
   - status code
   - Content-Type header
   - HTML body (response.text)
3. Verify content type contains text/html
4. Add raise_for_status()
"""

import requests

URL = "https://example.com"


def main() -> None:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    content_type = response.headers.get("Content-Type", "")
    if "text/html" not in content_type:
        raise ValueError("expected HTML response")

    print("Status code:", response.status_code)
    print("Content-Type:", content_type)
    print(response.text)


if __name__ == "__main__":
    main()
