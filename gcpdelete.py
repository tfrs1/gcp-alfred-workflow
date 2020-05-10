from __future__ import with_statement
import json
import sys

def main(proj):
    projects_filename = 'projects.json'
    try:
        with open(projects_filename, 'r') as file:
            data = json.load(file)
    except:
        data = []
    
    with open(projects_filename, 'w') as file:
        data.remove(proj)
        file.write(json.dumps(list(set(data))))

if __name__ == '__main__':
    proj = sys.argv[1]

    main(proj)
