from blessed import Terminal
import time

def main(data, delay):
    lines = [data]

    term = Terminal()

    with term.fullscreen():
        print(term.normal + term.clear)
        input() # wait for input to start
        for j, line in enumerate(lines):
            for i in range(len(line) - 3):
                isUnique = True

                four = line[i:i+4]
                string = ""
                for l in four:
                    if four.count(l) - 1:
                        isUnique = False
                        string += term.on_red
                    else:
                        string += term.on_yellow

                    string += l

                with term.location(0, j):
                    print(term.cleareol + line[:i] + term.on_yellow + string + term.normal + line[i+4:] + ' -', i+4)

                if isUnique:
                    break

                time.sleep(delay)

        for j, line in enumerate(lines):
            for i in range(len(line) - 3):
                isUnique = True

                fourteen = line[i:i+14]
                string = ""
                for l in fourteen:
                    if fourteen.count(l) - 1:
                        isUnique = False
                        string += term.on_red
                    else:
                        string += term.on_yellow

                    string += l

                with term.location(0, j+(len(max(lines))//222)+1):
                    print(term.cleareol + line[:i] + term.on_yellow + string + term.normal + line[i+14:] + ' -', i+14)

                if isUnique:
                    break

                time.sleep(delay)
        with term.location(0, len(line)*2 + 2):
            input() # wait for input to end
            print(term.clear)