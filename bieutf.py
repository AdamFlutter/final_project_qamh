from bs4 import BeautifulSoup
import os
def half(content):
    soup = BeautifulSoup(content,"html.parser")
    form = soup.find("form")
    form["action"] = "/"
    file = open("fffff.html",'w').write(str(soup))
    return str(soup)
    