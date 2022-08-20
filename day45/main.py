# use beautiful soup module
from bs4 import BeautifulSoup

# shove all of the html website into variable named contents
with open("website.html") as f:
    contents = f.read()

# pass beautiful soup a string with the parser
soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.prettify())

# gives first occurrence of anchor tag
print(soup.a)
