from bs4 import BeautifulSoup

html = """
<html>
<head> <title> Beautiful Soup Example </title> </head>
<body>
<p class="intro">This is the first paragraph.</p>
<p class="content">This is the second paragraph.</p>
<p class="new">This is my new third paragraph!</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html5lib')

all_p = soup.find_all('p')
print("Total paragraphs found:", len(all_p))

for i, p in enumerate(all_p, 1):
    print(f"--- Paragraph {i} ---")
    print(p.text)
