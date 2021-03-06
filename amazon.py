import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.in/s?k=mobile+phone+under+10000&page=1&crid=2Y2D0HIDVJ4TM&qid=1605879923&sprefix=mobile+%2Caps%2C489&ref=sr_pg_1"
r = requests.get(url)
if(r.status_code==503):
    print("No Response")
    exit()
content = r.content
#print(content)
soup = BeautifulSoup(content,'html.parser')
#print(soup)

names = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")
#print(names)
phone_details = list()
count = 1
for i in names:
    print(str(count) +". "+ i.string)

    name = i.string
    #price = i.find_next("span", class_="a-price-whole")
    price_ = i.find_next("span", class_="a-price")
    #print(type(price_))
    #mrp = price.find_next_sibling("span", class_="a-offscreen")
    if(price_ == None):
        price = "Not Mentioned"
    else:
        price = price_.find("span", class_="a-price-whole").string
    #print(price_)
    mrp = price_.find_next_sibling("span", class_="a-price a-text-price")
    #print(mrp)
    if (mrp == None):
        mrp = "Not Mentioned"
    else:
        mrp = mrp.find("span", class_="a-offscreen").string
    number_reviews = i.find_next("span", class_="a-size-base").string
    rating = i.find_next("span", class_="a-icon-alt").string

    print("Price :", price)
    print("MRP :", mrp)
    print("Number of Reviews :", number_reviews)
    print("Rating :", rating)

    details = dict()
    details['Name'] = name
    details['Price'] = price
    details['MRP'] = mrp
    details['Number of Reviews'] = number_reviews
    details['Rating'] = rating

    phone_details.append(details)

    count+=1

print(phone_details)
df = pd.DataFrame(phone_details)
print(df)
df.to_csv(r"phone-details.csv",index=True)