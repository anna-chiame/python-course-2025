import requests

urls = {
    "wikipedia": "https://www.wikipedia.org/robots.txt",
    "twitter": "https://twitter.com/robots.txt",
}

for name, url in urls.items():
    response = requests.get(url)

    # Save robots.txt to file
    with open(f"{name}_robots.txt", "w", encoding="utf-8") as file:
        file.write(response.text)

    print(f"{name}_robots.txt saved")
