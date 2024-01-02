#!/usr/bin/python3
import requests
import sys

para = sys.argv[1]
r = requests.get(f'https://jsonplaceholder.typicode.com/users/{para}')
t = requests.get(f'https://jsonplaceholder.typicode.com/todos/?userId={para}')
completed = 0
tasks = 0
todo = t.json()

for i in todo:
    if i['completed']:
        completed += 1
    tasks += 1
data = r.json()

print(f'Employee {data["name"]} is done with tasks({completed}/{tasks}):')
for j in todo:
    if j['completed']:
        print("\t {}".format(j['title']))
