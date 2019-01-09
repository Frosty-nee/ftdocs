#! python3

import sys

from groups import groups
from commands import commands
from tables import tables

if __name__ == '__main__': 
    if len(sys.argv) > 1:
        arg = ' '.join(sys.argv[1:])
        if arg in groups:
            for command in groups[arg]:
                print(command)
        elif arg in commands:
            for pair in commands[arg].items():
                print('{:20} {}'.format(*pair))
        elif arg in tables:
            for pair in tables[arg].items():
                print('{:20} {}'.format(*pair))
        else: print('command or command group not found')
    else:
        print("Command Groups:")
        for line in groups.keys():
            print(line)
        print('\nTables:')
        for line in tables.keys():
            print(line)
