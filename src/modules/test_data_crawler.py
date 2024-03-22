import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

def crawl_website(base_url):
    visited_urls = set()
    urls_to_visit = deque([base_url])

    while urls_to_visit:
        url = urls_to_visit.popleft()
        if url in visited_urls:
            continue

        # Load HTML
        response = requests.get(url)
        if response.status_code != 200:
            continue

        html = response.text

        # Transform HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Extract URLs
        new_urls = set()
        for link in soup.find_all("a", href=True):
            sub_url = link["href"]
            # Make sure the URL is absolute
            absolute_url = urljoin(url, sub_url)
            # Filter out URLs not from the base domain and not already visited
            if urlparse(absolute_url).netloc == urlparse(base_url).netloc:
                new_urls.add(absolute_url)

        visited_urls.add(url)
        print(url)
        urls_to_visit.extend(new_urls)

        # Write discovered URLs to a text file
    with open("././data/discovered_urls.txt", "w") as file:
        for url in visited_urls:
            file.write(url + "\n")

    return visited_urls

def main():
    base_url = "https://www.glos.ac.uk/information/knowledge-base/"
    visited_urls = crawl_website(base_url)
    for url in visited_urls:
        print(url)

if __name__ == "__main__":
    main()