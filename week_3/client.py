import requests

API_URL = "http://127.0.0.1:8000/predict"


def main():
    print("=== Spam API Client ===")
    print("Type a message to send to the API, or 'q' to quit.\n")

    while True:
        text = input("Message: ").strip()
        if text.lower() in {"q", "quit", "exit"}:
            break

        payload = {"text": text}
        try:
            resp = requests.post(API_URL, json=payload, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            print(f"=> API label: {data['label']} (is_spam={data['is_spam']})\n")
        except Exception as e:
            print(f"Error calling API: {e}\n")


if __name__ == "__main__":
    main()
