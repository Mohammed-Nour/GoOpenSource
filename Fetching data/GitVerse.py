import requests
from bs4 import BeautifulSoup

URL = "https://gitverse.ru/explore/repos"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

# Find all <a> tags with class "block min-w-0 hover:underline"
a_tags = soup.find_all('a', class_="block min-w-0 hover:underline")

# Extract href values from each <a> tag and prepend "https://gitverse.ru"
href_values = [tag['href'] for tag in a_tags]

#href_values = ["https://gitverse.ru" + tag['href'] for tag in a_tags]
projects =[]
for link in href_values:

  new_link= link[1:]
  print(new_link)
  parts = new_link.split('/')

  dic={}


  URL ="https://gitverse.ru" + link
  r = requests.get(URL)

  soup = BeautifulSoup(r.content, 'html5lib')
  stars = soup.find_all('span',class_="text-gr-50 group-hover:text-bl-65")
  descriptions = soup.find_all('h4',class_="text-h4")
  forks=  soup.find_all('div',class_="px-1.5 py-0.5 inline-flex items-center justify-center border-none rounded-full text-small tracking-[0.00625rem] bg-gr-93 text-gr-35 h-5 min-w-[20px] text-small")


  dic['contributorsName']=parts[0]
  dic['contributorsAccount']="https://gitverse.ru" + parts[0]
  dic['contributorsPhoto']=""
  dic[ 'contributorsRole']="owner"
  dic['repositoryName']= link
  dic['repositoryFullName']=  link
  dic['repoUrl']= "https://gitverse.ru" + link
  dic['stars']=0
  dic['forks'] =0
  dic['topics']=0
  dic['readmeURL']="https://gitverse.ru" + link +"/content/master/README.md"
  dic['contributorsCount']= ''
  dic['commitsCount']=''
  dic['description']=descriptions
  dic['language']=''
  projects.append(dic)


print(len(href_values))
#print(href_values)
print(projects[0])

import csv
csv_filename = 'repository_features.csv'

feature_names = ['contributorsName','contributorsAccount','contributorsPhoto','contributorsRole','repositoryName','repositoryFullName', 'repoUrl','stars', 'forks', 'lastUpdate', 'size', 'topics', 'readmeURL','contributorsCount','commitsCount','descriptions','language']

with open(csv_filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(feature_names)

    for repo in (projects):
        #print(i)
        contributorsName = repo['contributorsName']
        contributorsAccount =repo['contributorsAccount']
        contributorsPhoto = repo['contributorsPhoto']
        contributorsRole='owner'
        repositoryName = repo['repositoryName']
        repositoryFullName = repo['repositoryFullName']
        repoUrl= repo['repoUrl']
        stars = repo['stars']

        forks = repo['forks']

        lastUpdate = ''
        size = 0
        topics=repo['topics']
        topics = []
        readmeURL = repo['readmeURL']
        contributorsCount= ''
        commitsCount=''
        descriptions=repo['description']
        language='none'
        row = [contributorsName,contributorsAccount,contributorsPhoto,contributorsRole,repositoryName,repositoryFullName, repoUrl,stars, forks, lastUpdate, size, topics, readmeURL,contributorsCount,commitsCount,descriptions,language]

        #row = [name, full_name, stars, forks, last_update, size, topics, readme_url,description]

        writer.writerow(row)

print(f"Data for {len(projects)} repositories saved to {csv_filename}")
