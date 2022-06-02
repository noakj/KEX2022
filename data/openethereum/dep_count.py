import sys
import json

if __name__ == "__main__":

    infile = sys.argv[-1]

    with open(infile, 'r') as f:
        deps = json.load(f)

    count = 0
    for gav in deps.keys():
        count += len(deps[gav])

    print(count)
