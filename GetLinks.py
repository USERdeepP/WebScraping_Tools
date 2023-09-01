import requests
from bs4 import BeautifulSoup

a = input("Enter the Url of webpage \n > ")
w = input("Enter the name of your output text file \n > ")
page = requests.get(a)
content = BeautifulSoup(page.content,"lxml")

with open(f"{w}.txt","w+") as f:
    f.write("---> Links Are <--- \n")
    for link in content.find_all('a'):
        f.write(link.get('href') + "\n")
