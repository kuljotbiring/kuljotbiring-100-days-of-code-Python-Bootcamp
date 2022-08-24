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

# finds all anchor tags
all_anchor_tags = soup.find_all(name="a")


for tag in all_anchor_tags:
    # get just the names of the anchor tags
    print(tag.getText())
    # get href links
    print(tag.get("href"))

# get a hold by attribute name
heading = soup.find(name="h1", id="name")
section_heading = soup.find(name="h3", class_="heading")

# drill down into elements using CSS selectors
company_url = soup.select_one(selector="p a")

