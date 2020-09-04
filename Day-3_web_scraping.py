import webbrowser, requests

url = 'http://books.toscrape.com/'
webbrowser.open(url)

res = requests.get(url)

res.raise_for_status() # similiar to assert but raise error if got error

assert res.status_code == requests.codes.ok ,'request not sucessful' # 200 is OK in HTTP protocol

print(len(res.text))

print(res.text[:1000])