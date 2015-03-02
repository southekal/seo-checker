import sys
from bs4 import BeautifulSoup
import requests


def arg_checker():
    if len(sys.argv) == 1:
        print 'Format should be "python page.py [URL]"'
    else:
        request_url()


def request_url():
    r = requests.get(sys.argv[1])
    soup = BeautifulSoup(r.text)
    print title_checker(soup)
    print h1_checker(soup)
    print h2_checker(soup)
    print h3_checker(soup)
    print desc_checker(soup)
    print keyword_checker(soup)


def title_checker(soup):
    titles = []
    for title in soup.find_all('title'):
        titles.append(str(title.text.encode('utf-8')))
    return titles


def h1_checker(soup):
    header1 = []
    for h1 in soup.find_all('h1'):
        header1.append(str(h1))
    return header1


def h2_checker(soup):
    header2 = []
    for h2 in soup.find_all('h2'):
        header2.append(str(h2))
    return header2


def h3_checker(soup):
    header3 = []
    for h3 in soup.find_all('h3'):
        header3.append(str(h3))
    return header3


def desc_checker(soup):
    description = []
    for desc in soup.find_all('meta', attrs={'name': 'description'}):  # name is a reserved keyword and
    #  has to be used with attrs!
        description.append(str(desc.get('content')))
    return description


def keyword_checker(soup):
    keywords = []
    for keyword in soup.find_all('meta', attrs={'name': 'keywords'}):
        keywords.append(str(keyword.get('content')))
    return keywords

arg_checker()



