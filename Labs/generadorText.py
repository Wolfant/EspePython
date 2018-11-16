import sys
def secuencia(count):
    seq = 0
    while True:
        yield seq
        seq +=1
        if seq == count:
            break

def escribe_sequencia(file, num):
    f = open(file, mode='wt')
    f.writelines('{}\n'.format(r) for r in secuencia(num) )
    f.close()

if __name__ == '__main__':
    escribe_sequencia(sys.argv[1], sys.argv[2])

