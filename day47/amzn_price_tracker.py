import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

# find the URL of the product I want to track
url = "https://www.amazon.com/LG-34UM69G-B-34-Inch-UltraWide-Reduction/dp/B06XFXX5JH/ref=sr_1_19?content-id=amzn1" \
      ".sym.cdff5709-1ad3-49fb-b3a2-fd145c65c07d%3Aamzn1.sym.cdff5709-1ad3-49fb-b3a2-fd145c65c07d&keywords=lg+34+" \
      "inch+ultrawide+monitor&pd_rd_r=1530c6a4-af98-4f9c-a49f-9adb3f662c69&pd_rd_w=CUmJD&pd_rd_wg=KX2LF&pf_rd_" \
      "p=cdff5709-1ad3-49fb-b3a2-fd145c65c07d&pf_rd_r=BHVWFJESSGQM31MVS397&qid=1674326831&sr=8-19"

# get the header information from http://myhttpheader.com/
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Accept-Language": "en-US,en;q=0.5"
}
# get the response from the webpage
response = requests.get(url, headers=header)

# use BS to make the soup with the webpage HTML. Use lxml parser instead of html.parser
soup = BeautifulSoup(response.content, "lxml")

# print out soup results
# print(soup.prettify())

price = soup.find(name="span", class_="a-price-whole").get_text()
# price_without_currency = price.split("$")[1]
price_as_float = float(price)
print(f"${price_as_float}")

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 350

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(
            from_addr="YOUR_EMAIL",
            to_addrs="YOUR_EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
