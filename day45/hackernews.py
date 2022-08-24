from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

# print(response.text)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find(name="a", class_="titlelink")

#get the text of the article
article_text = article_tag.getText()
print(article_text)

# get the link of the article
article_link = article_tag.get("href")
print(article_link)

# get the number of upvotes of the article
article_upvotes = soup.find(name="span", class_="score").getText()
print(article_upvotes)

article_texts = []
article_links = []
# get all of the article links
articles = soup.find_all(name="a", class_="titlelink")

# get the article text and article link
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link = article_tag.get("href")
    article_links.append(link)

upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_text)
print(article_links)
print(upvotes)

# find the largest upvotes and get its index
largest_upvote = max(upvotes)
largest_index = upvotes.index(largest_upvote)

# display the corresponding article and article link
print(article_texts[largest_index])
print(article_links[largest_index])


