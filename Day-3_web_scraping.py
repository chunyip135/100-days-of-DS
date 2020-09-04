import webbrowser, requests, bs4, pprint

url = 'http://books.toscrape.com/'
webbrowser.open(url)

res = requests.get(url)

res.raise_for_status() # similiar to assert but raise error if got error

assert res.status_code == requests.codes.ok ,'request not sucessful' # 200 is OK in HTTP protocol

print(len(res.text))

print(res.text[:250])

# creating BeautifulSoup Object from HTML
bookstore = bs4.BeautifulSoup(res.text) # print out entire html

# extract all book names
titles = bookstore.select('.product_pod > h3 > a ')

bookname = list()
for title in titles:
	bookname.append(title.getText().split('.')[0])

bookname = list()
for title in titles:
	bookname.append(title.get('title')) # simpler

# extract all book's price
prices = bookstore.select('.price_color')

bookprice = list()
for price in prices:
	bookprice.append(price.getText()[1:])

# extract all book's stock availability
stocks = bookstore.select('.availability.instock')
stock = [True for t in stocks if 'In stock' in str(t)]

catalog = dict()
for i,name in enumerate(bookname):
	catalog[name] = [bookprice[i], stock[i]]

pprint.pprint(catalog)