# -*- coding: UTF-8 -*-
import csv
import re
import requests	

from bs4 import BeautifulSoup 
from math import ceil
from random import shuffle, randint

random_searches = ['haberler', 'youtube', 'youtube+com', 'yavru+köpek', 
					'yavru+kedi', 'vatanım+sensin', 'google',
					'gmail', 'açıköğretim', 'turkcell', 'ösym', 'yemeksepeti', 
					'facebook', 'face', 'yemek+tarifleri',
					'dizi+film+izle', 'sağlık', 'doktor', 'sinema', 'eczane', 
					'gazete', 'maç+skoru', 'maç', 'fikstür',
					'magazin', 'survivor', 'instagram']

# Returns [ad]
def search_crawler(URL, session, user_agent):
	headers = {
	    'User-Agent': user_agent,
	    'Accept' : 
	    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	    'Accept-Language' : 'tr-tr;q=0.5',  #'en-US,en;q=0.5',
	    'Accept-Encoding' : 'gzip',
	    #'DNT' : '1', # Do Not Track Request Header
	    'Connection' : 'close'
	}

	resp = session.get(URL, headers=headers).text 
	soup = BeautifulSoup(resp, 'html.parser')

	ads = list()
	for div in soup.find_all('div', {'class': re.compile(r'ad_cclk')}):
		#print(div)
		for link in div.findAll('a', href=True): 
		    if link.get('href').startswith('https://'):
		    	#print (link.get('href'))
		    	ads.append(link.get('href'))
	return ads

#returns [search]
def generate_searches(adjectives, names, iterations = 1000):
	lenght = len(adjectives)
	google_searches = set()
	for iteration in range(1,iterations):
		shuffle(names)
		shuffle(adjectives)
		for name in names[1:randint(2, ceil((lenght-1)/2))]:
			searh_url ='https://www.google.com.tr/search?client=firefox-b-d&q='\
							+ adjectives[randint(1, lenght-1)]  + '+' + name
			google_searches.add(searh_url)
	print('Number of queries:', len(google_searches))
	return google_searches

def generate_searches_oneinput(keywords):

	lenght = len(keywords)
	google_searches = set()
	shuffle(keywords)
	for keyword in keywords[1:randint(2, ceil((lenght-1)/4))]:
		searh_url = 'https://www.google.com.tr/search?client=firefox-b-d&q='\
						+ keywords[randint(1, lenght-1)]
		google_searches.add(searh_url)
	print('Number of queries:', len(google_searches))
	return google_searches

# Returns [[URL, ad]]
def crawl_and_search(shopping_sites, google_searches, user_agent,iterations=20):
	headers = {
	    'User-Agent': user_agent,
	    'Accept' : 
	    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	    'Accept-Language' : 'tr-tr;q=0.5',  #'en-US,en;q=0.5',
	    'Accept-Encoding' : 'gzip',
	    #'DNT' : '1', # Do Not Track Request Header
	    'Connection' : 'close'
	}

	searches_and_ads = set()
	with requests.Session() as s:
		for iteration in range(1,iterations):
			shuffle(shopping_sites)
			lenght = len(shopping_sites)
			print('Iteration:', iteration, '/', iterations)
			for URL in shopping_sites[1:randint(1, ceil((lenght-1)/2))]:
				print("Crawling:", URL)
				try:
					s.get(URL, headers=headers)
				except Exception as e: print(e)
			print('Number of cookies:',len(s.cookies.get_dict()))
			for URL in google_searches:
				s.get(URL, headers=headers)
				print("Searching:", URL)
				try:
					ads = search_crawler(URL, s, user_agent)
					for ad in ads:
						s.get(URL, headers=headers)
						print("		Ad:", ad)
						searches_and_ads.add([URL, ad])
				except Exception as e: print(e)
	return searches_and_ads

def write_to_csv(adjectives, names, websites, iterations, user_agent, 
	query_type, user_type, device_type = 'Unknown', device_brand = 'Unknown'):

	google_searches = generate_searches_oneinput(random_searches) +\
						generate_searches(adjectives, names, 3)
	shuffle(google_searches)
	ads = crawl_and_search(websites, google_searches, user_agent, iterations)
	print('ads:', ads)
	try:
		with open('advertisements.csv', 'a') as csvfile:
			for entry in ads: 
				writer = csv.writer(csvfile)
				writer.writerow([entry[0], entry[1], query_type, user_type, 
								device_type, device_brand])
	except Exception as e:print('Error %s' % e ) 
