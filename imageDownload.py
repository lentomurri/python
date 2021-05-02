#  the program will iterate through a comic website and download a certain number of images
#  can go as far as the beginning or in a set range
#  It will create a folder where to store the img in a set location.
#THIS PROGRAM IS A WEB PARSER. IT'S BUILT AROUND A SPECIFIC WEBSITE. IT CAN BE ADAPTED.

import requests, os, re
from PIL import Image
from bs4 import  BeautifulSoup

if not os.path.exists(r"path_to_folder"):
    os.mkdir(r"path_to_folder")

# LOOP
# get the starting page 
def getComics():
    startingPage = "insert_http_page"
    # iterate through it until the image is found
    number = 0
    while True:
        response = requests.get(startingPage)
        soup = BeautifulSoup(response.content, "html.parser")
        images = soup.findAll("img")
        url = "http:" + images[2]["src"]
        getExtension = url[len(url) -4: len(url)]
        saveImage = Image.open(requests.get(url, stream=True).raw)
        saveImage.save(r"C:\Users\Lento\Desktop\comics folder\comic" + str(number) + getExtension)
        # get the new page to search for 
        previousLink = soup.find(rel = "prev")
        if previousLink["href"] == "#":
            break
        startingPage = "https://xkcd.com" + previousLink["href"]
        number +=1

getComics()
