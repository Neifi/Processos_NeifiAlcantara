# -*- coding: utf8 -*-
import md5, random, sys, time
from multiprocessing import Process, Semaphore, Pipe

def busca(x, s):
    s.acquire()
    f = open('fitxer.txt', 'r')
    fr = f.read()
    index = fr.find('\n'+x+',')
    index2 = fr.find('\n', index+1)
    if index == -1:
        pass
    else:
        print fr[index+1:index2]
        f.close()
    s.release()

def substitueix(x, y, s):
    s.acquire()
    f = open('fitxer.txt', 'r')
    fr = f.read()
    f.close()
    index = fr.find('\n'+x+',')
    index2 = fr.find('\n', index+1)
    if index == -1:
        print 'Aquest nombre no existeix'
        s.release()
    else:
        print fr[index+1:index2]
        f = open('fitxer.txt', 'w')
        f.write(fr[:index+1])
        f.write(y + ',' + md5.md5(y).hexdigest()+ "\n")
        f.write(fr[index2+1:])
        f.close()
        s.release()
        busca(y, s)


def inici():
    f = open('fitxer.txt', 'w')
    for i in range(100):
        f.write(str(i)+ ',' + md5.md5(str(i)).hexdigest()+ "\n")
    f.close()
    #print open('fitxer.txt', 'ro').read()

def fill(p, s):

    while True:
        p.poll()
        n = p.recv()
        if n == 'q':
            break
        p.poll()
        n2 = p.recv()
        if n2 == 'q':
            break
        substitueix(n, n2, s)


if __name__ == '__main__' :

    inici()
    #x = sys.argv[1]
    #busca(x)

    s = Semaphore(1)
    a, b = Pipe()
    p1 = Process(target=fill, args=[b, s])
    p1.start()
    while True:
        e = raw_input('Nombre a substituir: ')
        a.send(e)
        if e == 'q':
            break
        e = raw_input('Nombre a substitud: ')
        a.send(e)
        if e == 'q':
            break
        time.sleep(1)
    p1.join()
    #substitueix(x)
