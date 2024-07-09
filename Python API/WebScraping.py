# install BeautifulSoup4 pacakge
"""

import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://risenshinetechnologies.com/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup)

header = soup.find("h1", class_='rns-h1')

print(header.text)

"""

import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://www.python.org/jobs/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup)

finding_jobs = soup.find_all('h2', class_='listing-company')
# print(type(finding_company))

# for job_post in finding_jobs:
#     print(job_post.a.text)

finding_posted_date = soup.find_all('span', class_='listing-posted')
# print(finding_posted_data)

# for posted_date in finding_posted_date:
#     print(posted_date.time.text)

for job_post, posted_date in zip(finding_jobs, finding_posted_date):
    print(job_post.a.text, posted_date.time.text)