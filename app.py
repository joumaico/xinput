#!/usr/bin/python3.11

import pathlib
import re
import subprocess
import tomllib


def main():
    path = pathlib.Path(__file__)

    with open(path.parent / 'config.toml', 'rb') as f:
        data = tomllib.load(f)

    for item in subprocess.check_output(['xinput', '--list']).decode().split('\n'):
        if (match := re.search(r'id=(\d+)', item)):
            for d in data['ENABLE']['devices']:
                if d in item:
                    subprocess.run(['xinput', 'enable', match.group(1)])
                    break
            for d in data['DISABLE']['devices']:
                if d in item:
                    subprocess.run(['xinput', 'disable', match.group(1)])
                    break


if __name__ == '__main__':
    main()
