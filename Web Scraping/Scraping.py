import requests
import bs4

request = requests.get('https://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(request.text,'lxml')

# Getting the namees of all authors on the first page
authors_first_page = set()
auths = soup.select(".author")
for i in range(10):
    authors_first_page.add(auths[i].text)

# Printing authors on the first page
authors_list = sorted(list(authors))
print("Authors on the first page:")
for i in range(len(authors_list)):
    print(i+1,authors_list[i])

# Creating a list of all the quotes on the first page
quotes = []
quos = soup.select(".text")
for i in range(10):
    quotes.append(quos[i].text)

# Printing quotes on the first page
print("Quotes on the first page:")
for i in range(len(quotes)):
    print(i+1,quotes[i])

# Getting top ten tags of the site
toptags = ''
tags = soup.select(".tag-item")
for i in range(10):
    toptags += tags[i].text+"\n"

# Printing top ten tags
print("Top ten tags:")
top_tags_list = toptags.split()
for i in (range(len(top_tags_list))):
    print(i+1,top_tags_list[i])

# Getting all unique authors in the website
base_url = "https://quotes.toscrape.com/page/{}/"
n = 1
authors = set()
while True:
    try:
        scrape_url = base_url.format(n)
        res = requests.get(scrape_url)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        quos = soup.select(".author")
        
        for i in range(10):
            authors.add(quos[i].text)
        n += 1
    except:
        break

# Printing all unique authors in the website
all_authors = list(authors)
print("All authors in the website:")
for i in range(len(all_authors)):
    print(i+1,all_authors[i])
