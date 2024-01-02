#!/usr/bin/python3
"""fetches from JSONplaceholder API and exports to json file"""

import json
from requests import get
from sys import argv


if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com"
    todo_url = main_url + "/user/{}/todos".format(argv[1])
    name_url = main_url + "/users/{}".format(argv[1])
    todos = get(todo_url).json()
    names = get(name_url).json()

    todo_list = []
    for todo in todos:
        todo_dict = {}
        todo_dict.update({"user_ID": argv[1], "username": names.get(
            "username"), "completed": todo.get("completed"),
                          "task": todo.get("title")})
        todo_list.append(todo_dict)
    with open("{}.json".format(argv[1]), 'w') as f:
        json.dump({argv[1]: todo_list}, f)
