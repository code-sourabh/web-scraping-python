#!/usr/bin/env python
# coding: utf-8
# # GoTrained - Web Scraping with Python - Getting Started
#  
# - Python web scraping libraries you need for the course and how to install them.
# - How to extract URLs from one webpage.
# - How to extract other text data pieces from one webpage.
# - How to crawl multiple webpages and extract data from each of them.
# - How to handle navigation links and move to *next* pages.
# - How to save your scraped data into a CSV file.
# - And finally, a quick overview about *other* popular web scraping frameworks.

from bs4 import BeautifulSoup
import requests 


url = "https://boston.craigslist.org/search/sof"


response = requests.get(url)


#print(response)


data = response.text


soup = BeautifulSoup(data,'html.parser')


jobs = soup.find_all('p',{'class':'result-info'})


for job in jobs:
    title = job.find('a',{'class':'result-title'}).text
    location_tag = job.find('span',{'class':'result-hood'})
    location = location_tag.text[2:-1] if location_tag else "N/A"
    date = job.find('time', {'class': 'result-date'}).text
    link = job.find('a', {'class': 'result-title'}).get('href')
    job_response = requests.get(link)
    job_data = job_response.text
    job_soup = BeautifulSoup(job_data, 'html.parser')
    job_description = job_soup.find('section',{'id':'postingbody'}).text
    job_attributes_tag = job_soup.find('p',{'class':'attrgroup'})
    job_attributes = job_attributes_tag.text if job_attributes_tag else "N/A"
    
    print('Job Title:', title, '\nLocation:', location, '\nDate:', date, '\nLink:', link,"\n", job_attributes, '\nJob Description:', job_description,'\n---')



