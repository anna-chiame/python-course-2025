import json
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
OUT_FILE = "comments_chronological.json"

def main() -> None:
    # 1) Download all comments
    url = f"{BASE_URL}/comments"
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()

    comments = resp.json()  # list[dict]

    # 2) "Chronological" order: jsonplaceholder has no timestamps,
    # so we treat increasing 'id' as creation order.
    comments_sorted = sorted(comments, key=lambda c: c.get("id", 0))

    # 3) Dump to file 
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(comments_sorted, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(comments_sorted)} comments to {OUT_FILE}")

if __name__ == "__main__":
    main()
