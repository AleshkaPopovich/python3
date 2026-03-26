"""Problem 07 (part B): messenger sender client.

Task:
1. Split into pairs
2. Write an infinite loop reading message text from terminal
3. Send each message to partner API endpoint /messages
4. Show send status in terminal


Partner setup:
- Partner gives you ngrok public URL
- You set TARGET_BASE_URL to that URL
"""

import requests

TARGET_BASE_URL = "https://replace-with-partner-ngrok-url"
SENDER_NAME = "replace-with-your-name"


def main() -> None:
    target_url = f"{TARGET_BASE_URL.rstrip('/')}/messages"

    while True:
        text = input("Message: ").strip()
        if text.lower() in {"quit", "exit"}:
            break
        if not text:
            continue

        payload = {"sender": SENDER_NAME, "text": text}
        try:
            response = requests.post(target_url, json=payload, timeout=10)
            response.raise_for_status()
            print("Sent:", response.status_code, response.json())
        except requests.RequestException as exc:
            print(f"Send failed: {exc}")


if __name__ == "__main__":
    main()
