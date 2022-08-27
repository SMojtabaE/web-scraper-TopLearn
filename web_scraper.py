import requests
from bs4 import BeautifulSoup

# get the contents of page using request 
url = "https://toplearn.com/courses/2150/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-(-python-)"
page = requests.get(url)
soup = BeautifulSoup(page.content,'xml')

#find the title using HTML tags
name_first = soup.find_all('h2',{"class" : "view-Live"})
names = []

#extract the titles and append them in a list
for name in name_first:
    names.append(name.string)

#write titles in a txt file
with open("python_cours_videos_title.txt" , 'w', encoding='utf-8') as file:
    for i in range(0,len(names)):
        line = str(str(i +1) + ":" + names[i] + "\n")
        file.write(line)