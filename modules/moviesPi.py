from bs4 import BeautifulSoup
import urllib2


url = urllib2.urlopen("https://www.amctheatres.com/movie-theatres/pittsburgh/amc-loews-waterfront-22")
soup = BeautifulSoup(url)


for link in soup.find_all('a'):
    if "Deadpool" in link.text:
        print link
#     if "Deadpool" in link.div.h4.href:
#         print link