import os
import platform
import argparse

parser = argparse.ArgumentParser(description="SatsumaProject Giga Text Editor 1.1")

parser.add_argument('-o', '--open', type=str, help='Open File')


args = parser.parse_args()

if args.open:

    def get_input():

        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Darwin':
            os.system('clear')
        elif platform.system() == 'Linux':
            os.system('clear')

        indentvers = os.get_terminal_size().columns - 49
        indentvers2 = indentvers // 2

        print('-'*os.get_terminal_size().columns)
        print('|',' '*indentvers2,'SatsumaProject Giga Text Editor Version 1.2',' '*indentvers2,'|')
        print('-'*os.get_terminal_size().columns)

        print('|')

        lines = []

        while True:
            line = input('|')
            if line.strip() == '#END':
                break
            elif line.strip() == '#DEL':
                if lines:
                    lines.pop()
                    try:
                        print("\033[F\033[K", end="")
                        print("\033[F\033[K", end="")
                    except:
                        print('Last Line Has Been Removed')
            else:
                lines.append(line)

        return lines


    indentvers = os.get_terminal_size().columns - 9
    indentvers2 = indentvers // 2

    text = get_input()

    for x in range(3):

        print('')

    print('-'*os.get_terminal_size().columns)
    file = args.open
    print(' '*indentvers2+'File Saved As '+file)

    with open(file, 'w') as file:
        for line in text:
            file.write(line + '\n')