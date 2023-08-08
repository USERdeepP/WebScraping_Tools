import requests
from bs4 import BeautifulSoup
# taking input of url from the user 
a = input("Enter the Url of webpage \n > ")
w = input("Enter the name of your text file \n > ")

# requesting the url
b = requests.get(a)
c = b.content

# making content more readable and saving it to a text file
soup = BeautifulSoup(c , 'lxml')
z = soup.prettify
print(z)
with open(f"{w}.txt" , "w+") as f:
    f.write("\n ------> The Html Content of your page <------ \n")
    f.write(f"\n url is ({a}) \n\n")
    f.write(f"{z}")