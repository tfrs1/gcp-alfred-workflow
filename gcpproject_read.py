from __future__ import with_statement
import json

def main():
    try:
        with open('projects.json', 'r') as file:
            data = json.load(file)
            data = {
                "items": [{"title": d, "uid": d, "arg": d} for d in data]
            }
            print json.dumps(data)
    except IOError:
        print json.dumps({"items": [{"title": "Please add a project using 'gcpproject' command."}]})

if __name__ == '__main__':
    main()