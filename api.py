# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:09:18 2019

@author: adityaroyal
"""
from github import Github
import sys
g = Github("amattur@bgsu.edu", "Lokam@123")
#for repo in g.get_user().get_repos():
#    print(repo.id,repo.name)

repo = g.get_repo("adityaroyalm/Informatica")
try:
    contents = repo.get_contents("")
except:
    print('repo is empty')
    sys.exit()
#for content_file in contents:
#    print(content_file)
import wget
for c in contents:
    wget.download('https://raw.githubusercontent.com/adityaroyalm/Informatica/master/'+str(c.name),r'C:\Users\adityaroyal\github\output')
repo.create_file('test8.txt','jn','n')