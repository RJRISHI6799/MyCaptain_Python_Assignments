import requests
from bs4 import BeautifulSoup
import pandas as pd

wiki_url = "https://www.wikipedia.org/"

req = requests.get(wiki_url)
content = req.content

soup = BeautifulSoup(content, "html.parser")

all_projects = soup.find_all("div", {"class": "other-project"})
scraped_info_list = []

for project in all_projects:
    project_name = project.find("a", {"class": "other-project-link"}).text.strip()
    print(project_name)
    scraped_info_list.append(project_name)

dataframe = pd.DataFrame(scraped_info_list, columns=["Project Name"])
dataframe.to_csv("wiki.csv", index=False)
