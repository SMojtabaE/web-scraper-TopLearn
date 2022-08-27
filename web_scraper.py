import requests
from bs4 import BeautifulSoup

page = requests.get("https://toplearn.com/courses/2150/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-(-python-)")
soup = BeautifulSoup(page.content,'xml')