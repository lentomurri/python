# The program will paste a search into a "GialloZafferano" page (recipe website) and open the first 4 links

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import sys, requests

recipeFile = open(r"C:\Users\Lento\Desktop\recipe.txt", "a")

# TODO search for the form id and fill it with the sys.argv string
string = " ".join(sys.argv[1:]) # temporary string 
op = webdriver.ChromeOptions()
op.add_argument("log-level=3")
# op.add_argument("headless")

driver = webdriver.Chrome(r"C:\Users\Lento\Downloads\chromedriver_win32 (1)\chromedriver.exe", options=op)
driver.get("https://www.giallozafferano.it/ricerca-ricette/" + string)

links = driver.find_elements_by_xpath("//h2[@class='gz-title']/a")
relatedRecipes = []
for link in links:
    relatedRecipes.append((link.get_attribute("href")))

for url in relatedRecipes[:4]:
    driver.get(url)
    ingredients = driver.find_element_by_xpath("//div[@class='gz-ingredients gz-mBottom4x gz-outer']")
    recipeFile.write("---")
    recipeFile.write(ingredients.text)
    recipeFile.write("\n")
    steps = driver.find_elements_by_xpath("//div[@class='gz-content-recipe-step']/p")
    for step in steps:
        soupIngredient = str(BeautifulSoup(step.text, "html.parser"))
        recipeFile.write(soupIngredient)
    recipeFile.write("\n")


recipeFile.close()

# TODO click the form, find the first 4 recipes link 
# TODO open them, find the text, copy it
# TODO create txt file and past all the recipes one after the other 