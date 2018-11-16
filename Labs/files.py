import sys

def main(filename):
    encode = sys.getdefaultencoding()
    f = open(filename, mode = 'rt', encoding = encode)
    for linea in f:
        sys.stdout.write(linea)
    f.close()

if __name__ == '__main__':
    main(sys.argv[1])


