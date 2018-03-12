import mechanicalsoup
import requests
from bs4 import BeautifulSoup
import re

def substituteScraper(ingredient):
	browser = mechanicalsoup.StatefulBrowser()
	response = browser.open("http://search.freefind.com/find.html?id=81296093&pageid=r&mode=ALL&n=0&query=" + ingredient)
	try:
		browser.follow_link("foodsubs")
	except:
		print("No appropriate substitute found!")
	currUrl = browser.get_url()
	page = requests.get(currUrl)	
	soup = BeautifulSoup(page.content, 'html.parser')	
	allSubs = soup.find_all("b")
	searchSub = ""
	for i in allSubs:
		searchSub += i.text
	reg = '(' + ingredient + ').*(Substitutes: \w)'
	m = re.search(reg, searchSub, re.IGNORECASE)
	sub = m.group(0)
	print(sub)


substituteScraper("parmesan")	
