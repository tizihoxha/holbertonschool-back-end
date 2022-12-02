#!/usr/bin/python3
"""returns information about his/her TODO list progress"""
import urllib.request
import json
import sys


if __name__ == '__main__':
    uId = int(sys.argv[1])
    toDoList = []
    compTask = 0
    tasks = 0
    with urllib.request.urlopen('https://jsonplaceholder'
                                '.typicode.com/users') as response:
        users = json.loads(response.read().decode())
        for user in users:
            if user['id'] == uId:
                userName = user['name']

    with urllib.request.urlopen('https://jsonplaceholder'
                                '.typicode.com/todos') as response:
        jsonDict = json.loads(response.read().decode())
        for line in jsonDict:
            if line['userId'] == uId:
                if line['completed'] is True:
                    string = ("\t " + line['title'])
                    toDoList.append(string)
                    compTask += 1
                tasks += 1

    print(f"Employee {userName} is done with tasks({compTask}/{tasks}):")
    for att in toDoList:
        print(att)
