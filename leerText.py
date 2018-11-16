import sys

def leer_serie_numerica(file):
    with open(file, mode = 'rt') as f:
        serie = []
        for line in f:
            a = int(line.strip())
            serie.append(a)
    
    return serie

def main(file):
    series = leer_serie_numerica(file)
    print(series)

if __name__ == '__main__':
    main(sys.argv[1])