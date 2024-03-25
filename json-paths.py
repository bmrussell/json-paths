import argparse
import json


def get_paths(d):
    if isinstance(d, dict):
        for key, value in d.items():
            yield f'.{key}'
            yield from (f'.{key}{p}' for p in get_paths(value))
        
    elif isinstance(d, list):
        for i, value in enumerate(d):
            yield f'[{i}]'
            yield from (f'[{i}]{p}' for p in get_paths(value))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print paths for JSON file.')
    parser.add_argument('--json', required=True, help='JSON file to print paths for')
    args = parser.parse_args()
    
    with open(args.json) as json_file:
        d = json.load(json_file)

    for i in list(get_paths(d)):
        if "[" in i:
            if "[0]" in i and i[-3:] != "[0]":
                print(i.replace("[0]", "[]"))
        else:
            print(i)
            
            