#!/usr/bin/python3
"""extend your Python script to export data in the JSON format"""
from json import dump
import requests


if __name__ == '__main__':

    users_response = requests.get(
        'https://jsonplaceholder.typicode.com/users/')
    todos_response = requests.get(
        'https://jsonplaceholder.typicode.com/todos/')

    users = {}
    for user in users_response.json():
        users[user['id']] = user['username']

    tasks = {}
    for uid, uname in users.items():
        for todo in todos_response.json():
            if todo['userId'] == uid:
                tasks.setdefault(uid, [])
                tasks[uid].append(dict(username=uname,
                                       task=todo['title'],
                                       completed=todo['completed']))

    with open('todo_all_employees.json', 'w') as f:
        dump(tasks, f)
