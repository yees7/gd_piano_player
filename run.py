import sys
import os
from src.convert_music import convert_music

def main():
    l = len(sys.argv)
    if l <= 1:
        print("Expected up to two arguments, 0 were given")
        return
    elif l > 3:
        print("Expected up to two arguments, "+str(l-1)+" were given")
        return

    convert_music(sys.argv[1])
    if l == 2:
        os.system("spwn build src/create_triggers.spwn --allow readfile")
    else:
        os.system("spwn build src/create_triggers.spwn --level-name " + sys.argv[2] + " --allow readfile")

if __name__ == '__main__':
    main()