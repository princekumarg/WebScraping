from bs4 import BeautifulSoup
import requests 
import pandas as pd
URL="https://www.amazon.in/s?k=phone+under+10000&rh=n%3A1389432031%2Cp_89%3AVivo&dc&ds=v1%3ANnyNPK32h4kqzv0frwd9d81TbOXHEYzjp5v74K8U%2B1E&crid=CFM5UPHFJXAS&qid=1678597048&rnid=3837712031&sprefix=phone+%2Caps%2C471&ref=sr_nr_p_89_4"
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
webpage=requests.get(URL, headers=HEADERS)
#print(webpage)
#print(webpage.content)
#print(type(webpage.content))
soup=BeautifulSoup(webpage.content,'html.parser')
#print(soup)
link=soup.find_all("a",attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
print(link)
link2=soup.find_all("span",attrs={'class':'a-price-whole'})
#print(link2)
x=link[0].get('href')
#print(x)
l='https://www.amazon.in/'+x
print(l)