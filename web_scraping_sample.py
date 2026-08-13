import requests
import re
from bs4 import BeautifulSoup

url = "https://blog.python.org/blog/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html5lib")

headings = soup.find_all("h3")

posts = []
for h in headings:
    # The post link wraps the h3 as a parent, not a child
    parent_link = h.find_parent("a")
    if not parent_link:
        continue
    href = parent_link.get("href", "")
    if not re.search(r"/\d{4}/\d{2}/", href):
        continue

    title = h.get_text(strip=True)

    author_tag = h.find_next("a", href=re.compile(r"^/authors/"))
    author = author_tag.get_text(strip=True) if author_tag else "Unknown author"

    date = "Unknown date"
    if author_tag:
        meta_text = author_tag.parent.get_text()
        date_match = re.search(r"[A-Z][a-z]+ \d{1,2}, \d{4}", meta_text)
        if date_match:
            date = date_match.group(0)

    posts.append((title, author, date))

print(f"Found {len(posts)} posts:\n")
for i, (title, author, date) in enumerate(posts, start=1):
    print(f"{i}. {title}")
    print(f"   By {author} · {date}")
    print()
