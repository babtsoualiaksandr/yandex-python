import sys
import argparse

import os
import requests
from time import sleep
import subprocess
import json
import pprint
import functools
from statistics import mean





def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', nargs='?', default='127.0.0.1')
    parser.add_argument('port', nargs='?', default='5000')
    parser.add_argument('-nm', '--not_mult', default=100)
    parser.add_argument ('-sm', '--smallest', default=0)
 
    return parser


if __name__ == "__main__":
    parser = createParser()

    namespace = parser.parse_args(sys.argv[1:])

    print(namespace)

    print("Starting server...")
    os.system(f'python -m http.server {namespace.port} &')

    sleep(1)
    cmd = 'echo $$'
    pid = int(subprocess.check_output(cmd, shell=True).decode('UTF-8'))-1
    print(pid)

    url = f'http://{namespace.host}:{namespace.port}/ser.json'
    print(url)
    print("Testing request: ", url)
    r = requests.get(url)
    print("Status code: ", r.status_code)
    req = json.loads(r.text)


    def get_set_from(a, b):
        for key, value in b.items():
            a.add(key)
        return a

    list_reduce = functools.reduce(get_set_from, req, set())
    total = {}
    for name in list_reduce:
        if name in total.keys():
            pass
        else:
            total[name] = []
            for item_list in req:
                for (key, value) in item_list.items():
                    if key == name:
                        total[name] += value
    print(total)
    result =[]
    for key, item in total.items():
        max_items = max(item)
        min_items = min(item)
        mean_items = round(mean(item), 2)
        sum_items = sum(item)
        result.append(f'{key}; {max_items}; {min_items}; {mean_items}; {sum_items}')

    sleep(3)
    pprint.pprint(sorted(result))
    f = open("truth.csv", "w")
    for item in sorted(result):     
        f.writelines(str(item) + '\n')
    f.close()
    print("Stopping server...")
    os.system(f'kill -9 {pid}')




    